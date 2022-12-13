from sqlalchemy import Column, DateTime, Boolean,String
from datetime import datetime
import getpass

class Common():

    is_delete = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.utcnow)
    updated_at = Column(DateTime, default = datetime.utcnow)
    created_by=Column(String, default = getpass.getuser())
    updated_by=Column(String, default = getpass.getuser())
