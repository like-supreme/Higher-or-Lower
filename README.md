# Higher-or-Lower
A simple Python-based Higher-Lower game. Compare Instagram follower counts and guess who's more popular. Built with beginner-friendly logic using dictionaries and loops

# 🔼 Higher Lower Game (Python)

This is a simple terminal-based Python game inspired by the "Higher Lower" format.

You are shown two random celebrities or brands, and your task is to guess which one has **more followers** on Instagram.

---

## 📁 Project Structure

higher_lower/
│
├── art.py # ASCII art (logo, vs symbol)
├── game_data.py # Data list of dictionaries (names, followers, etc.)
├── main.py # Main game logic (import, compare, scoring, loop)
└── pycache/ # Auto-generated Python cache


---

## ▶️ How to Play

1. Run `main.py`  
2. Two random entries will be shown (e.g., Ronaldo vs Instagram)
3. You guess who has more followers: `'a'` or `'b'`
4. If correct → your score increases and the game continues  
   If wrong → game ends and your final score is shown

---

## 🧠 Concepts Used

- `random.choice()`
- Dictionaries
- Functions and parameters
- Loops (`while`)
- Conditional statements (`if-else`)
- Input handling
- ASCII art display

---

## ✅ Example

```bash
a: Cristiano Ronaldo from Portugal, a Footballer
vs
b: Instagram from United States, a Social Media Platform

Make a Guess a or b: a

You lose
Your final score is: 0

 Future Improvements
Track highest score

Add UI with tkinter or web version

Store past scores or leaderboard

Add more diverse data
