from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid

db = SQLAlchemy()

class SavedSearch(db.Model):
    __tablename__ = 'saved_searches'

    search_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    query = db.Column(db.Text, nullable=False)
    search_date = db.Column(db.DateTime, default=datetime.utcnow)