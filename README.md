# The Renewables Migration - Chapter 6 Proof Engine
### The Storage Deficit: When the Machine Stops

This repository contains the complete mathematical proof engine for Chapter 6 of "The Renewables Migration" by Vincenzo Grimaldi. It verifies every claim, equation, and figure related to the **Dunkelflaute Resilience** and **Protocol-Driven Balancing**.

## 🚀 Quick Start (Under 60 Seconds)
```bash
# Clone the repository
git clone https://github.com/iceccarelli/Renewables_Migration_Chapter6_Proof_Engine.git
cd Renewables_Migration_Chapter6_Proof_Engine

# Install dependencies
pip install -r requirements.txt

# Run the interactive dashboard
streamlit run main_interactive.py

# Run the automated proofs
pytest tests/test_chapter6.py
```

## 📊 Chapter 6 Metrics Verified
- **Dunkelflaute Energy Gap:** 15.6 TWh (10-day stress test)
- **2026 Storage Limit:** 0.07 TWh (The "Storage Delusion")
- **2025 Redispatch Cost:** €3.1 Billion (Manual Triage)
- **2030 Efficiency Target:** 70% (Autonomous Balancing Efficiency η_AB)
- **Kraftwerksstrategie:** 12 GW H2-ready capacity (Feb 2026)

## 🛠️ Package Structure
- `chapter6_core.py`: Mathematical engine for Dunkelflaute equations and resilience metrics.
- `main_interactive.py`: Streamlit dashboard with "Spy Mode" to highlight book claims.
- `data/book_numbers.csv`: Hardcoded metrics extracted from the book.
- `tests/test_chapter6.py`: Pytest suite validating all book numbers.
- `notebooks/`: Jupyter notebooks for step-by-step proofs.
- `plots/`: Reproduced figures (Figure 6.1, 6.2).

## ⚖️ License
MIT License - Copyright (c) 2026 Vincenzo Grimaldi
