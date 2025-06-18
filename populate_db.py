from app import app
from models import db, Card

app.app_context().push()
db.drop_all()
db.create_all()

sample_cards = [
    Card(name="Axis Atlas", issuer="Axis Bank", joining_fee=5000, annual_fee=5000,
         reward_type="Travel Points", reward_rate=2.5, lounge_accesses=12,
         min_income=50000, perks="12 domestic + 6 international lounge visits",
         image_url="/static/images/axis_atlas.png", apply_link="#"),
    Card(name="HSBC TravelOne", issuer="HSBC", joining_fee=4999, annual_fee=4999,
         reward_type="Travel Points", reward_rate=2.0, lounge_accesses=10,
         min_income=45000, perks="6 domestic + 4 international lounge visits",
         image_url="/static/images/hsbc_travelone.png", apply_link="#"),
    Card(name="SBI Cashback Card", issuer="SBI", joining_fee=999, annual_fee=999,
         reward_type="Cashback", reward_rate=1.0, lounge_accesses=0,
         min_income=30000, perks="5% cashback on online spends",
         image_url="/static/images/sbi_cashback.png", apply_link="#"),
    # Add more cards to make it 20+
]

db.session.add_all(sample_cards)
db.session.commit()
print("Database populated!")