from flask import Flask, render_template, request, jsonify, send_file, session
from config import Config
from utils.law_database import match_problem, LEGAL_AID_CLINICS, NATIONAL_HELPLINES, LAW_DATABASE
from utils.llm_handler import get_ai_response, generate_legal_letter
from utils.pdf_generator import create_letter_pdf
import uuid

app = Flask(__name__)
app.config.from_object(Config)

conversations = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    sid = session.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if sid not in conversations:
        conversations[sid] = []

    matched = match_problem(user_message)
    ai_reply = get_ai_response(user_message, matched, conversations[sid])

    conversations[sid].append({"role": "user", "content": user_message})
    conversations[sid].append({"role": "assistant", "content": ai_reply})

    return jsonify({
        "reply": ai_reply,
        "matched_category": matched.get("title") if matched else None,
        "matched_laws": matched.get("laws") if matched else [],
        "rights": matched.get("rights") if matched else [],
        "remedies": matched.get("remedies") if matched else [],
        "forum": matched.get("forum") if matched else None,
    })

@app.route("/letter", methods=["GET"])
def letter():
    return render_template("letter.html")

@app.route("/api/letter", methods=["POST"])
def api_letter():
    data = request.get_json()
    problem = data.get("problem", "")
    details = {
        "name": data.get("name", ""),
        "address": data.get("address", ""),
        "phone": data.get("phone", ""),
        "recipient": data.get("recipient", ""),
    }
    matched = match_problem(problem)
    letter_text = generate_legal_letter(problem, details, matched)
    session["last_letter"] = letter_text
    return jsonify({"letter": letter_text})

@app.route("/download_letter", methods=["GET"])
def download_letter():
    letter_text = session.get("last_letter", "No letter generated yet.")
    pdf = create_letter_pdf(letter_text)
    return send_file(pdf, mimetype="application/pdf",
                     as_attachment=True, download_name="NyayaBot_Legal_Notice.pdf")

@app.route("/clinics")
def clinics():
    return render_template("clinics.html",
                           clinics=LEGAL_AID_CLINICS,
                           helplines=NATIONAL_HELPLINES)

@app.route("/api/categories")
def categories():
    return jsonify([{"key": k, "title": v["title"]} for k, v in LAW_DATABASE.items()])

if __name__ == "__main__":
    app.run(debug=True, port=5000)