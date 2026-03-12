from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid

db = SQLAlchemy()

class Document(db.Model):
    __tablename__ = 'documents'

    document_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    id_document_repo = db.Column(db.Integer, nullable=True)
    # Relazioni
    shared_documents = db.relationship('SharedDocument', backref='document', lazy=True)

class SharedDocument(db.Model):
    __tablename__ = 'shared_documents'

    share_id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.String, db.ForeignKey('documents.document_id', ondelete='CASCADE'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    shared_with_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    shared_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('document_id', 'shared_with_id', name='unique_shared_document'),
    )