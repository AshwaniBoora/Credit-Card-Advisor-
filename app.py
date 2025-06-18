from flask import Flask, render_template, redirect, request, session
from models import db, Card
from forms import Step1Form, Step2Form, Step3Form, Step4Form

app = Flask(__name__)
app.secret_key = 'your-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
db.init_app(app)

@app.route('/')
def index():
    return redirect('/step1')

@app.route('/step1', methods=['GET', 'POST'])
def step1():
    form = Step1Form()
    if form.validate_on_submit():
        session['income'] = form.income.data
        session['credit_score'] = form.credit_score.data
        return redirect('/step2')
    return render_template('step1.html', form=form)

@app.route('/step2', methods=['GET', 'POST'])
def step2():
    form = Step2Form()
    if form.validate_on_submit():
        session['fuel'] = form.fuel.data
        session['travel'] = form.travel.data
        session['groceries'] = form.groceries.data
        session['dining'] = form.dining.data
        return redirect('/step3')
    return render_template('step2.html', form=form)

@app.route('/step3', methods=['GET', 'POST'])
def step3():
    form = Step3Form()
    if form.validate_on_submit():
        session['benefits'] = form.benefits.data
        return redirect('/step4')
    return render_template('step3.html', form=form)

@app.route('/step4', methods=['GET', 'POST'])
def step4():
    form = Step4Form()
    if form.validate_on_submit():
        return redirect('/results')
    return render_template('step4.html', form=form)

@app.route('/results')
def results():
    income = int(session['income'])
    benefits = session['benefits']
    travel_spend = int(session['travel'])
    cards = Card.query.all()

    scored = []
    for card in cards:
        if income < card.min_income:
            continue
        score = 0
        if 'travel' in benefits and card.reward_type == 'Travel Points':
            score += travel_spend * card.reward_rate / 100
        if 'lounge' in benefits:
            score += card.lounge_accesses * 10
        scored.append((card, score))

    top_cards = sorted(scored, key=lambda x: x[1], reverse=True)[:3]
    return render_template('results.html', cards=[x[0] for x in top_cards])