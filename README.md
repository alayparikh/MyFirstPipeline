# MyFirstPipeline

[![CI](https://github.com/alay/MyFirstPipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/alay/MyFirstPipeline/actions/workflows/ci.yml)

A basic CI/CD pipeline demonstration project showcasing automated workflows using GitHub Actions.

## Features

- Automated CI/CD pipeline triggered on push and pull requests
- Runs on Ubuntu latest environment
- Simple build and test simulation
- **Blue/Green Deployment**: Zero-downtime deployment strategy that alternates between two identical environments

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
