from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker , AsyncSession

from app.core.config import settings

from typing import AsyncGenerator

# The engine is defined so it uses the url in the config.py and therefore, the one in the .env. The echo is for logging and 
# it's wired to the development .env variable so it only shows when in development.

engine = create_async_engine(settings.database_url, echo=settings.environment == "development") 



# Creates an instance of the async_session maker, to create a session. It says expire_on_commit = False because that way it preserves
# the cached changes when using an async function.

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# the -> AsyncGenerator[AsyncSession, None] is more a tag that shows what the function get_db() will yield
# in this case, it will yield an AsyncSession, the none is because nothing goes back to the function after yielding.
# the async tag indicates it's an async function.

async def get_db() -> AsyncGenerator[AsyncSession, None]:

# The async with, helps by not only creating the session, but with the cleaning, by ensuring that the session
# is closed, no matter what, even if it brokes. It is similar to manually doing a try and a finally.
    async with AsyncSessionLocal() as session:
        yield session
