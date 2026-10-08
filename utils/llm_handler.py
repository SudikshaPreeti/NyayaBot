import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

PROVIDER = "groq"

if PROVIDER == "openai":
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or "missing-key")
    MODEL = "gpt-4o-mini"
elif PROVIDER == "groq":
    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )
    MODEL = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """You are NyayaBot, a compassionate legal aid assistant for Indian citizens.
Your role:
1. Understand the citizen's legal problem in plain language (English or Hinglish).
2. Explain relevant Indian laws and their rights in SIMPLE, non-technical language.
3. Be empathetic, clear, and empowering — many users cannot afford lawyers.
4. NEVER give definitive legal advice; always recommend consulting a free legal aid clinic for serious matters.
5. Cite actual Indian Acts and Sections where possible.
6. Format responses with clear headings and bullet points.
7. Keep responses concise — under 350 words unless the user asks for more.
"""

def get_ai_response(user_message: str, matched_law: dict = None, history: list = None) -> str:
    context = ""
    if matched_law:
        context = f"""
Relevant Legal Context (auto-detected category: {matched_law.get('title')}):

Applicable Laws:
{chr(10).join('- ' + l for l in matched_law.get('laws', []))}

Citizen's Rights:
{chr(10).join('- ' + r for r in matched_law.get('rights', []))}

Possible Remedies:
{chr(10).join('- ' + r for r in matched_law.get('remedies', []))}

Appropriate Forum: {matched_law.get('forum', 'N/A')}
"""

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if history:
        messages.extend(history[-6:])
    messages.append({
        "role": "user",
        "content": f"{context}\n\nCitizen's Problem: {user_message}\n\nRespond helpfully with:\n1. Empathetic acknowledgment\n2. Relevant laws & rights\n3. Step-by-step actions\n4. Emergency helplines if needed"
    })

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.4,
            max_tokens=800,
        )
        return response.choices[0].message.content
    except Exception as e:
        return _fallback_response(matched_law, str(e))

def _fallback_response(matched_law, err=""):
    if not matched_law:
        return (
            "I could not reach the AI service right now. Please describe your problem "
            "with more specific keywords (e.g., 'landlord deposit', 'unpaid salary', "
            "'consumer refund', 'cyber fraud') and try again.\n\n"
            f"(Debug: {err[:120]})"
        )
    return (
        f"**{matched_law['title']}** (offline mode — AI unavailable)\n\n"
        f"**Your Rights:**\n" + "\n".join(f"• {r}" for r in matched_law["rights"]) +
        f"\n\n**Remedies:**\n" + "\n".join(f"• {r}" for r in matched_law["remedies"]) +
        f"\n\n**Forum:** {matched_law['forum']}"
    )

def generate_legal_letter(problem: str, user_details: dict, matched_law: dict = None) -> str:
    law_context = ""
    if matched_law:
        law_context = f"Relevant laws: {', '.join(matched_law.get('laws', []))}"

    prompt = f"""Generate a formal legal notice/complaint letter in Indian legal format.

Sender Details:
- Name: {user_details.get('name', '[Your Name]')}
- Address: {user_details.get('address', '[Your Address]')}
- Phone: {user_details.get('phone', '[Your Phone]')}

Recipient: {user_details.get('recipient', '[Recipient Name & Address]')}

Issue: {problem}

{law_context}

Format:
1. Proper heading (LEGAL NOTICE / COMPLAINT)
2. Date
3. From/To addresses
4. Subject line
5. Body with facts, legal grounds, demand
6. Timeline for response (15 days)
7. Consequences of non-compliance
8. Signature block

Use formal Indian legal English. Keep it concise and legally sound. Include relevant Act names.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an expert Indian legal draftsman."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return _fallback_letter(problem, user_details, matched_law, str(e))

def _fallback_letter(problem, details, matched_law, err=""):
    laws = ", ".join(matched_law.get("laws", [])) if matched_law else "relevant Indian laws"
    return f"""LEGAL NOTICE

Date: [Today's Date]

From:
{details.get('name', '[Your Name]')}
{details.get('address', '[Your Address]')}
Phone: {details.get('phone', '[Your Phone]')}

To:
{details.get('recipient', '[Recipient Name & Address]')}

SUBJECT: Legal Notice regarding {matched_law.get('title') if matched_law else 'grievance'}

Sir/Madam,

Under instructions from and on behalf of my client, I hereby serve you this legal notice:

1. That the following facts constitute my grievance: {problem}

2. That your actions are in violation of {laws}.

3. That you are hereby called upon to remedy the aforesaid grievance within 15 (fifteen) days of receipt of this notice.

4. That failing compliance, I shall be constrained to initiate appropriate legal proceedings against you at your sole risk as to costs and consequences.

This notice is issued without prejudice to my other rights and remedies.

Yours faithfully,
{details.get('name', '[Your Name]')}

(Note: AI generation was unavailable — this is a template draft. Please review before sending.)
"""