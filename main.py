from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CONTENTS = {
    "A": ["contents_1", "contents_2", "contents_3"],
    "B": ["contents_4", "contents_5", "contents_6"],
}

@app.get("/api")
def get_contents(usertype: str):
    if usertype not in CONTENTS:
        return {"error": "Invalid usertype"}
    return {"contents": CONTENTS[usertype]}
