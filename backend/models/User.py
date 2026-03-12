from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    deleted = db.Column(db.Integer)
    owners = db.Column(ARRAY(db.Integer))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relazioni
    groups = db.relationship('Group', backref='owner', lazy=True)
    documents = db.relationship('Document', backref='user', lazy=True)
    shared_documents_owner = db.relationship('SharedDocument', foreign_keys='SharedDocument.owner_id', backref='owner_user', lazy=True)
    shared_documents_shared_with = db.relationship('SharedDocument', foreign_keys='SharedDocument.shared_with_id', backref='shared_with_user', lazy=True)
    saved_searches = db.relationship('SavedSearch', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)
    action_logs = db.relationship('ActionLog', backref='user', lazy=True)