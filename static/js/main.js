// ============ CHAT PAGE ============
const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.className = `message ${sender === "user" ? "user-message" : "bot-message"}`;
    const avatar = sender === "user" ? "🧑" : "⚖️";
    msg.innerHTML = `
        <div class="avatar">${avatar}</div>
        <div class="bubble">${text.replace(/\n/g, "<br>")}</div>
    `;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
    return msg;
}

function addTyping() {
    const msg = document.createElement("div");
    msg.className = "message bot-message typing";
    msg.id = "typingIndicator";
    msg.innerHTML = `<div class="avatar">⚖️</div><div class="bubble">NyayaBot is thinking…</div>`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
    const el = document.getElementById("typingIndicator");
    if (el) el.remove();
}

async function sendMessage(text) {
    if (!text || !text.trim()) return;
    addMessage(text, "user");
    userInput.value = "";
    addTyping();

    try {
        const res = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text }),
        });
        const data = await res.json();
        removeTyping();
        addMessage(data.reply || "Sorry, something went wrong.", "bot");
    } catch (err) {
        removeTyping();
        addMessage("⚠️ Network error. Please try again.", "bot");
        console.error(err);
    }
}

if (sendBtn && userInput) {
    sendBtn.addEventListener("click", () => sendMessage(userInput.value));
    userInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage(userInput.value);
        }
    });
}

document.querySelectorAll(".quick-btn").forEach((btn) => {
    btn.addEventListener("click", () => sendMessage(btn.dataset.prompt));
});

// ============ LETTER PAGE ============
const generateBtn = document.getElementById("generateBtn");

if (generateBtn) {
    generateBtn.addEventListener("click", async () => {
        const name = document.getElementById("name").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const address = document.getElementById("address").value.trim();
        const recipient = document.getElementById("recipient").value.trim();
        const problem = document.getElementById("problem").value.trim();

        if (!name || !address || !recipient || !problem) {
            alert("Please fill in Name, Address, Recipient, and Problem.");
            return;
        }

        generateBtn.disabled = true;
        generateBtn.textContent = "⏳ Generating…";

        try {
            const res = await fetch("/api/letter", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, phone, address, recipient, problem }),
            });
            const data = await res.json();

            document.getElementById("letterContent").textContent = data.letter;
            document.getElementById("letterOutput").classList.remove("hidden");
            document.getElementById("letterOutput").scrollIntoView({ behavior: "smooth" });
        } catch (err) {
            alert("Failed to generate letter. Please try again.");
            console.error(err);
        } finally {
            generateBtn.disabled = false;
            generateBtn.textContent = "✨ Generate Legal Notice";
        }
    });
}