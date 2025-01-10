import { useState } from 'react';
import '../css/CopilotInput.css'

const ChatInput = ({ onSend }) => {
    const [message, setMessage] = useState('');

    const handleChange = (event) => {
        setMessage(event.target.value);
    };

    const handleSend = () => {
        if (message.trim()) {
            onSend(message);
            setMessage('');
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSend();
        }
    };

    return (
        <div className="chat-input">
            <input
                type="text"
                value={message}
                onChange={handleChange}
                onKeyPress={handleKeyPress}
                placeholder="Type a message..."
            />
            <button onClick={handleSend}>Send</button>
        </div>
    );
};

export default ChatInput;
