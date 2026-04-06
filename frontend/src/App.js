import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = { role: "user", text: message };
    setChat((prev) => [...prev, userMsg]);
    setMessage("");
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();

      const botMsg = { role: "bot", text: data.response };
      setChat((prev) => [...prev, botMsg]);
    } catch (error) {
      setChat((prev) => [
        ...prev,
        { role: "bot", text: "Error connecting to server." },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      {/* HEADER */}
      <div className="header">
        <h1>Health & Fitness Assistant 🏋️‍♀️</h1>
        <p>Your personal AI guide for diet, BMI & wellness</p>
      </div>

      {/* CHAT BOX */}
      <div className="chat-container">
        {chat.length === 0 && (
          <div className="empty">
            Start chatting about your health goals 💬
          </div>
        )}

        {chat.map((c, i) => (
          <div
            key={i}
            className={c.role === "user" ? "msg user" : "msg bot"}
          >
            {c.text}
          </div>
        ))}

        {loading && <div className="msg bot">Thinking...</div>}
      </div>

      {/* INPUT AREA */}
      <div className="input-box">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about diet, BMI, weight loss..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;