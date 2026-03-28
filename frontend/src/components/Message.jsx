import React from "react";
import "../styles/Message.css";

const Message = ({ message }) => {
  return (
    <div className={`message ${message.role}`}>
      <div className="avatar">
        {message.role === "user" ? "🧑" : "🤖"}
      </div>

      <div className="bubble">{message.content}</div>
    </div>
  );
};

export default Message;