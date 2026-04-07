from flask import Flask, request, jsonify
from agent import ask_agent
import time

app = Flask(__name__)

@app.route("/")
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Bharat Upadhyay's Confluence RAG Agent</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: #f5f5f5;
            color: #1a1a1a;
            min-height: 100vh;
            padding: 40px 20px;
        }

        .app {
            max-width: 900px;
            margin: 0 auto;
        }

        .topbar {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 2rem;
            padding-bottom: 1.25rem;
            border-bottom: 0.5px solid #e0e0e0;
        }

        .logo {
            width: 48px;
            height: 48px;
            background: #185FA5;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }

        .brand {
            font-size: 26px;
            font-weight: 700;
            color: #1a1a1a;
        }

        .brand span {
            color: #185FA5;
            font-size: 28px;
            font-weight: 800;
        }

        .badge {
            margin-left: auto;
            font-size: 11px;
            background: #E6F1FB;
            color: #185FA5;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 500;
            border: 0.5px solid #185FA5;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 1.5rem;
        }

        .stat {
            background: #ffffff;
            border: 0.5px solid #e0e0e0;
            border-radius: 10px;
            padding: 14px 16px;
        }

        .stat-val {
            font-size: 22px;
            font-weight: 500;
            color: #1a1a1a;
        }

        .stat-label {
            font-size: 12px;
            color: #888888;
            margin-top: 2px;
        }

        .input-card {
            background: #ffffff;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 1rem;
        }

        .input-label {
            font-size: 11px;
            color: #888888;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        textarea {
            width: 100%;
            background: #f5f5f5;
            border: 0.5px solid #dddddd;
            border-radius: 8px;
            padding: 12px 14px;
            font-size: 14px;
            color: #1a1a1a;
            resize: vertical;
            font-family: inherit;
            min-height: 80px;
            outline: none;
            transition: border-color 0.15s;
        }

        textarea:focus { border-color: #185FA5; }

        .actions {
            display: flex;
            gap: 10px;
            margin-top: 12px;
        }

        .btn-primary {
            background: #185FA5;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: background 0.15s;
        }

        .btn-primary:hover { background: #0C447C; }
        .btn-primary:disabled { background: #a8c4e0; cursor: not-allowed; }

        .btn-secondary {
            background: transparent;
            color: #777777;
            border: 0.5px solid #dddddd;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 14px;
            cursor: pointer;
        }

        .btn-secondary:hover { border-color: #aaaaaa; color: #444444; }

        .loading {
            display: none;
            align-items: center;
            gap: 8px;
            padding: 12px 0;
            font-size: 13px;
            color: #888888;
        }

        .spinner {
            width: 14px;
            height: 14px;
            border: 2px solid #e0e0e0;
            border-top-color: #185FA5;
            border-radius: 50%;
            animation: spin 0.7s linear infinite;
        }

        @keyframes spin { to { transform: rotate(360deg); } }

        .result-card {
            background: #ffffff;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 1rem;
            display: none;
        }

        .result-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 16px;
            border-bottom: 0.5px solid #eeeeee;
            background: #fafafa;
        }

        .result-title {
            font-size: 11px;
            color: #888888;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #185FA5;
        }

        .answer-output {
            padding: 1.25rem;
            font-size: 14px;
            line-height: 1.8;
            color: #1a1a1a;
            white-space: pre-wrap;
        }

        .sources-section {
            padding: 12px 16px;
            border-top: 0.5px solid #eeeeee;
            background: #fafafa;
        }

        .sources-title {
            font-size: 11px;
            color: #888888;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 8px;
        }

        .source-pill {
            display: inline-block;
            font-size: 12px;
            background: #E6F1FB;
            color: #0C447C;
            padding: 4px 12px;
            border-radius: 20px;
            margin: 3px;
            border: 0.5px solid #185FA5;
        }

        .history-section { margin-top: 2rem; }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }

        .section-title {
            font-size: 11px;
            font-weight: 500;
            color: #888888;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .clear-link {
            font-size: 12px;
            color: #c0392b;
            cursor: pointer;
            background: none;
            border: none;
        }

        .history-item {
            background: #ffffff;
            border: 0.5px solid #eeeeee;
            border-radius: 10px;
            padding: 12px 16px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: border-color 0.15s;
        }

        .history-item:hover { border-color: #185FA5; }

        .h-question { font-size: 13px; color: #666666; margin-bottom: 4px; }
        .h-answer { font-size: 12px; color: #333333; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .h-time { font-size: 11px; color: #999999; margin-top: 6px; }

        .no-history { font-size: 13px; color: #aaaaaa; text-align: center; padding: 2rem 0; }

        .sample-questions {
            margin-bottom: 1.5rem;
        }

        .sample-label {
            font-size: 11px;
            color: #888888;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 8px;
        }

        .sample-btn {
            display: inline-block;
            font-size: 12px;
            background: #ffffff;
            color: #185FA5;
            padding: 6px 14px;
            border-radius: 20px;
            margin: 3px;
            border: 0.5px solid #185FA5;
            cursor: pointer;
            transition: background 0.15s;
        }

        .sample-btn:hover { background: #E6F1FB; }
    </style>
</head>
<body>
<div class="app">

    <div class="topbar">
        <div class="logo">📋</div>
        <div>
            <div class="brand"><span>Bharat Upadhyay's</span> Confluence RAG Agent</div>
        </div>
        <div class="badge">Powered by LLaMA 3.2 + RAG</div>
    </div>

    <div class="stats">
        <div class="stat">
            <div class="stat-val" id="stat-count">0</div>
            <div class="stat-label">Questions answered</div>
        </div>
        <div class="stat">
            <div class="stat-val">10</div>
            <div class="stat-label">Confluence pages indexed</div>
        </div>
        <div class="stat">
            <div class="stat-val">100%</div>
            <div class="stat-label">Local and private</div>
        </div>
    </div>

    <div class="sample-questions">
        <div class="sample-label">Try asking</div>
        <span class="sample-btn" onclick="askSample(this)">How many customers were affected in the bonus interest remediation?</span>
        <span class="sample-btn" onclick="askSample(this)">What was the root cause of the bonus interest error?</span>
        <span class="sample-btn" onclick="askSample(this)">What is the total remediation amount for the loan fee waiver?</span>
        <span class="sample-btn" onclick="askSample(this)">How is the time value of money calculated?</span>
        <span class="sample-btn" onclick="askSample(this)">What were the exclusion criteria for loan fee remediation?</span>
    </div>

    <div class="input-card">
        <div class="input-label">Ask a question about your remediation documents</div>
        <textarea id="question" placeholder="e.g. What was the root cause of the bonus interest error?"></textarea>
        <div class="actions">
            <button class="btn-primary" id="askBtn" onclick="askQuestion()">
                🔍 Ask Agent
            </button>
            <button class="btn-secondary" onclick="clearInput()">Clear</button>
        </div>
        <div class="loading" id="loading">
            <div class="spinner"></div>
            Searching Confluence pages and generating answer...
        </div>
    </div>

    <div class="result-card" id="resultCard">
        <div class="result-header">
            <div class="result-title"><div class="dot"></div> Answer</div>
        </div>
        <div class="answer-output" id="answer"></div>
        <div class="sources-section">
            <div class="sources-title">Sources</div>
            <div id="sources"></div>
        </div>
    </div>

    <div class="history-section">
        <div class="section-header">
            <div class="section-title">Question history</div>
            <button class="clear-link" onclick="clearHistory()">Clear all</button>
        </div>
        <div id="history"></div>
    </div>

</div>

<script>
    let questionCount = 0;
    let historyItems = [];

    async function askQuestion() {
        const question = document.getElementById("question").value.trim();
        if (!question) return;

        document.getElementById("askBtn").disabled = true;
        document.getElementById("loading").style.display = "flex";
        document.getElementById("resultCard").style.display = "none";

        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        document.getElementById("askBtn").disabled = false;
        document.getElementById("loading").style.display = "none";
        document.getElementById("resultCard").style.display = "block";
        document.getElementById("answer").innerText = data.answer;

        const sourcesDiv = document.getElementById("sources");
        sourcesDiv.innerHTML = data.sources.map(s =>
            `<span class="source-pill">${s}</span>`
        ).join("");

        questionCount++;
        document.getElementById("stat-count").innerText = questionCount;

        const now = new Date();
        const timestamp = now.toLocaleTimeString();

        historyItems.unshift({
            question: question,
            answer: data.answer,
            timestamp: timestamp
        });

        renderHistory();
    }

    function askSample(el) {
        document.getElementById("question").value = el.innerText;
        askQuestion();
    }

    function clearInput() {
        document.getElementById("question").value = "";
        document.getElementById("resultCard").style.display = "none";
    }

    function renderHistory() {
        const container = document.getElementById("history");

        if (historyItems.length === 0) {
            container.innerHTML = "<div class='no-history'>No questions yet. Ask something above!</div>";
            return;
        }

        container.innerHTML = historyItems.map((item, index) => `
            <div class="history-item" onclick="loadHistory(${index})">
                <div class="h-question">💬 ${item.question}</div>
                <div class="h-answer">${item.answer}</div>
                <div class="h-time">🕐 ${item.timestamp}</div>
            </div>
        `).join("");
    }

    function loadHistory(index) {
        const item = historyItems[index];
        document.getElementById("question").value = item.question;
        document.getElementById("answer").innerText = item.answer;
        document.getElementById("resultCard").style.display = "block";
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function clearHistory() {
        historyItems = [];
        questionCount = 0;
        document.getElementById("stat-count").innerText = 0;
        renderHistory();
    }

    renderHistory();
</script>
</body>
</html>
'''

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    result = ask_agent(question)
    return jsonify({
        "answer": result["answer"],
        "sources": result["sources"]
    })

if __name__ == "__main__":
    app.run(debug=True)
