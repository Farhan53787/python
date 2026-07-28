
def run_gk_quiz():

    question = "Which planet in our solar system has the most moons?\n"
    
    options = [
        "A) Jupiter",
        "B) Saturn",
        "C) Neptune",
        "D) Uranus"
    ]
    
    print(question)
    for option in options:
        print(option)
        
    print("\n---------------------------------")
    user_choice = input("Enter your answer (A, B, C, or D): ").strip().upper()
    print("---------------------------------")
    
    if user_choice == "B":
        print(" 🎉 Correct! Saturn has 146 officially recognized moons.\n")
    elif user_choice in ["A", "C", "D"]:
        print(" ❌ Incorrect. The correct answer is B (Saturn has 146 moons, while Jupiter has 95).\n")
    else:
        print(" ⚠️ Invalid input! Please restart and enter A, B, C, or D.\n")

if __name__ == "__main__":
    run_gk_quiz()


def run2_gk_quiz():
    question = "Which gas is the most abundant in Earth's atmosphere?\n"
    options = [
        "A) Oxygen",
        "B) Nitrogen",
        "C) Carbon Dioxide",
        "D) Hydrogen"
    ]
    
    print(question)
    for option in options:
        print(option)
        
    print("\n---------------------------------")
    user_choice = input("Enter your answer (A, B, C, or D): ").strip().upper()
    print("---------------------------------")
    
    if user_choice == "B":
        print(" 🎉 Correct! Nitrogen makes up about 78% of Earth's atmosphere.\n")
    elif user_choice in ["A", "C", "D"]:
        print(" ❌ Incorrect. The correct answer is B (Nitrogen is 78%, while Oxygen is only 21%).\n")
    else:
        print(" ⚠️ Invalid input! Please restart and enter A, B, C, or D.\n")

if __name__ == "__main__" and run_gk_quiz:
    run2_gk_quiz()

def run3_gk_quiz():
    question = "Which planet in our solar system is known as the Red Planet?"
    options = ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"]
    print(question)
    for option in options:
        print(option)
    print("\n---------------------------------")
    user_choice = input("Enter your answer (A, B, C, or D): ").strip().upper()
    print("---------------------------------")
    
    if user_choice == "C":
        print("🎉 Correct! Mars is called the Red Planet because of iron oxide (rust) on its surface.\n")
    elif user_choice in ["A", "B", "D"]:
        print("❌ Incorrect. The correct answer is C (Mars).\n")
    else:
        print("⚠️ Invalid input! Please restart and enter A, B, C, or D.\n")

if __name__ == "__main__" and run2_gk_quiz:
    run3_gk_quiz()