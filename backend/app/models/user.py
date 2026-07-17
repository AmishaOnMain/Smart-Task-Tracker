from datetime import datetime 

from sqlalchemy import Boolean, DateTime, Integer, String 

from sqlalchemy.orm import Mapped, mapped_column 

from app.database.base import Base 

class User(Base): 

  __tablename__ = "users"

  id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

  google_id: Mapped[str] = mapped_column(

    String,
    unique= True,
    nullable= False,

  )

  name: Mapped[str] = mapped_column(

    String,
    nullable= False,

  )

  email: Mapped[str] = mapped_column(

    String,
    unique= True,
    nullable= False,

  )

  profile_picture: Mapped[str | None] = mapped_column(

    String,
    nullable= True,

  )

  created_at: Mapped[datetime]= mapped_column(

    DateTime,
    default= datetime.utcnow,

  )

  is_active: Mapped[bool]=mapped_column(

    Boolean,
    default= True,
    
  )