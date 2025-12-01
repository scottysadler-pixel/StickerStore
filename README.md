# Mr Stickerman - Sticker Store

A Flask web application for an online sticker store based in Bundaberg, Australia.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Seed the database with products:
```
python seed_db.py
```

3. Run the app:
```
python run.py
```

4. Open browser to: http://localhost:5000

## Features

- Browse sticker packs by category
- Search for products
- View product details
- Add items to shopping basket
- Update quantities and remove items
- Checkout with customer details
- Order confirmation

## Technologies Used

- Python Flask
- Flask-SQLAlchemy (SQLite database)
- Flask-WTF (forms and validation)
- Bootstrap 4

## Database Structure

- Products - stores all sticker pack info
- Orders - stores customer orders
- OrderDetails - stores items in each order
