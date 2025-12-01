#!/usr/bin/env python3
"""
Run the Flask app
"""
from mrstickerman import create_app, db

app = create_app()

# create db tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    import os
    # enable debug mode if set in environment
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
