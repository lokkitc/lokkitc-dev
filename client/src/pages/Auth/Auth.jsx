import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Auth.css';
import { API_BASE_URL } from '../../config';
import { User, LogIn, UserPlus } from 'lucide-react';

const Auth = () => {
    const [formData, setFormData] = useState({
        name: '',
        surname: '',
        username: '',
        email: '',
        password: ''
    });
    const [isLogin, setIsLogin] = useState(true);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const url = isLogin ? `${API_BASE_URL}/users/login` : `${API_BASE_URL}/users/`;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                throw new Error('Ошибка при отправке данных');
            }

            const data = await response.json();
            console.log(data);
            navigate("/");
        } catch (error) {
            console.error('Ошибка:', error);
        }
    };

    return (
        <div className="auth-container">
            <div className='auth-container-buttons'>
                <button onClick={() => setIsLogin(true)}>
                    <LogIn size={20} /> Авторизация
                </button>
                <button onClick={() => setIsLogin(false)}>
                    <UserPlus size={20} /> Регистрация
                </button>
            </div>
            <div className={`form-container ${isLogin ? '' : 'hidden'}`}>
                <form className="auth-form" onSubmit={handleSubmit}>
                    <h2>Вход в систему</h2>
                    <div className="form-group">
                        <label htmlFor="login-email">Email:</label>
                        <input
                            type="email"
                            id="login-email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="login-password">Пароль:</label>
                        <input
                            type="password"
                            id="login-password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit" className="submit-btn">Войти</button>
                </form>
            </div>
            <div className={`form-container ${isLogin ? 'hidden' : ''}`}>
                <form className="auth-form" onSubmit={handleSubmit}>
                    <h2>Регистрация</h2>
                    <div className="form-group">
                        <label htmlFor="register-name">Имя:</label>
                        <input
                            type="text"
                            id="register-name"
                            name="name"
                            value={formData.name}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="register-surname">Фамилия:</label>
                        <input
                            type="text"
                            id="register-surname"
                            name="surname"
                            value={formData.surname}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="register-username">Имя пользователя:</label>
                        <input
                            type="text"
                            id="register-username"
                            name="username"
                            value={formData.username}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="register-email">Email:</label>
                        <input
                            type="email"
                            id="register-email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="register-password">Пароль:</label>
                        <input
                            type="password"
                            id="register-password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit" className="submit-btn">Зарегистрироваться</button>
                </form>
            </div>
        </div>
    );
};

export default Auth;
