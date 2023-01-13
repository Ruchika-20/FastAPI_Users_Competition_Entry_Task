from sqlalchemy import Column, DateTime, Boolean, String
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
import getpass


def commonfunc():
    return datetime.utcnow


class Common:
    """A common class for common functions"""

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    is_delete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=commonfunc())
    updated_at = Column(DateTime, default=commonfunc())
    created_by = Column(String, default=getpass.getuser())
    updated_by = Column(String, default=getpass.getuser())
