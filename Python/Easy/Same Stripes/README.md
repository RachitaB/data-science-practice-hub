# 🧩 Same Stripes (ServiceNow)

## ❓ Problem

Given an `m x n` matrix, determine whether all **diagonals (top-left → bottom-right)** have the same values.

Return **True** if every diagonal contains identical elements, otherwise return **False**.

---

## 📌 Examples

### Example 1

Input:

```
[[42, 7, 13, 99],
 [6, 42, 7, 13],
 [1, 6, 42, 7]]
```

Output:

```
True
```

---

### Example 2

Input:

```
[[8, 23],
 [69, 1]]
```

Output:

```
False
```

---

## 🧠 Approach

* Each diagonal has a constant difference:
  👉 `i - j` is same for all elements in a diagonal

* For every cell:

  * Compare it with its **top-left neighbor**
  * If mismatch → return False

---

## ⏱️ Complexity

* Time: **O(m × n)**
* Space: **O(1)**

---
