# 🐍 Maximum Average Subarray of Size K

## 📌 Problem Statement
You are given:

- An integer array **nums** of size **n**
- An integer **k**

Your task is to:

> Find a **contiguous subarray of length k** that has the **maximum average value**

Return the average **rounded to 2 decimal places**.

---

## 📝 Definition
- A **subarray** is a sequence of **consecutive elements**
- Length of subarray must be **exactly k**

---

## 🧾 Example 1

### Input
```python
nums = [1, 2, -5, -3, 10, 3]
k = 3

## ✅ Output
```python
3.33
```

---

## 💡 Explanation

### Best Subarray
```python
[-3, 10, 3]
```

```text
(-3 + 10 + 3) / 3 = 10 / 3 = 3.33
```

---

## 🧾 Example 2

### Input
```python
nums = [9]
k = 1
```

### Output
```python
9.00
```

### Explanation

```python
[9]
```

```text
9 / 1 = 9.00
```

---

## 🧠 Approach
- Use **sliding window technique**
- Maintain a window of size **k**
- Compute sum of first window
- Slide the window:
  - Add next element  
  - Remove previous element  
- Track **maximum sum**
- Divide by **k** to get maximum average

---

## 🚀 Key Concepts
- Sliding Window  
- Subarrays  
- Running Sum  
- Optimization  
- Averaging  

---
