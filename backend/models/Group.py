from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid

db = SQLAlchemy()

class Group(db.Model):
    __tablename__ = 'groups'

    group_id = db.Column(db.Integer, primary_key=True)
    group_owner = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    group_name = db.Column(db.String(100), nullable=False)

    # Relazioni
    users = db.relationship('User', secondary='user_groups', back_populates='groups')

class UserGroup(db.Model):
    __tablename__ = 'user_groups'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id', ondelete='CASCADE'), primary_key=True)