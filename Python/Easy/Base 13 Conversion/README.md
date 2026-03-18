# 🔢 Base 13 Conversion (Capital One)

## ❓ Problem

Given an integer `num`, return its string representation in **base 13**.

In base 13:

* Digits go from **0–9**
* Then:

  * 10 → A
  * 11 → B
  * 12 → C

---

## 📌 Examples

| Decimal | Base 13 |
| ------- | ------- |
| 9       | "9"     |
| 10      | "A"     |
| 11      | "B"     |
| 12      | "C"     |
| 13      | "10"    |
| 14      | "11"    |
| 49      | "3A"    |
| 69      | "54"    |

---

## 🧠 Approach

* Use **repeated division by 13**
* Store remainders
* Map:

  * 10 → A
  * 11 → B
  * 12 → C
* Reverse the result at the end

---

## ⏱️ Complexity

* Time: **O(log₁₃ n)**
* Space: **O(log₁₃ n)**

---
