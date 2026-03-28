import React, { useEffect, useRef, useState } from "react";
import Message from "./Message.jsx";
import InputBox from "./InputBox.jsx";
import { sendMessage } from "../api";
import "../styles/Chat.css";

const ChatWindow = ({
  messages,
  setMessages,
  chatId,
  setChatId,
}) => {
  const bottomRef = useRef(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSend = async (text) => {
    const userMsg = { role: "user", content: text };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);

    try {
      const res = await sendMessage({
        user_id: "596dc9e1-4ccb-472e-8af7-7a28d782fb41",
        message: text,
        chat_id: chatId,
      });

      setChatId(res.chat_id);

      const botMsg = {
        role: "assistant",
        content: res.message,
      };

      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="chat-window">
      <div className="messages">
        {messages.map((msg, i) => (
          <Message key={i} message={msg} />
        ))}

        {loading && (
          <div className="message assistant">
            <div className="bubble typing">Thinking...</div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      <InputBox onSend={handleSend} />
    </div>
  );
};

export default ChatWindow;