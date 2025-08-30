import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {

    const fetchTasks = async () => {
      try {

        const response = await fetch('http://127.0.0.1:8000/api/tasks/');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setTasks(data);
        setError(null);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

  if (loading) return <div className="loading">Loading tasks...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="app-container">
      <h1>Your Tasks Today</h1>
      <ul className="task-list">
        {tasks.map(task => (
          <li key={task.id} className="task-item">
            <h2>{task.title}</h2>
            <p>{task.description}</p>
            <p>Status: {task.completed ? 'Completed' : 'Incomplete'}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;