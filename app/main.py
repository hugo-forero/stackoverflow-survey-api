from fastapi import FastAPI
from app.core.config import settings
from app.routers import health

app = FastAPI(
    title = settings.app_name,
    summary = "Structured insights from the Stack Overflow Annual Developer Survey: languages, salaries, tools, and trends served as a REST API", 
    description = """
    
    REST API that serves structured insights from the Stack Overflow Developer Survey dataset.
    It queries the most loved languages, salary distributions by role and country, framework adoption trends, and
    year-over-year comparisons.

    Built with: 
    • FastAPI
    • Async SQLAlchemy
    • JWTauth

    And deployed on Render
    """,
    contact={
        "name": "Hugo Forero",
        "url": "https://www.linkedin.com/in/hforero/"

    },
    license_info= {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    version= settings.app_version

)

app.include_router(health.router)
