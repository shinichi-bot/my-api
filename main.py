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
    "推進者": [
        {"name": "MotionBoard 業務改善事例集", "url": "https://www.wingarc.com/product/motionboard/"},
        {"name": "KPI管理ダッシュボードの作り方", "url": "https://www.wingarc.com/product/motionboard/"},
        {"name": "経営レポート自動化ガイド", "url": "https://www.wingarc.com/product/motionboard/"},
    ],
    "構築者": [
        {"name": "MotionBoard 開発者向けガイド", "url": "https://www.wingarc.com/product/motionboard/"},
        {"name": "チャート・グラフの作成方法", "url": "https://www.wingarc.com/product/motionboard/"},
        {"name": "データソース接続マニュアル", "url": "https://www.wingarc.com/product/motionboard/"},
    ],
    "利用者": [
        {"name": "MotionBoard 基本操作ガイド", "url": "https://www.wingarc.com/product/motionboard/"},
        {"name": "ダッシュボードの見方・使い方", "url": "https://www.wingarc.com/product/motionboard/"},
        {"name": "レポート出力・共有の方法", "url": "https://www.wingarc.com/product/motionboard/"},
    ],
}

@app.get("/api")
def get_contents(usertype: str):
    if usertype not in CONTENTS:
        return {"error": "Invalid usertype"}
    return {"contents": CONTENTS[usertype]}