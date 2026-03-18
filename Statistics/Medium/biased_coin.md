# 🪙 Biased Coin (D.E. Shaw)

## ❓ Problem

A coin is flipped **1000 times**, and **550 heads** are observed.

Is the coin biased?

---

## 🧠 Hypothesis

* **H₀ (Null Hypothesis):** Coin is fair → p = 0.5
* **H₁ (Alternative Hypothesis):** Coin is biased → p ≠ 0.5

---

## 📊 Approach

Since sample size is large (n = 1000), we use **Central Limit Theorem (Normal Approximation)**.

* n = 1000
* p = 0.5

### Expected value (mean)

μ = n × p = 1000 × 0.5 = 500

### Standard deviation

σ = √(n × p × (1 - p))
= √(1000 × 0.5 × 0.5)
= √250 ≈ 15.81

---

## 📉 Z-Score

Z = (X - μ) / σ
= (550 - 500) / 15.81
≈ 3.16

---

## 📉 P-value

From Z-table:

P(Z < 3.16) ≈ 0.9992

Since this is a **two-tailed test**:

p-value = 1 - 0.9992
= **0.0008**

---

## ✅ Conclusion

Since **p-value (0.0008) < 0.05**,
we **reject the null hypothesis**.

👉 The coin is **very likely biased**.

---

## 💡 Insight

* Large sample → use **normal approximation to binomial**
* Always check:

  * One-tailed vs Two-tailed test
* A Z-score of **3.16 is extremely significant**

---
