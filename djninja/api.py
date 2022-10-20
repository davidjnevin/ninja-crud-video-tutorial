from ninja import NinjaAPI

from tracks.api import router as tracks_router

api = NinjaAPI(urls_namespace="tracks_api")

api.add_router("/tracks/", tracks_router)
