import uuid
import enum

from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from .database import Base

class LanguageEnum(enum.Enum):
    english = 'English'
    german = 'German'

class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default='False')
    role = Column(String, server_default='user', nullable=False)
    courses = relationship("Course")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))

class Course(Base):
    __tablename__ = 'course'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    identifier = Column(String, nullable=True, unique=True)
    language = Column(Enum(LanguageEnum), nullable=True)
    description = Column(Text, nullable=True)
    photo = Column(String, nullable=True)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('course.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    childrens = relationship("Course")
    components = relationship("Component")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))

class Component(Base):
    __tablename__ = 'component'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    element = Column(String, nullable=False)
    page_id = Column(UUID(as_uuid=True), ForeignKey('course.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
