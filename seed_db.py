#!/usr/bin/env python3
"""
Database seeding script for Mr Stickerman
Populates the database with sample sticker products
"""
from mrstickerman import create_app, db
from mrstickerman.models import Product

app = create_app()

def seed_database():
    """Add sample products to the database."""
    with app.app_context():
        # Clear existing products
        Product.query.delete()
        
        # Sample products based on available images
        products = [
            Product(
                name="Simpsons Pack",
                description="Classic Simpsons characters - Homer, Marge, Bart, Lisa, and more! Perfect for fans of the iconic TV show.",
                price=3.99,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="simpsons.webp",
                in_stock=True
            ),
            Product(
                name="Pokemon Pack",
                description="Catch 'em all with this amazing Pokemon sticker collection! Features Pikachu and many popular Pokemon.",
                price=4.99,
                category="Gaming & Online",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="pokemon.webp",
                in_stock=True
            ),
            Product(
                name="Anime Pack",
                description="Popular anime characters and symbols. Perfect for anime enthusiasts and collectors.",
                price=5.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="anime.webp",
                in_stock=True
            ),
            Product(
                name="Star Wars Pack",
                description="May the Force be with you! Classic Star Wars characters and iconic symbols from a galaxy far, far away.",
                price=5.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="starwars.webp",
                in_stock=True
            ),
            Product(
                name="Minions Pack",
                description="Despicably adorable Minions stickers! Perfect for kids and fans of the Despicable Me franchise.",
                price=5.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="minions.webp",
                in_stock=True
            ),
            Product(
                name="Flowers Pack",
                description="Beautiful floral designs perfect for decorating laptops, water bottles, and journals.",
                price=4.99,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Matte",
                image_url="flowers.webp",
                in_stock=True
            ),
            Product(
                name="Among Us Pack",
                description="Sus! Popular Among Us characters in various colours. Perfect for gamers.",
                price=4.49,
                category="Gaming & Online",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="among-us.webp",
                in_stock=True
            ),
            Product(
                name="Animals Pack",
                description="Cute and colourful animal stickers featuring cats, dogs, pandas, and more.",
                price=4.99,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="animals.webp",
                in_stock=True
            ),
            Product(
                name="Marvel Heroes Pack",
                description="Assemble! Featuring your favourite Marvel superheroes including Spider-Man, Iron Man, and Captain America.",
                price=5.99,
                category="Superheroes & Comics",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="marvel.webp",
                in_stock=True
            ),
            Product(
                name="Back to the Future Pack",
                description="Great Scott! Classic Back to the Future themed stickers with the DeLorean and more.",
                price=5.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="BackToTheFuture.webp",
                in_stock=True
            ),
            Product(
                name="Skateboard Pack",
                description="Cool skateboarding-themed stickers perfect for skaters and action sports enthusiasts.",
                price=4.99,
                category="Sports & Activities",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Skate.webp",
                in_stock=True
            ),
            Product(
                name="Brand Logos Pack",
                description="Popular brand logos and symbols. Show your brand loyalty!",
                price=4.99,
                category="Brands & Logos",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Logos.webp",
                in_stock=True
            ),
        ]
        
        # Add all products to the database
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        print(f"Successfully added {len(products)} products to the database!")

if __name__ == '__main__':
    seed_database()
