# 🚀 MyFirstPipeline

[![CI Status](https://github.com/alay/MyFirstPipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/alay/MyFirstPipeline/actions/workflows/ci.yml)
[![Code Coverage](https://codecov.io/gh/alay/MyFirstPipeline/branch/main/graph/badge.svg)](https://codecov.io/gh/alay/MyFirstPipeline)

A complete, end-to-end CI/CD demonstration showcasing professional software deployment patterns. This repository automates **testing, quality assurance, and zero-downtime Blue/Green deployments** using GitHub Actions.

---

## 🏗️ Project Overview

This pipeline demonstrates best practices for modern CI/CD workflows, ensuring code quality and safe production rollouts.

### 🛠️ Core Features
*   **Automated CI/CD:** Full pipeline triggered on `push` and `pull_request` to `main`.
*   **Quality Gates:** Integrated linting (`flake8`) and comprehensive unit testing (`pytest`).
*   **Coverage Reporting:** Detailed code coverage reports uploaded to Codecov.
*   **Blue/Green Deployment:** Implements a safe, zero-downtime strategy that alternates between two isolated production environments.
*   **Environment:** Runs consistently on `ubuntu-latest`.

## 🧱 Project Structure

```
MyFirstPipeline/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD workflow definition
├── src/
│   └── calculator.py       # Core Python business logic
├── tests/
│   └── test_calculator.py  # Unit and integration tests
├── requirements.txt        # Python dependencies list
└── README.md               # Project documentation