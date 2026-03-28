import React, { useState } from "react";
import Sidebar from "./components/Sidebar.jsx";
import ChatWindow from "./components/ChatWindow.jsx";
import "./styles/App.css";

const App = () => {
  const [messages, setMessages] = useState([]);
  const [chatId, setChatId] = useState(null);
  const userId = "demo-user";

  return (
    <div className="app">
      <Sidebar />
      <ChatWindow
        messages={messages}
        setMessages={setMessages}
        chatId={chatId}
        setChatId={setChatId}
        userId={userId}
      />
    </div>
  );
};

export default App;