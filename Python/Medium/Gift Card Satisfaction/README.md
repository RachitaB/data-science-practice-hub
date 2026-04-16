# 🐍 Maximum Teammates Satisfied with Gift Cards

## 📌 Problem Statement
You are given:

- An array **Expectations**, where each value represents the **minimum gift card value** a teammate expects  
- An array **Cards**, where each value represents the **value of an available gift card**

### Rules
- Each teammate can receive **at most one** gift card  
- Each gift card can be assigned to **only one** teammate  
- A gift card must be **greater than or equal to** a teammate’s expectation to satisfy them  

Return the **maximum number of teammates** that can be satisfied.

---

## 🧾 Example 1

### Input
```python
Expectations = [5, 20, 1000]
Cards = [10, 15, 100]
```

### Output
```python
2
```

### Explanation
- Expectation **5** → satisfied with **10**
- Expectation **20** → satisfied with **100**
- Expectation **1000** → cannot be satisfied  

> Maximum teammates satisfied = **2**

---

## 🧾 Example 2

### Input
```python
Expectations = [10, 30, 100, 200]
Cards = [5, 2, 5, 3, 9]
```

### Output
```python
0
```

### Explanation
No available gift card meets the minimum expectation of any teammate.

> Maximum teammates satisfied = **0**

---

## 🧠 Approach
- Sort both **Expectations** and **Cards**
- Use two pointers:
  - One for teammates  
  - One for gift cards  
- Try to assign the smallest possible card that satisfies current expectation  
- Move pointers accordingly and count satisfied teammates  

---

## 🚀 Python Solution

```python
def max_satisfied(expectations, cards):
    expectations.sort()
    cards.sort()

    i = 0
    j = 0
    satisfied = 0

    while i < len(expectations) and j < len(cards):
        if cards[j] >= expectations[i]:
            satisfied += 1
            i += 1
            j += 1
        else:
            j += 1

    return satisfied
```

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(n log n + m log m) |
| Space Complexity | O(1) |

Where:
- **n** = number of teammates  
- **m** = number of gift cards  

---

## 🚀 Key Concepts
- Greedy Algorithm  
- Sorting  
- Two Pointers  
- Optimization Problems  

---
