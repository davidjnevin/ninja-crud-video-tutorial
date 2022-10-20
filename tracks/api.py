from typing import List, Optional

from ninja import File, Router, UploadedFile

from tracks.models import Track
from tracks.schema import NotFoundSchema, TrackSchema

router = Router()


@router.get("/success", url_name="success")
def success_message(request):
    return {"message": "success!"}


@router.get("/tracks", response=List[TrackSchema])
def tracks(request, title: Optional[str] = None):
    "Adding an argument to the funciton allows for query parameters."
    if title:
        return Track.objects.filter(title__icontains=title)
    else:
        return Track.objects.all()


@router.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}


@router.post("/tracks", response={201: TrackSchema})
def create_track(request, track: TrackSchema):
    track = Track.objects.create(**track.dict())
    return track


@router.put("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def change_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(pk=track_id)
        for attribute, value in data.dict().items():
            setattr(track, attribute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist."}


@router.delete("/tracks/{track_id}", response={200: None, 404: NotFoundSchema})
def delete_track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        track.delete()
        return 200
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist."}


@router.post("/upload", url_name="upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read().decode()
    return {"name": file.name, "data": data}
