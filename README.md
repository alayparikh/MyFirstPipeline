# MyFirstPipeline

A comprehensive CI/CD pipeline demonstration project showcasing automated testing, code coverage, and Blue/Green deployment using GitHub Actions.

## Project Structure

```
MyFirstPipeline/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD pipeline
├── src/
│   └── calculator.py       # Sample Python module
├── tests/
│   └── test_calculator.py  # Unit tests
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Features

- Automated CI/CD pipeline triggered on push and pull requests
- Runs on Ubuntu latest environment
- **Automated Testing**: Unit tests using pytest
- **Code Coverage**: Coverage reporting with pytest-cov and Codecov integration
- **Code Quality**: Linting with flake8 for code style and error checking
- **Blue/Green Deployment**: Zero-downtime deployment strategy that alternates between two identical environments

## Testing and Code Coverage

This project includes comprehensive automated testing:

- **Unit Tests**: Written with pytest, covering core functionality
- **Coverage Reporting**: Generates coverage reports showing which lines of code are tested
- **Codecov Integration**: Uploads coverage data to Codecov for detailed analysis and badges

### Running Tests Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `pytest`
3. Run with coverage: `pytest --cov=src --cov-report=html`

Coverage reports are automatically generated in CI and uploaded to Codecov.

## Blue/Green Deployment

This pipeline implements a basic Blue/Green deployment strategy:

- **Blue Environment**: One production environment
- **Green Environment**: Another identical production environment
- **Deployment Process**:
  1. The pipeline determines the target environment (Blue or Green) based on the workflow run number
  2. Deploys the application to the inactive environment
  3. Simulates switching traffic to the newly deployed environment
- **Benefits**: Reduces downtime, enables easy rollback, and allows testing in production-like conditions

The deployment alternates between Blue and Green environments with each push to `main`.

## How to Run the Pipeline

1. **Push to GitHub**: Ensure your code is pushed to a GitHub repository.
2. **Trigger the Pipeline**:
   - The pipeline automatically runs on:
     - Pushes to the `main` branch (includes build and deployment)
     - Pull requests targeting the `main` branch (build only)
3. **Check the Status**:
   - Go to the **Actions** tab in your GitHub repository.
   - Click on the latest workflow run to see the logs.
   - The pipeline is runnable as long as the repository has the `.github/workflows/ci.yml` file.
   - For pushes to `main`, you'll see both `build` and `deploy` jobs.

## Screenshots

### Pipeline Status Badge
The badge at the top shows the current status of the CI pipeline (passing/failing).

### Actions Tab
![Actions Tab](https://via.placeholder.com/800x400?text=GitHub+Actions+Tab+Screenshot)
*Screenshot of the GitHub Actions tab showing the workflow runs.*

### Workflow Details
![Workflow Details](https://via.placeholder.com/800x400?text=Workflow+Run+Details+Screenshot)
*Detailed view of a workflow run, including job steps and logs.*

*Note: Replace the placeholder images with actual screenshots from your GitHub repository.*

## Contributing

Feel free to contribute by adding more features to the pipeline or improving the documentation.
