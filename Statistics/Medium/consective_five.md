# 🎲Consecutive Fives (Akuna Capital)

## ❓ Problem

A fair six-sided die is rolled repeatedly.

What is the **expected number of rolls** until you get **two consecutive 5s**?

---

## 🧠 Key Idea

We model this using **states**:

* **State A:** No previous 5
* **State B:** Last roll was a 5
* **Goal:** Two consecutive 5s

---

## 📊 Step-by-Step

Let:

* E₀ = expected rolls from State A
* E₁ = expected rolls from State B

---

### 🔹 From State A (no previous 5)

* Roll a 5 (prob = 1/6) → move to State B
* Roll anything else (prob = 5/6) → stay in State A

E₀ = 1 + (1/6)E₁ + (5/6)E₀

---

### 🔹 From State B (one 5 already)

* Roll a 5 (prob = 1/6) → done ✅
* Roll anything else (prob = 5/6) → back to State A

E₁ = 1 + (5/6)E₀

---

## 📉 Solve Equations

From first equation:

E₀ - (5/6)E₀ = 1 + (1/6)E₁
(1/6)E₀ = 1 + (1/6)E₁

E₀ = 6 + E₁

Substitute into second:

E₁ = 1 + (5/6)(6 + E₁)
E₁ = 1 + 5 + (5/6)E₁
E₁ = 6 + (5/6)E₁

(1/6)E₁ = 6
E₁ = 36

Now:

E₀ = 6 + 36 = **42**

---

## ✅ Final Answer

**Expected number of rolls = 42**

---

## 💡 Insight

* This is a classic **Markov / expectation recursion problem**
* You cannot just multiply averages — you must account for **reset behavior**
* Consecutive events → always think in **states**

---
