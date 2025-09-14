📊 Python Data Visualization Dashboard Demo: Streamlit vs. Dash vs. Bokeh
This repository serves as a practical showcase and comparison of three popular Python frameworks for building interactive web applications and dashboards: Streamlit, Plotly Dash, and Bokeh.

The same simple application—an interactive scatter plot explorer for the Palmer Penguins dataset—is built in each framework to provide a clear, side-by-side comparison of their syntax, structure, and development philosophy.

✨ Features
Interactive Dashboard: A simple yet functional dashboard to filter and explore the Palmer Penguins dataset.

Framework Comparison: See how the same functionality is implemented in three different ways, helping you choose the right tool for your project.

Deployment Ready: The Streamlit application is structured for easy deployment on Streamlit Community Cloud.

CI/CD Automation: Includes a GitHub Actions workflow to automatically lint Python code for quality assurance.

🚀 Live Demo (Streamlit Version)
(Note: Replace the link above with the URL of your deployed Streamlit app.)

🛠️ Tech Stack
Language: 🐍 Python 3.9+

Frameworks:

Streamlit

Plotly Dash

Bokeh

Core Libraries: Pandas, Plotly Express

Automation: GitHub Actions (CI/CD for linting)

📂 Repository Structure
/
├── .github/workflows/
│   └── linter.yml          # GitHub Action for CI Python linting
├── streamlit_app/
│   └── app.py              # The Streamlit version of the dashboard
├── dash_app/
│   └── app.py              # The Plotly Dash version of the dashboard
├── bokeh_app/
│   └── app.py              # The Bokeh version of the dashboard
├── .gitignore              # Files to be ignored by Git
├── README.md               # You are here!
└── requirements.txt        # All Python dependencies for the project
⚙️ Getting Started (Local Setup)
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Git

Python 3.9 or higher

Installation & Running
Clone the repository:

Bash

git clone https://github.com/YOUR_USERNAME/python-viz-tools-demo.git
cd python-viz-tools-demo
(Replace YOUR_USERNAME with your GitHub username)

Create and activate a virtual environment (recommended):

Bash

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.\.venv\Scripts\activate
Install the required dependencies:

Bash

pip install -r requirements.txt
Running the Apps
You can run each version of the dashboard from your terminal.

streamlit_app
Bash

streamlit run streamlit_app/app.py
Navigate to http://localhost:8501 in your browser.

dash_app
Bash

python dash_app/app.py
Navigate to http://127.0.0.1:8050 in your browser.

bokeh_app
Bash

bokeh serve --show bokeh_app/app.py
Navigate to http://localhost:5006 in your browser.

☁️ Deployment
The streamlit_app is configured for deployment on the Streamlit Community Cloud.

Push this repository to your GitHub account.

Sign up or log in to share.streamlit.io.

Click "New App" and select this repository.

Set the "Main file path" to streamlit_app/app.py.

Deploy!

🤖 Automation
This project uses GitHub Actions for Continuous Integration. The workflow is defined in .github/workflows/linter.yml. It triggers on every push and pull request to:

Install project dependencies.

Run the flake8 linter to check for Python code quality and style errors.

This ensures that the codebase remains clean and consistent.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details (or simply state it if you don't have a file).