# AI Hackers Team - Lablab Hackathon Project Intro

Welcome to the team!

## Setup Guide

### Install Miniconda with Python 3.11

1. Download Miniconda for Python 3.11 from the [official website](https://docs.conda.io/en/latest/miniconda.html).
2. Install Miniconda following the instructions for your operating system.
3. Open a new terminal or command prompt to ensure the installation is recognized.

### Create and Activate a Conda Environment

```
conda create -n ibm-watson python=3.11
conda activate ibm-watson
```

### Install Required Packages

```
pip install -r requirements.txt
```

### Set Up .env File

Create a `.env` file in your project root based on the provided `.env.example`:

```
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
```

Replace `your_api_key_here` and `your_project_id_here` with the values you obtained from IBM Cloud and Watson.

### Run the Script

```
python api-test.py
```

You should now be able to interact with the Watsonx AI through the command line interface.

## Hackathon Participation Guidelines

To ensure smooth collaboration during the hackathon, please follow these guidelines:

### 1. Always Start a New Branch

Before making any changes:

```
git checkout main
git pull origin main
git checkout -b your-feature-name
```

Replace `your-feature-name` with a brief description of your feature or fix.

### 2. Make Your Changes

Implement your feature or fix in the new branch.

### 3. Update Requirements and README

If you've added new dependencies or made significant changes:

1. Update `requirements.txt`:
   ```
   pip freeze > requirements.txt
   ```

2. Update this README if necessary, especially if you've added new setup steps or changed existing ones.

### 4. Commit Your Changes

```
git add .
git commit -m "Brief description of your changes"
```

### 5. Push Your Branch

```
git push origin your-feature-name
```

### 6. Create a Pull Request (PR)

1. Go to the project's GitHub page.
2. Click on "Pull requests" and then "New pull request".
3. Select your branch to compare with main.
4. Fill in the PR template with details about your changes.
5. Submit the PR for review.

### 7. Address Review Comments

If your teammates or mentors suggest changes, make them in your branch and push again. The PR will update automatically.

### 8. Merge Your PR

Once approved, merge your PR into the main branch.

Remember: Frequent communication with your team is key to a successful hackathon!

## Troubleshooting

If you encounter any issues:

1. Ensure your `.env` file is correctly set up with valid credentials.
2. Check your internet connection.
3. Verify that you have the latest version of the required packages by running `pip install -r requirements.txt` again.
4. If you get API errors, check the IBM Cloud console for any service disruptions or quota limits.

If you're still having trouble, don't hesitate to ask your teammates or mentors for help!
