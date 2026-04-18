# 🐍 Minimum Amplitude After At Most 3 Changes

## 📌 Problem Statement
Given an integer array **arr**, the **amplitude** is defined as:

> **max(arr) - min(arr)**

You are allowed to **change up to 3 elements** in the array to **any value**.

Return the **minimum possible amplitude** after performing at most 3 changes.

---

## 🧾 Example 1

### Input
```python
arr = [4, -8, -1, 3, 7, 10, 5]
## 🧾 Example 1

### Output
```python
4
```

### Explanation
We can modify:
- **-8 → 3**
- **-1 → 3**
- **10 → 7**

Resulting array:

```python
[4, 3, 3, 3, 7, 7, 5]
```

- Min = **3**  
- Max = **7**

> **Amplitude = 7 - 3 = 4**

---

## 🧾 Example 2

### Input
```python
arr = [3, 5, 10, 0]
```

### Output
```python
0
```

### Explanation
We can change:
- **3, 5, 10 → 0**

Resulting array:

```python
[0, 0, 0, 0]
```

- Min = **0**  
- Max = **0**

> **Amplitude = 0**

---

## 🧠 Approach
- Sort the array  
- Since you can change up to **3 elements**, you can effectively:
  - Remove up to **3 largest values**  
  - Remove up to **3 smallest values**  
  - Or a combination of both  

### Cases to Check
- Remove **3 smallest**
- Remove **2 smallest + 1 largest**
- Remove **1 smallest + 2 largest**
- Remove **3 largest**

> Choose the **minimum difference** among all cases.

---

## 🚀 Key Concepts
- Sorting  
- Greedy Optimization  
- Sliding Window Insight  
- Edge Case Handling  

---
