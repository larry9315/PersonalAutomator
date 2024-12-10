import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [helloMessage, setHelloMessage] = useState('');
    const [anotherData, setAnotherData] = useState('');

    useEffect(() => {
        // Fetch data from /api/hello/
        axios.get('http://127.0.0.1:8000/api/hello/')
            .then(response => setHelloMessage(response.data.message))
            .catch(error => console.error('Error fetching hello endpoint:', error));

        // Fetch data from /api/another/
        axios.get('http://127.0.0.1:8000/api/another/')
            .then(response => setAnotherData(response.data.data))
            .catch(error => console.error('Error fetching another endpoint:', error));
    }, []);

    return (
        <div>
            <h1>React and Django Integration</h1>
            <p>Hello Endpoint: {helloMessage}</p>
            <p>Another Endpoint: {anotherData}</p>
        </div>
    );
}

export default App;