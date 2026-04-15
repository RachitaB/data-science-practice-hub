# 🐍 Looping Number Checker

## 📌 Problem Statement
Given an integer **n**, determine whether it is a **looping number**.

A number is considered a looping number if:

1. It is repeatedly replaced by the **sum of the squares of its digits**
2. The process continues until either:
   - The number becomes **1**, in which case it is **not** a looping number  
   - The sequence starts repeating in a **cycle that does not include 1**, making it a **looping number**

Return:

- **True** → If `n` is a looping number  
- **False** → Otherwise  

---

## 🧾 Example 1

### Input
```python
n = 4
```

### Output
```python
True
```

### Explanation

```text
4² = 16
1² + 6² = 1 + 36 = 37
3² + 7² = 9 + 49 = 58
5² + 8² = 25 + 64 = 89
8² + 9² = 64 + 81 = 145
1² + 4² + 5² = 1 + 16 + 25 = 42
4² + 2² = 16 + 4 = 20
2² + 0² = 4 + 0 = 4
```

Since the process loops back to **4**, it forms a cycle.

> Therefore, **4 is a looping number**

---

## 🧾 Example 2

### Input
```python
n = 19
```

### Output
```python
False
```

### Explanation

```text
1² + 9² = 1 + 81 = 82
8² + 2² = 64 + 4 = 68
6² + 8² = 36 + 64 = 100
1² + 0² + 0² = 1 + 0 + 0 = 1
```

Since the sequence reaches **1**:

> **19 is NOT a looping number**

---

## 🧠 Approach
- Repeatedly calculate the sum of the squares of digits  
- Track previously seen values  
- If the number reaches **1**, return **False**  
- If a number repeats before reaching **1**, return **True**

---

## 🚀 Key Concepts
- Digit Extraction  
- Mathematical Simulation  
- Cycle Detection  
- Hash Sets / Tracking Visited Values  

---
