# CGCNN Reproduction and Extension Project

This repository contains work toward reproducing and extending the **Crystal Graph Convolutional Neural Network (CGCNN)** originally proposed by **Xie & Grossman (2018)** for crystal property prediction.

The project is structured into three phases:

---

### Phase 1 — Pipeline Setup and Initial Validation  *(Completed)*

- Configure and test the full CGCNN framework.
- Generate a small dataset using the Materials Project API.
- Verify that the model trains end-to-end on custom CIF data.

---

### Phase 2 — Baseline Reproduction

- Build the full dataset using Materials Project IDs referenced in the original paper.
- Train CGCNN to predict formation energy per atom.
- Compare performance against the reported published baseline.

---

### Phase 3 — Application: Nickel Superalloy Screening

- Construct a focused dataset relevant to Nickel-based superalloys.
- Extend the model to predict **energy above hull**.
- Identify potential alloy candidates based on predicted stability.

---

### Notes

- Data files and API credentials are intentionally excluded from the repository.
- The project will be documented in more detail after Phase 2 and Phase 3.

---

#### Reference

Xie, T., & Grossman, J. C. (2018).  
*Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties.*  
Physical Review Letters, 120(14), 145301.

