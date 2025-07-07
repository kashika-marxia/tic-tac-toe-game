

# 🎮 Tic-Tac-Toe Game with AI (Minimax Algorithm)

This is a command-line Tic-Tac-Toe game built with Python, where the player competes against an unbeatable AI opponent powered by the **Minimax algorithm**.

---

## 🧠 Features

* 3x3 Tic-Tac-Toe board
* Human plays as `X`, AI plays as `O`
* AI uses **Minimax** to make optimal moves
* Detects:

  * Player win
  * AI win
  * Draw
* Input validation for valid moves

---

## 📁 File Structure

```bash
tic_tac_toe_ai.py   # Main game file
README.md           # Project documentation (this file)
```

---

## ▶️ How to Run

1. Ensure Python 3.x is installed.
2. Save the script as `tic_tac_toe_ai.py`.
3. Run the script in your terminal or command prompt:

```bash
python tic_tac_toe_ai.py
```

---

## 🎮 How to Play

* The board has 9 positions labeled from **1 to 9** as shown below:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

* On your turn, enter a number from 1 to 9 corresponding to the position you want to mark with `X`.
* After your move, the AI will respond with the optimal move using Minimax.
* The game ends when either player wins or the board is full (draw).

---

## 🧮 AI Logic: Minimax Algorithm

The AI uses the **Minimax algorithm** to:

* Explore all possible moves
* Evaluate the outcome (win/loss/draw)
* Choose the best move that guarantees the highest chance of winning or forcing a draw

This makes the AI **unbeatable**.

---

## 📌 Example Gameplay

```
Welcome to Tic-Tac-Toe!
 | | 
-----
 | | 
-----
 | | 
Enter your move (1-9): 1
X| | 
-----
 | | 
-----
 | | 
AI is making a move...
X| |O
-----
 | | 
-----
 | | 
...
```

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required (uses only built-in `math` module)

---

## 📚 Concepts Covered

* Game loops
* Board state representation
* Minimax algorithm (recursion + backtracking)
* Input validation
* Simple AI decision-making
  
#📈 check out the coding:

https://drive.google.com/file/d/1c9HGomh01VlCF-r6y-Uxdn24CFCiCvAF/view?usp=drivesdk
---

## ✅ To-Do (Optional Enhancements)

* GUI using Tkinter or Pygame
* Difficulty levels (easy/medium/hard)
* Highlight winning combinations
* Multiplayer mode

---
