# 🐍 Triangular Sum of an Array

## 📌 Problem Statement
You are given an integer array **nums**, where each element is a **single digit (0–9)**.

The **triangular sum** of the array is obtained by repeatedly:

1. Replacing the array with a new array where each element is:

> **(nums[i] + nums[i+1]) % 10**

2. Continuing until only **one element remains**

Return that final remaining value.

---

## 📝 Process Rules
Given an array of length **n**:

- If **n = 1**, stop and return the only element  
- Otherwise:
  - Create a new array of length **n - 1**
  - Each new element is calculated as:

> **(nums[i] + nums[i+1]) % 10**

- Replace original array with new array  
- Repeat until one element remains  

---

## 🧾 Example 1

### Input

```python
nums = [1, 3, 5, 7]
