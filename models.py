from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Member(Base):
   __tablename__ = 'members'
   id = Column(Integer, primary_key=True)
   name = Column(String(255))
   email = Column(String(255))
   phone = Column(String(50))

class Staff(Base):
   __tablename__ = 'staff'
   id = Column(Integer, primary_key=True)
   name = Column(String(255))
   email = Column(String(255))

class Venue(Base):
   __tablename__ = 'venues'
   id = Column(Integer, primary_key=True)
   name = Column(String(255))
   floor = Column(Integer)
   capacity = Column(Integer)

class Event(Base):
   __tablename__ = 'events'
   id = Column(Integer, primary_key=True)
   title = Column(String(50))
   start_time = Column(DateTime)
   end_time = Column(DateTime)
   venue_id = Column(Integer, ForeignKey('venues.id'))
   organizer_id = Column(Integer, ForeignKey('staff.id'))

class Registration(Base):
   __tablename__ = 'registrations'
   id = Column(Integer, primary_key=True)
   member_id = Column(Integer, ForeignKey('members.id'))
   event_id = Column(Integer, ForeignKey('events.id'))
   registered_at = Column(DateTime, default=datetime.now)
