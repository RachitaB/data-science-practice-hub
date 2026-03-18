# 🎲 4 Rolls to 4 (Visa)

## ❓ Problem

A fair die is rolled repeatedly until a number **greater than 4** is observed.

What's the probability that it takes you **4 rolls to roll a number greater than 4**?

---

## 🧠 Key Idea

To take exactly 4 rolls:

* First 3 rolls → number ≤ 4
* 4th roll → number > 4

---

## 📊 Probabilities

* Total outcomes on a die = 6

### Probability of ≤ 4:

= 4 / 6 = 2/3

### Probability of > 4:

= 2 / 6 = 1/3

---

## 📉 Final Calculation

P(≤4 for first 3 rolls AND >4 on 4th roll)

= (2/3)³ × (1/3)
= 8/27 × 1/3
= **8/81**

---

## ✅ Final Answer

**Probability = 8/81 ≈ 0.0988**

---

## 💡 Concept

This is a **Geometric Distribution**:

* First success (number > 4) occurs on the 4th trial
* Formula:
  P(X = k) = (failure)^(k-1) × (success)

Here:

* Failure = 2/3
* Success = 1/3
* k = 4

---
