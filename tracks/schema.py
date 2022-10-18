from datetime import datetime

from ninja import ModelSchema, Schema

from tracks.models import Track


class TrackSchema(ModelSchema):
    class Config:
        model = Track
        model_fields = ["title", "artist", "duration", "last_play"]


class NotFoundSchema(Schema):
    message: str
