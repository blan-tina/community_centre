from main import Session
from models import Member, Staff, Venue, Event, Registration
from faker import Faker
from random import randint, choice
from datetime import timedelta

session = Session()
fake = Faker()

# Clear old data
session.query(Registration).delete()
session.query(Event).delete()
session.query(Member).delete()
session.query(Staff).delete()
session.query(Venue).delete()
session.commit()

# Create staff
staff_list = []
for i in range(5):
    staff = Staff(
        name=fake.name(),
        email=fake.email()
    )
    staff_list.append(staff)

session.add_all(staff_list)
session.commit()

# Create venues
venue_list = []
for i in range(5):
    venue = Venue(
        name=f"Room {i+1}",
        floor=i+1,
        capacity=randint(20, 100)
    )
    venue_list.append(venue)

session.add_all(venue_list)
session.commit()

# Create members
member_list = []
for i in range(10):
    member = Member(
        name=fake.name(),
        email=fake.email(),
        phone=str(randint(700000000, 799999999))
    )
    member_list.append(member)

session.add_all(member_list)
session.commit()

# Create events
event_list = []
for i in range(8):
    start = fake.date_time_between(start_date="now", end_date="+30d")
    event = Event(
        title=fake.catch_phrase(),
        start_time=start,
        end_time=start + timedelta(hours=2),
        venue_id=choice(venue_list).id,
        organizer_id=choice(staff_list).id
    )
    event_list.append(event)

session.add_all(event_list)
session.commit()

# Create registrations
registration_list = []
for i in range(15):
    registration = Registration(
        member_id=choice(member_list).id,
        event_id=choice(event_list).id,
        registered_at=fake.date_time_between(start_date="-10d", end_date="now")
    )
    registration_list.append(registration)

session.add_all(registration_list)
session.commit()

print("Done!")

# QUERY SECTION
print("\n=== MEMBERS ===")
for m in session.query(Member).all():
    print(m.id, m.name, m.email, m.phone)

print("\n=== STAFF ===")
for s in session.query(Staff).all():
    print(s.id, s.name, s.email)

print("\n=== VENUES ===")
for v in session.query(Venue).all():
    print(v.id, v.name, v.floor, v.capacity)

print("\n=== EVENTS ===")
for e in session.query(Event).all():
    print(e.id, e.title, e.venue_id, e.organizer_id)

print("\n=== REGISTRATIONS ===")
for r in session.query(Registration).all():
    print(r.id, r.member_id, r.event_id, r.registered_at)

session.close() 