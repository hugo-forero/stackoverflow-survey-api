from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column

from sqlalchemy import String, Numeric
from sqlalchemy import Enum as SAEnum
from sqlalchemy import JSON

from app.db.enums import RemoteWork, NewRole

from decimal import Decimal

class Base(DeclarativeBase):
    pass

class Respondent(Base):
    __tablename__ = "respondents"

    id: Mapped[int] = mapped_column(primary_key=True)
    remote_work: Mapped[RemoteWork | None] = mapped_column(SAEnum(RemoteWork), nullable = True)
    new_role: Mapped[NewRole | None] = mapped_column(SAEnum(NewRole), nullable = True)
    country: Mapped [str | None] = mapped_column(String(255), nullable= True)
    industry: Mapped [str | None] = mapped_column(String(255), nullable = True)
    currency: Mapped [str | None] = mapped_column(String(255), nullable = True)
    comp_total: Mapped [Decimal | None] = mapped_column(Numeric(18,2), nullable = True)
    lang_have_worked_with: Mapped [list | None] = mapped_column (JSON, nullable = True)
    db_have_worked_with: Mapped [list | None] = mapped_column (JSON, nullable = True)
    plat_have_worked_with: Mapped [list | None] = mapped_column (JSON, nullable = True)
    webfr_have_worked_with: Mapped [list | None] = mapped_column (JSON, nullable = True)

