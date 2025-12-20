## 🚀 Getting Started

This section explains how to set up the local environment to run and explore the projects in this repository.

### Prerequisites
- Python **3.13+**
- Git
- Docker & Docker Compose
- (Optional) An API key for OpenAI / Gemini

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/lamnhuthoa/learn-generative-and-agentic-ai.git
cd <repo-name>
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
```

#### macOS / Linux
```bash
source venv/bin/activate
```

#### Windows
```bash
venv\Scripts\activate
```

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables
Create a .env file in the project root:
```bash
OPENAI_API_KEY=your_api_key_here
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run with Docker (Optional)

Some projects are designed to run as containerized services:
```bash
docker compose up
```
Or in detached mode:
```bash
docker compose up -d
```