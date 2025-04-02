import { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import './User-profile.css';

const DEFAULT_IMAGES = {
  frame: '/images/defaults/default-frame.png',
  avatar: '/images/defaults/default-avatar.jpeg',
  header: '/images/defaults/default-header.jpg'
};

const UserProfile = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const { username } = useParams();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`http://localhost:8000/users/username/${username}`);
        setUser(response.data);
        setError(null);
      } catch (err) {
        setError(err.response?.data?.detail || 'Произошла ошибка при загрузке данных пользователя');
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, [username]);

  const getImageUrl = (path) => {
    if (path.startsWith('/static')) {
      return `http://localhost:8000${path}`;
    }
    return path;
  };

  if (loading) {
    return <div className="loading-container">
      <div className="loader"></div>
    </div>;
  }

  if (error) {
    return <div className="error-container">
      <div className="error-message">
        <h2>Ошибка</h2>
        <p>{error}</p>
      </div>
    </div>;
  }

  if (!user) {
    return <div className="not-found-container">
      <h2>Пользователь не найден</h2>
    </div>;
  }

  return (
    <div className='container'>
      <div className="profile-container">
        <div className="profile-card">
          <div className="profile-header" style={{ backgroundImage: `url(${user.header_photo})` }}>
            <div className="profile-info-container">
            <div className="profile-avatar-container">
              <div className="profile-avatar">
                <img src={user.photo} alt={`Аватар пользователя ${user.name}`} />
              </div>
              <div className="profile-frame">
                <img src={getImageUrl(user.frame_photo)} alt="Рамка профиля" />
              </div>
            </div>

            <div className="profile-info">
              <h1>{user.name}</h1>
              <div className="user-meta">
                <span className="age">{user.age} лет</span>
                <span className="user-type">Пользователь</span>
              </div>
              <div className="username">@{user.username}</div>
            </div>
            </div>
          </div>

        </div>
      </div>
      
    </div>
  );
};

export default UserProfile;
