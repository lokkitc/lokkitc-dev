import React, { useState, useEffect } from 'react';
import './Users.css';
function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch('http://localhost:8000/users/');
        if (!response.ok) {
          throw new Error('Ошибка при загрузке пользователей');
        }
        const data = await response.json();
        setUsers(data);
      } catch (err) {
        setError(err.message);
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
            <h2 style={{color: 'var(--color-text-primary)'}}>Список пользователей</h2>
      <div className="users-header">

      <div className="users-grid">
        {users.map((user) => (
          <div key={user.user_id} className="user-card">
            <div className="user-photo-container">
            <img 
              src={user.photo || 'путь/к/дефолтной/картинке'} 
              alt={`${user.name} ${user.surname}`}
              className="user-photo"
            /></div>
            <h3>{user.name} {user.surname}</h3>
            <p>Имя пользователя: {user.username}</p>
            <p>Email: {user.email}</p>
            <p>Статус: {user.is_active ? 'Активный' : 'Неактивный'}</p>
          </div>
          
        ))}
        </div>
      </div>
    </div>
  );
}

export default Users;