# Testing ML Return Forecasts Under Transaction Costs

**Author:** Bernard Shen  
**Status:** Personal Research Project (Active Development)

## Project Overview
This project explores the "Paper vs. Practice" gap in quantitative finance. Specifically, it examines whether the superior statistical predictive power ($R^2$, MSE) often observed in Machine Learning models (LASSO, Neural Networks) translates into realizable economic value (Net Sharpe Ratio) once realistic transaction costs are applied.

## Methodology
* **Prediction Models:** Training LASSO and Neural Networks on a rolling window of monthly-lagged features (consistent with Gu, Kelly & Xiu, 2020) to forecast S&P 500 stock returns.
* **Portfolio Construction:** Rank-weighted, dollar-neutral long/short portfolios.
* **Market Impact:** Simulation of execution costs using the **Square-Root Impact Law**, calibrated to reflect liquidity slippage for large institutional portfolios (e.g., $1B AUM).

## Repository Context & Architecture
This repository contains the code necessary to reproduce the data pipeline and simulation engine. Note the following regarding the current state of specific files:

* **`02_ml_transaction_costs.ipynb` (MVP):**
    * This notebook represents a **lean Proof of Concept (POC)**.
    * It implements the end-to-end pipeline for the LASSO model to demonstrate the core strategy.
    * *Note:* It does not yet include the Neural Network models, full benchmark comparisons ($1/N$), or the comprehensive data analysis planned for future iterations.

* **`fundamental_models.py` (Legacy):**
    * Contains class definitions for fundamental econometric models (ARMA, VAR, GARCH).
    * *Note:* These files are from a previous iteration of the project. They are **deprecated** and not currently used in the active machine learning workflow.

* **`preprocessing.ipynb`:**
    * The active ETL pipeline that merges proprietary CRSP/Compustat data and generates predictive features.

## Preliminary Findings (MVP)
Initial backtests using the LASSO model at a simulated **$1B AUM** indicate:
* **Gross Sharpe (Paper):** ~0.73 (Highly profitable)
* **Net Sharpe (Practice):** ~0.08 (Alpha consumed by costs)
* **Key Insight:** The high turnover required to capture ML signals generates transaction costs that may outweigh the statistical advantage of the "smarter" model.
