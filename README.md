# Mr Stickerman - Flask Web Application

A complete Flask web application for Mr Stickerman sticker store, built as a learning project for Australian students.

## About

Mr Stickerman is a Bundaberg-based sticker store specialising in premium waterproof vinyl sticker packs. This web application allows customers to browse products, add items to their basket, and complete orders.

## Features

- **Product Catalogue**: Browse all sticker packs with search functionality
- **Product Details**: View detailed specifications for each product
- **Shopping Basket**: Add products to basket and manage orders
- **Checkout System**: Complete orders with customer details using Flask-WTF forms
- **Database Seeding**: Automatically populate the database with sample products
- **Responsive Design**: Bootstrap 4.3.1 for mobile-friendly interface
- **Australian Context**: Uses Australian English spelling and metric measurements

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone or download this repository**

2. **Navigate to the project directory**
   ```bash
   cd StickerStore
   ```

3. **Install the required Python packages**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - Flask 2.3.0
   - Flask-SQLAlchemy 3.0.0
   - Flask-WTF 1.1.0
   - email-validator 2.0.0
   - Flask-Bootstrap 3.3.7.1
   - WTForms 3.0.0

## Running the Application

1. **Start the Flask application**
   ```bash
   python run.py
   ```

2. **Open your web browser and navigate to**
   ```
   http://localhost:5000
   ```

3. **Seed the database with sample products** (first time only)
   
   Visit: `http://localhost:5000/admin/dbseed`
   
   This will populate the database with 20 sticker pack products.

## Using the Application

### Browse Products
- The home page displays all available sticker packs
- Use the search bar to find specific products
- Click "View Details" to see product specifications

### Add to Basket
- Click "Add to Basket" on any product
- View your basket by clicking "Basket" in the navigation

### Checkout
- In your basket, click "Proceed to Checkout"
- Fill in your customer details
- Click "Complete Order" to finalise your purchase

### Clear Basket
- Use "Remove" to delete individual items
- Use "Clear Basket" to empty your entire basket

## Project Structure

```
StickerStore/
├── mrstickerman/           # Main application package
│   ├── __init__.py         # Application factory
│   ├── models.py           # Database models
│   ├── views.py            # Main routes and views
│   ├── admin.py            # Admin routes (database seeding)
│   ├── forms.py            # Flask-WTF forms
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── index.html      # Home page
│   │   ├── product_detail.html
│   │   ├── basket.html     # Shopping basket
│   │   └── checkout.html   # Checkout form
│   └── static/             # Static files
│       └── images/         # Product images
├── run.py                  # Application launcher
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Database

The application uses SQLite database (`mrstickerman.sqlite`) which is created automatically when you run the application.

### Database Models

**Product**
- id (Primary Key)
- name
- description
- price
- category
- sticker_count
- size (in cm)
- material
- finish (Glossy/Matte)
- image_url
- in_stock

**Order**
- id (Primary Key)
- status (False = in basket, True = completed)
- firstname
- surname
- email
- phone
- totalcost
- date
- products (Many-to-many relationship)

## Key Features Explained

### Session-Based Basket
The application uses Flask sessions to maintain a shopping basket for each user. The `order_id` is stored in the session and links to an Order in the database.

### Australian English
The application consistently uses Australian English spelling:
- "colour" instead of "color"
- "favourite" instead of "favorite"
- "specialise" instead of "specialize"
- "organised" instead of "organized"

### Metric Measurements
All product specifications use metric units:
- Sizes: 3-6 cm
- Weights: grams (where applicable)

## Routes

- `/` - Home page with product catalogue
- `/product/<id>` - Product detail page
- `/order` - Shopping basket (GET to view, POST to add items)
- `/deleteorderitem` - Remove single item from basket
- `/deleteorder` - Clear entire basket
- `/checkout` - Checkout page with customer form
- `/admin/dbseed` - Seed database with products

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **WTForms**: Form handling and validation
- **Bootstrap 4.3.1**: CSS framework for responsive design
- **Jinja2**: Template engine

## Development Notes

- Debug mode is enabled by default in `run.py`
- The database file is created in the project root directory
- Static files (images) are served from `mrstickerman/static/`
- Flash messages are used to provide user feedback

## Troubleshooting

**Issue**: Database not found
- **Solution**: Run `python run.py` which creates the database automatically

**Issue**: No products showing
- **Solution**: Visit `/admin/dbseed` to populate the database

**Issue**: Images not loading
- **Solution**: Ensure all images are in `mrstickerman/static/images/`

## Learning Resources

This project demonstrates:
- Flask application structure and blueprints
- Database models with SQLAlchemy
- Many-to-many relationships
- Form handling with Flask-WTF
- Session management
- Template inheritance with Jinja2
- Bootstrap integration

## Support

For questions or issues, please contact:
- Email: hello@mrstickerman.com.au
- Phone: (07) 4152 8834

## Licence

Educational project for learning purposes.

---

© 2025 Mr Stickerman. All Rights Reserved.
