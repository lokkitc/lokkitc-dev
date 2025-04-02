import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Users.css';
import { API_BASE_URL } from '../../config';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/users/`);
        setUsers(response.data);
        setError(null);
      } catch (err) {
        console.error('Error details:', err);
        setError(err.response?.data?.detail || 'Ошибка при загрузке пользователей');
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return <div className="container">Загрузка...</div>;
  }

  if (error) {
    return <div className="container">Ошибка: {error}</div>;
  }

  return (
    <div className="container">
      <div className="users-grid">
        {users.map((user) => (
          <div key={user.user_id} className="user-card">
            <div className="user-photo-container">
              <img 
                src={user.photo || 'путь/к/дефолтной/картинке'} 
                alt={`${user.name} ${user.surname}`}
                className="user-photo"
              />
            </div>
            <h3>{user.name} {user.surname}</h3>
            <p>Имя пользователя: {user.username}</p>
            <p>Email: {user.email}</p>
            <p>Статус: {user.is_active ? 'Активный' : 'Неактивный'}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Users;