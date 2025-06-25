from .handler import router as main_router
from .start import router as start_router
from .book_handler import router as book_router
from .category_handler import router as category_router

all_routers = [
    main_router,
    start_router,
    book_router,
    category_router,
]