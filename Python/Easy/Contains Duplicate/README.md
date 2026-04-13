# 🐍 Check for Duplicate Elements in a List

## 📌 Problem Statement
Given a list of integers called **input**, return **True** if any value appears **at least twice** in the array.

Return **False** if every element in the list is **distinct**.

---

## 🧾 Example 1

### Input
```python
input = [1, 3, 5, 7, 1]
```

### Output
```python
True
```

### Explanation
- The number **1** appears more than once in the list.
- Therefore, the function returns **True**.

---

## 🧾 Example 2

### Input
```python
input = [1, 3, 5, 7]
```

### Output
```python
False
```

### Explanation
- Every element appears only once.
- Therefore, the function returns **False**.

---

## 🧠 Approach
- Convert the list into a **set**
- Since sets only store unique values:
  - If the set length is smaller than the list length, duplicates exist
- Compare lengths and return result

---

## 🚀 Python Solution

```python
def contains_duplicate(input):
    return len(input) != len(set(input))
```

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(n) |
| Space Complexity | O(n) |

---

## 🚀 Key Concepts
- Sets  
- Duplicate Detection  
- List Length Comparison  
- Hashing  

---
