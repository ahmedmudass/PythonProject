print("----- Cricket Quiz -----")
print("Answer the questions by typing A, B, C, or D\n")

questions = [
    {
        "question": "1. Who has scored the most runs in ODI cricket?",
        "options": ["A. Sachin Tendulkar", "B. Virat Kohli", "C. Ricky Ponting", "D. Kumar Sangakkara"],
        "answer": "A"
    },
    {
        "question": "2. Which team won the 2023 Cricket World Cup?",
        "options": ["A. India", "B. England", "C. Australia", "D. New Zealand"],
        "answer": "C"
    },
    {
        "question": "3. Who holds the record for the most centuries in T20 Internationals?",
        "options": ["A. Chris Gayle", "B. Rohit Sharma", "C. Babar Azam", "D. David Warner"],
        "answer": "B"
    },
    {
        "question": "4. When did Pakistan win their first Cricket World Cup?",
        "options": ["A. 1983", "B. 1987", "C. 1992", "D. 1996"],
        "answer": "C"
    },
    {
        "question": "5. Who scored the fastest fifty in T20 International cricket?",
        "options": ["A. Yuvraj Singh", "B. Chris Gayle", "C. Babar Azam", "D. Martin Guptill"],
        "answer": "A"
    },
    {
        "question": "6. In which country did cricket originate?",
        "options": ["A. India", "B. Australia", "C. England", "D. South Africa"],
        "answer": "C"
    },
    {
        "question": "7. Who has taken the most wickets in Test cricket?",
        "options": ["A. Shane Warne", "B. Muttiah Muralitharan", "C. James Anderson", "D. Glenn McGrath"],
        "answer": "B"
    },
    {
        "question": "8. Who won the first T20 World Cup?",
        "options": ["A. India", "B. Pakistan", "C. Sri Lanka", "D. West Indies"],
        "answer": "A"
    },
    {
        "question": "9. Who is the highest run-scorer for Pakistan in international cricket?",
        "options": ["A. Inzamam-ul-Haq", "B. Younis Khan", "C. Babar Azam", "D. Mohammad Yousuf"],
        "answer": "A"
    },
    {
        "question": "10. Which player hit six sixes in an over?",
        "options": ["A. Yuvraj Singh", "B. Shahid Afridi", "C. Garry Sobers", "D. Both A and C"],
        "answer": "D"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer: ").strip().upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {q['answer']}")

print("\n----- Quiz Completed -----")
print(f"Your Score: {score} / {len(questions)}")
if score == len(questions):
    print("Excellent! You are a cricket expert.")
elif score >= 5:
    print("Good job! But there’s room for improvement.")
else:
    print("Keep learning! Brush up on your cricket knowledge.")