import React, { useState } from 'react';
import { searchProducts, storeChatLog } from '../services/api';
import ProductCard from './ProductCard';

const Chatbot = () => {
  const [query, setQuery] = useState('');
  const [chat, setChat] = useState([]);
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    setChat([...chat, `User: ${query}`]);
    const res = await searchProducts(query);
    setResults(res.data);
    setChat([...chat, `User: ${query}`, `Bot: Found ${res.data.length} product(s).`]);
    setQuery('');
  };

  const handleStore = async () => {
    const sessionId = `session_${Date.now()}`;
    await storeChatLog(sessionId, chat);
    alert('Chat log saved.');
  };

  return (
    <div className="container mt-4">
      <h2>🛍️ SmartShop Chatbot</h2>
      <div className="mb-3">
        <input
          className="form-control"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about a product (e.g., 'laptop under 50000')"
        />
        <button className="btn btn-primary mt-2" onClick={handleSearch}>Send</button>
        <button className="btn btn-secondary mt-2 ms-2" onClick={handleStore}>Save Chat</button>
      </div>
      <div className="chat-box">
        {chat.map((msg, i) => (
          <div key={i} className="chat-msg">{msg}</div>
        ))}
      </div>
      <hr />
      <div className="row">
        {results.map(product => (
          <div className="col-md-4" key={product.id}>
            <ProductCard product={product} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Chatbot;
