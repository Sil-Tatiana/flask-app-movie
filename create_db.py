from applications import db, app
from applications.models import ShowMovies

def create_database():
    with app.app_context():
        db.create_all()

def delete_database():
    with app.app_context():
        db.drop_all()

def add_entries():
    entry1 = ShowMovies(title="Star-wars", rating="5")
    entry2 = ShowMovies(title="Star-warsII", rating="5")
    entry3 = ShowMovies(title="Harry Potter", rating="3")
    entry4 = ShowMovies(title="Lord of the Rings", rating="4")
    with app.app_context():
        db.session.add(entry1)
        db.session.add(entry2)
        db.session.add(entry3)
        db.session.add(entry4)
        db.session.commit()

def see_db_entries():
    with app.app_context():
        entries = ShowMovies.query.all()
        for entry in entries:
            print(f"{entry.title}, {entry.rating}, {entry.date}")

if __name__ == "__main__":
    delete_database()
    create_database()
    add_entries()
    see_db_entries()