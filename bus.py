from flask import Flask, request
import requests
import xml.etree.ElementTree as ET
import random

app = Flask(__name__)

BUS_KEY   = "5b1b7bc26db1b880e34dfb394514d6452f67f3371b7b5c99cee3990cf3722f65"
TEL_TOKEN = "8672017761:AAGNOCUxv9i72_BcdJgNMwhtbvd15miJqTQ"
CHAT_ID   = "7941177235"
AUTH_PASS = "hobbang77"
ARS_ID    = "20131"
TARGET_BUS = "360"

DINNER_MENUS = {
    "한식": ["김치찌개", "된장찌개", "불고기", "삼겹살", "비빔밥", "순두부찌개", "갈비탕", "제육볶음"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "깐풍기", "볶음밥"],
    "일식": ["초밥", "라멘", "우동", "돈카츠", "규동", "오야코동"],
    "양식": ["파스타", "스테이크", "피자", "리조또", "햄버거", "샐러드"],
    "분식": ["떡볶이", "순대", "튀김", "김밥", "라면", "치즈볶이"],
}

@app.route("/dinner")
def dinner():
    if request.args.get("key") != AUTH_PASS:
        return "인증 실패", 401

    category = random.choice(list(DINNER_MENUS.keys()))
    menu = random.choice(DINNER_MENUS[category])
    msg = f"🍽️ 오늘 저녁 추천 메뉴\n[{category}] {menu} 어떠세요? 😋"

    requests.post(f"https://api.telegram.org/bot{TEL_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg}, timeout=5)
    return msg.replace("\n", "<br>"), 200

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    text = message.get("text", "").strip()
    chat_id = message.get("chat", {}).get("id")

    if not chat_id:
        return "ok", 200

    if text == "/dinner":
        category = random.choice(list(DINNER_MENUS.keys()))
        menu = random.choice(DINNER_MENUS[category])
        msg = f"🍽️ 오늘 저녁 추천 메뉴\n[{category}] {menu} 어떠세요? 😋"
        requests.post(f"https://api.telegram.org/bot{TEL_TOKEN}/sendMessage",
                      data={"chat_id": chat_id, "text": msg}, timeout=5)

    return "ok", 200

@app.route("/bus")
def get_bus():
    if request.args.get("key") != AUTH_PASS:
        return "인증 실패", 401

    res = requests.get(
        "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid",
        params={"ServiceKey": BUS_KEY, "arsId": ARS_ID},
        timeout=10
    )
    res.encoding = "utf-8"

    root = ET.fromstring(res.text)
    items = [{c.tag: c.text for c in item} for item in root.iter("itemList")]
    target = [i for i in items if i.get("rtNm", "").strip() == TARGET_BUS]

    if not target:
        all_buses = ", ".join(i.get("rtNm", "?") for i in items)
        msg = f"🚌 {TARGET_BUS}번 없음 (현재 정류소: {all_buses or '없음'})"
    else:
        i = target[0]
        msg = (f"🚌 {TARGET_BUS}번 버스\n"
               f"⏱️ {i.get('arrmsg1', '정보없음')}\n"
               f"⏱️ {i.get('arrmsg2', '정보없음')}\n"
               f"📍 방향: {i.get('adirection', '?')}")

    requests.post(f"https://api.telegram.org/bot{TEL_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg}, timeout=5)
    return msg.replace("\n", "<br>"), 200

def register_webhook():
    url = f"https://api.telegram.org/bot{TEL_TOKEN}/setWebhook"
    res = requests.post(url, data={"url": "https://ahnssang.cloud/telegram"}, timeout=10)
    print(f"Webhook 등록: {res.json()}")

if __name__ == "__main__":
    register_webhook()
    app.run(host="0.0.0.0", port=5000)