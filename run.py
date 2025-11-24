#!/usr/bin/env python3
"""
Run script for Mr Stickerman Flask application
"""
from mrstickerman import create_app, db

app = create_app()

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
