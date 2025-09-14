<h1 align="center">📊 Python Data Visualization Dashboard Demo</h1>

This repository showcases and compares three popular Python frameworks for building interactive dashboards:

- **Streamlit**
- **Plotly Dash**
- **Bokeh**

The same simple application—an interactive scatter plot explorer for the Palmer Penguins dataset—is built in each framework for a clear, side-by-side comparison.

---

## ✨ Features

- **Interactive Dashboard:** Filter and explore the Palmer Penguins dataset.
- **Framework Comparison:** See how the same functionality is implemented in three different ways.
- **Deployment Ready:** Streamlit app is structured for easy deployment on Streamlit Community Cloud.
- **CI/CD Automation:** GitHub Actions workflow automatically lints Python code for quality assurance.

---

## 🚀 Live Demo (Streamlit Version)

> _Replace the link below with your deployed Streamlit app URL._

---

## 🛠️ Tech Stack

- **Language:** 🐍 Python 3.9+
- **Frameworks:** Streamlit, Plotly Dash, Bokeh
- **Core Libraries:** Pandas, Plotly Express
- **Automation:** GitHub Actions (CI/CD for linting)

---

## 📂 Repository Structure

```text
/
├── .github/workflows/
│   └── linter.yml          # GitHub Action for CI Python linting
├── streamlit_app/
│   └── app.py              # Streamlit dashboard
├── dash_app/
│   └── app.py              # Plotly Dash dashboard
├── bokeh_app/
│   └── app.py              # Bokeh dashboard
├── .gitignore              # Git ignore file
├── README.md               # You are here!
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Getting Started (Local Setup)

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Git

git clone https://github.com/YOUR_USERNAME/python-viz-tools-demo.git
pip install -r requirements.txt
dash_app
bokeh_app
bokeh serve --show bokeh_app/app.py
  
- Python 3.9 or higher

---

### Installation & Running

1. **Clone the repository:**
	```bash
	git clone https://github.com/YOUR_USERNAME/python-viz-tools-demo.git
	cd python-viz-tools-demo
	# Replace YOUR_USERNAME with your GitHub username
	```

2. **Create and activate a virtual environment (recommended):**
	```bash
	# For macOS/Linux
	python3 -m venv .venv
	source .venv/bin/activate

	# For Windows
	python -m venv .venv
	.\.venv\Scripts\activate
	```

3. **Install the required dependencies:**
	```bash
	pip install -r requirements.txt
	```

---

## ▶️ Running the Apps

You can run each version of the dashboard from your terminal:

### Streamlit
```bash
streamlit run streamlit_app/app.py
```
Navigate to [http://localhost:8501](http://localhost:8501) in your browser.

### Dash
```bash
python dash_app/app.py
```
Navigate to [http://127.0.0.1:8050](http://127.0.0.1:8050) in your browser.

### Bokeh
```bash
bokeh serve --show bokeh_app/app.py
```
Navigate to [http://localhost:5006](http://localhost:5006) in your browser.

---

## ☁️ Deployment (Streamlit)

The `streamlit_app` is configured for deployment on the Streamlit Community Cloud:

1. Push this repository to your GitHub account.
2. Sign up or log in to [share.streamlit.io](https://share.streamlit.io).
3. Click "New App" and select this repository.
4. Set the "Main file path" to `streamlit_app/app.py`.
5. Deploy!

---

## 🤖 Automation

This project uses GitHub Actions for Continuous Integration. The workflow is defined in `.github/workflows/linter.yml`. It triggers on every push and pull request to:

- Install project dependencies
- Run the flake8 linter to check for Python code quality and style errors

This ensures that the codebase remains clean and consistent.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.