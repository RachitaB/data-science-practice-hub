# 📊 Expected Value of Minimum of Two Uniform Random Variables

## 📌 Question
Suppose:

- **X ~ Uniform(0,1)**
- **Y ~ Uniform(0,1)**

and **X** and **Y** are independent.

Determine:

> **What is the expected value of**  
> **min(X, Y)?**

---

## 🧠 Solution

Let:

```text
A = min(X, Y)
```

We want to compute:

```text
E[A]
```

---

## Step 1: Find the CDF of A

We start with:

```text
P(A ≤ k) = P(min(X,Y) ≤ k)
```

Using complement rule:

```text
P(A ≤ k) = 1 − P(X > k AND Y > k)
```

Since **X** and **Y** are independent:

```text
P(A ≤ k) = 1 − P(X > k) × P(Y > k)
```

For Uniform(0,1):

```text
P(X > k) = P(Y > k) = 1-k
```

Thus:

```text
P(A ≤ k) = 1 − (1-k)²
```

Expanding:

```text
P(A ≤ k) = 1 − (1 − 2k + k²)
```

```text
P(A ≤ k) = 2k − k²
```

So the **CDF** is:

```text
F_A(k) = 2k − k²
```

---

## Step 2: Find the PDF

Differentiate the CDF:

```text
f_A(k) = d/dk (2k − k²)
```

```text
f_A(k) = 2 − 2k
```

---

## Step 3: Compute Expected Value

Using:

```text
E[A] = ∫₀¹ k f_A(k) dk
```

Substitute PDF:

```text
E[A] = ∫₀¹ k(2 − 2k) dk
```

Factor out 2:

```text
E[A] = 2∫₀¹ k(1-k) dk
```

Expand:

```text
E[A] = 2∫₀¹ (k − k²) dk
```

Integrate:

```text
E[A] = 2[(k²/2) − (k³/3)] from 0 to 1
```

Substitute limits:

```text
E[A] = 2[(1/2) − (1/3)]
```

```text
E[A] = 2[(3−2)/6]
```

```text
E[A] = 2(1/6)
```

```text
E[A] = 1/3
```

---

## ✅ Final Answer

```text
E[min(X,Y)] = 1/3
```

---

## 🏆 Conclusion

> The expected value of the minimum of two independent Uniform(0,1) random variables is:

# **1/3**

---

## 🚀 Key Concepts Used

- Uniform Distribution  
- CDF/PDF Conversion  
- Complement Rule  
- Independence of Random Variables  
- Integration / Expected Value Formula  

---
