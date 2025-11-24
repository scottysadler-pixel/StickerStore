"""
Mr Stickerman Flask Application Launcher

This script initialises and runs the Flask web application for Mr Stickerman sticker store.
It creates the database tables if they don't exist and starts the development server.

Usage:
    python run.py

The application will be available at http://localhost:5000
"""

from mrstickerman import create_app, db

# Create the Flask application instance
app = create_app()

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    # Run the application in debug mode
    # Debug mode provides helpful error messages and auto-reloads on code changes
    print("Starting Mr Stickerman application...")
    print("Visit http://localhost:5000 in your browser")
    print("To seed the database, visit http://localhost:5000/admin/dbseed")
    app.run(debug=True)
