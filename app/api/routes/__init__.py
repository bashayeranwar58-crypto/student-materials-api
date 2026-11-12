from app.api.routes.students import router as students_router
from app.api.routes.subjects import router as subjects_router
from app.api.routes.materials import router as materials_router

__all__ = ["students_router", "subjects_router", "materials_router"]