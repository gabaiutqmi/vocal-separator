from fastapi import FastAPI, File, UploadFile
import os
import uuid
from utils.separate import separate_audio

app = FastAPI()

@app.post("/separate")
async def separate(file: UploadFile = File(...)):
    temp_id = str(uuid.uuid4())
    input_path = f"temp/{temp_id}.mp3"
    os.makedirs("temp", exist_ok=True)

    with open(input_path, "wb") as f:
        f.write(await file.read())

    vocals_path, accompaniment_path = separate_audio(input_path)

    return {
        "vocals": vocals_path,
        "instrumental": accompaniment_path
    }
