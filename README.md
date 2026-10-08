 NyayaBot — Free Legal Aid for Underserved Indians
 
> **"Justice shouldn't cost a fortune."**
>
> An AI-powered legal aid agent that helps Indian citizens understand their rights, draft legal notices, and find free legal aid — in plain language, in minutes, for free.


## 📌 The Problem

**80% of Indians cannot afford a lawyer.**

Free legal aid is a fundamental right under the **Legal Services Authorities Act, 1987** — but millions never access it because of:

| Barrier | Impact |
|---|---|
| 🌐 **Language** | Legal documents are in complex English or formal Hindi |
| 📍 **Distance** | District Legal Services Authorities are often far away |
| 📚 **Complexity** | Citizens don't know which law applies to their problem |
| 💸 **Cost** | Private lawyers charge ₹5,000+ just for a consultation |
| ⏱️ **Time** | Working people can't take days off to visit courts |

The result: **rights exist on paper, but not in practice** for the majority of Indians.

---

## 💡 Our Solution

**NyayaBot** is a free, AI-powered legal aid agent that bridges the gap between citizens and justice.

### Four Core Capabilities

1. 🧠 **Understands plain language** — English, Hindi, or Hinglish
   > *"Mera landlord deposit wapas nahi kar raha"* → identifies it as a landlord-tenant dispute

2. 📖 **Explains your rights simply** — matched against a curated India-specific law database
   > Cites actual Acts: Transfer of Property Act, Consumer Protection Act 2019, IT Act 2000, etc.

3. 📄 **Generates formal legal notices** — ready to send, downloadable as PDF
   > Professional drafting format, legally sound, no lawyer needed for the first step

4. 🏛️ **Connects to free legal aid** — nearest DLSA + national helplines
   > Because sometimes you DO need a lawyer — and free ones exist

### Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11+, Flask 3.x |
| **AI/LLM** | Groq API (OpenAI GPT-OSS-120B) |
| **PDF Generation** | ReportLab |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Law Data** | Curated India-specific database (7 categories) |
| **Session** | Flask server-side sessions |

---

## 🚀 Quick Start

### Deployed link (Render) -
https://nyayabot-73qq.onrender.com/chat



### Prerequisites

- Python 3.11 or higher
- A free API key from [Groq](https://console.groq.com/keys) (recommended) or [OpenAI](https://platform.openai.com/api-keys)

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/nyayabot.git
cd nyayabot

### 2.Create a virtual environment
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

### 3.Install dependencies
pip install -r requirements.txt

### 4. Configure your API key
Create a .env file in the project root:
FLASK_SECRET_KEY=change-this-to-a-random-string
GROQ_API_KEY=gsk_your_groq_key_here
OPENAI_API_KEY=sk-your_openai_key_here_optional

### 5. Run the app
python app.py

Open http://127.0.0.1:5000 in your browser.






