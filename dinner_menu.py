import random

menus = {
    "한식": ["김치찌개", "된장찌개", "불고기", "삼겹살", "비빔밥", "순두부찌개", "갈비탕", "제육볶음"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "깐풍기", "볶음밥"],
    "일식": ["초밥", "라멘", "우동", "돈카츠", "규동", "오야코동"],
    "양식": ["파스타", "스테이크", "피자", "리조또", "햄버거", "샐러드"],
    "분식": ["떡볶이", "순대", "튀김", "김밥", "라면", "치즈볶이"],
}

def recommend_random():
    category = random.choice(list(menus.keys()))
    menu = random.choice(menus[category])
    print(f"\n오늘 저녁 추천 메뉴: [{category}] {menu} 어떠세요? 😋")

def recommend_by_category():
    print("\n카테고리를 선택하세요:")
    categories = list(menus.keys())
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    try:
        choice = int(input("번호 입력: "))
        if 1 <= choice <= len(categories):
            category = categories[choice - 1]
            menu = random.choice(menus[category])
            print(f"\n추천 메뉴: [{category}] {menu} 어떠세요? 😋")
        else:
            print("올바른 번호를 입력해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")

def show_all():
    print("\n===== 전체 메뉴 목록 =====")
    for category, items in menus.items():
        print(f"\n[{category}]")
        for item in items:
            print(f"  - {item}")

def main():
    print("=" * 35)
    print("   오늘 저녁 뭐 먹지? 🍽️")
    print("=" * 35)

    while True:
        print("\n1. 랜덤 추천")
        print("2. 카테고리별 추천")
        print("3. 전체 메뉴 보기")
        print("4. 종료")
        choice = input("\n선택: ").strip()

        if choice == "1":
            recommend_random()
        elif choice == "2":
            recommend_by_category()
        elif choice == "3":
            show_all()
        elif choice == "4":
            print("\n맛있는 저녁 드세요! 👋")
            break
        else:
            print("1~4 중에서 선택해주세요.")

if __name__ == "__main__":
    main()
