# 📊 Probability of a Lazy Netflix Rater

## 📌 Question
Suppose:

- **80%** of Netflix users rate movies:
  - **Thumbs Up:** 60% of the time  
  - **Thumbs Down:** 40% of the time  

- **20%** of Netflix users are **"lazy" raters**:
  - They rate **100%** of movies as **Thumbs Up**

Given that a user gives **3 movies in a row** a **Thumbs Up**, determine:

> **What is the probability that the user is a lazy rater?**

---

## 🧠 Solution

### Terminology

- **LU** = Lazy User  
- **NLU** = Non-Lazy User  

---

### Given Probabilities

| Event | Probability |
|--------|------------|
| P(LU) | 0.2 |
| P(NLU) | 0.8 |
| P(Like \| NLU) | 0.6 |
| P(Not Like \| NLU) | 0.4 |
| P(Like \| LU) | 1.0 |

---

## 📐 Required Formula

We need to calculate:

```text
P(LU | 3 Likes)
```

Using **Bayes' Theorem**:

```text
P(LU | 3 Likes) = P(3 Likes | LU) × P(LU) / P(3 Likes)
```

---

## Step 1: Calculate P(3 Likes)

### Probability of 3 Likes from Non-Lazy User

```text
P(3 Likes | NLU) = 0.6 × 0.6 × 0.6 = 0.216
```

### Probability Contribution from Non-Lazy Users

```text
0.8 × 0.216 = 0.1728
```

---

### Probability of 3 Likes from Lazy User

```text
P(3 Likes | LU) = 1 × 1 × 1 = 1
```

### Probability Contribution from Lazy Users

```text
0.2 × 1 = 0.2
```

---

### Total Probability of 3 Likes

```text
P(3 Likes) = 0.1728 + 0.2 = 0.3728
```

---

## Step 2: Apply Bayes Theorem

```text
P(LU | 3 Likes) = (1 × 0.2) / 0.3728
```

```text
P(LU | 3 Likes) = 0.53648
```

---

## ✅ Final Answer

```text
53.65%
```

> The probability that the user is a **lazy rater** after giving **3 consecutive thumbs up** is:

# **53.65%**

---

## 🚀 Key Concepts Used

- Conditional Probability  
- Bayes’ Theorem  
- Independent Events  
- Probability Trees  

---
