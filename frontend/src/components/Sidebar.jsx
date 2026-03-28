import React from "react";
import "../styles/Sidebar.css";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Copilot</h2>

      <button className="new-chat">+ New Chat</button>

      <div className="history">
        <p>No chats yet</p>
      </div>
    </div>
  );
};

export default Sidebar;