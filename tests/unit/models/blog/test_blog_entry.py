from demo_app.blog.models import Entry

def test_entry_has_categories(app, session, create_entries):
    entry1 = Entry.query.filter_by(title='Hello World').first()
    assert len(entry1.en_ca) > 0

def test_entry_can_refresh_categories(app, session):
    entry1 = Entry.query.filter_by(title='Hello World').first()
    entry1.refresh_categories()
    assert len(entry1.en_ca) == 0
