# 🐍 Factorial of a Number

## 📌 Problem Statement
Given a non-negative integer **n**, write a formula/program that returns **n! (n factorial)**.

---

## 📝 Definition
The factorial of a number is calculated as:

> **n! = n × (n - 1) × (n - 2) × ... × 2 × 1**

---

## 💡 Formula Explanation

Examples:

- **5! = 5 × 4 × 3 × 2 × 1 = 120**
- **4! = 4 × 3 × 2 × 1 = 24**
- **3! = 3 × 2 × 1 = 6**

Special Case:

- **0! = 1**

---

## 🧾 Example Input / Output

| Input | Output |
|-------|--------|
| 5     | 120    |
| 4     | 24     |
| 0     | 1      |

---

## 🧠 Approach
- Start with result = 1  
- Multiply result by every number from **1 to n**  
- Return final result  

---

## 🚀 Python Solution

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
