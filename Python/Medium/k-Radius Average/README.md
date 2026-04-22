# 🐍 K-Radius Subarray Averages

## 📌 Problem Statement
You are given:

- An integer array **nums** of length **n**
- An integer **k**

For each index **i**, compute the **k-radius average**, defined as:

> The average of elements from index **i - k to i + k (inclusive)**

### Rules
- If there are not enough elements on either side → return **-1**
- Return all values rounded to **2 decimal places**

---

## 🧾 Example

### Input
```python
nums = [7, 2, 5, 12, 9, 4, 1]
k = 2

## ✅ Output

```python
[-1, -1, 7.0, 6.4, 6.2, -1, -1]
```

---

## 💡 Explanation

### ❌ Invalid Indices
For indices:
- **i = 0, 1, 5, 6**

Not enough elements exist on either side → **-1**

---

### ✅ Valid Calculations

#### 📍 i = 2  
Subarray: `nums[0] → nums[4]`

```text
(7 + 2 + 5 + 12 + 9) / 5 = 35 / 5 = 7.0
```

---

#### 📍 i = 3  
Subarray: `nums[1] → nums[5]`

```text
(2 + 5 + 12 + 9 + 4) / 5 = 32 / 5 = 6.4
```

---

#### 📍 i = 4  
Subarray: `nums[2] → nums[6]`

```text
(5 + 12 + 9 + 4 + 1) / 5 = 31 / 5 = 6.2
```

---

## 🧠 Approach
- Window size = **2k + 1**
- For each valid index:
  - Compute average of window `[i - k → i + k]`
- For invalid indices:
  - Assign **-1**
- Use **sliding window / prefix sum** for optimization

---

## 🚀 Key Concepts
- Sliding Window  
- Prefix Sum  
- Array Traversal  
- Boundary Conditions  
- Averaging  

---
