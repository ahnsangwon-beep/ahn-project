import random

MENUS = {
    "한식": [
        "된장찌개",
        "김치찌개",
        "제육볶음",
        "비빔밥",
        "삼겹살",
        "순두부찌개",
        "갈비탕",
        "불고기",
        "닭볶음탕",
        "해물파전",
    ],
    "양식": [
        "파스타",
        "피자",
        "스테이크",
        "리조또",
        "햄버거",
        "샐러드",
        "크림수프",
        "그라탱",
    ],
    "일식": [
        "초밥",
        "라멘",
        "돈카츠",
        "우동",
        "오야코동",
        "규동",
        "샤브샤브",
        "타코야키",
    ],
    "중식": [
        "짜장면",
        "짬뽕",
        "탕수육",
        "마파두부",
        "볶음밥",
        "딤섬",
        "깐풍기",
    ],
    "분식": [
        "떡볶이",
        "순대",
        "김밥",
        "라면",
        "만두",
        "어묵",
        "튀김",
    ],
}


def recommend_random():
    category = random.choice(list(MENUS.keys()))
    menu = random.choice(MENUS[category])
    return category, menu


def recommend_by_category(category):
    if category not in MENUS:
        return None, None
    menu = random.choice(MENUS[category])
    return category, menu


def show_all_menus():
    for category, items in MENUS.items():
        print(f"\n[{category}]")
        for item in items:
            print(f"  - {item}")


def main():
    print("=" * 40)
    print("      저녁 메뉴 추천 프로그램")
    print("=" * 40)

    while True:
        print("\n무엇을 하시겠습니까?")
        print("1. 랜덤 추천")
        print("2. 카테고리별 추천")
        print("3. 전체 메뉴 보기")
        print("4. 종료")

        choice = input("\n선택 (1-4): ").strip()

        if choice == "1":
            category, menu = recommend_random()
            print(f"\n오늘 저녁은... [{category}] {menu} 어떠세요? 😋")

        elif choice == "2":
            categories = list(MENUS.keys())
            print("\n카테고리를 선택하세요:")
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
            cat_input = input("선택: ").strip()
            if cat_input.isdigit() and 1 <= int(cat_input) <= len(categories):
                selected = categories[int(cat_input) - 1]
                category, menu = recommend_by_category(selected)
                print(f"\n오늘 저녁은... [{category}] {menu} 어떠세요? 😋")
            else:
                print("올바른 번호를 입력해주세요.")

        elif choice == "3":
            print("\n전체 메뉴 목록:")
            show_all_menus()

        elif choice == "4":
            print("\n맛있는 저녁 드세요! 👋")
            break

        else:
            print("1~4 중에서 선택해주세요.")


if __name__ == "__main__":
    main()
