import React, { useState, useRef, useEffect } from "react";
import { Search, User, FolderTree, BookOpen, Flame, Sun, Moon, Bell, Menu } from "lucide-react";
import "./Base.css";
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [theme, setTheme] = useState('light');
  const navRef = useRef(null);

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme');
    const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    const initialTheme = savedTheme || systemTheme;

    setTheme(initialTheme);
    document.documentElement.setAttribute('data-theme', initialTheme);
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  };

  useEffect(() => {
    if (navRef.current) {
      setNavHeight(navRef.current.offsetHeight);
    }
  }, []);

  const navLinks = [
    { title: 'Категории', path: "/categories", icon: <FolderTree size={20} /> },
    { title: 'Блог', path: "/users", icon: <BookOpen size={20} /> },
    { title: 'Форум', path: "/forum", icon: <Flame size={20} /> },
    { path: "/about", icon: <Search size={20} /> },
  ];

  return (
    <header className="header">
      <div className="main-nav">
        <div className="logo">LokkitcDev</div>

        <nav className={`nav-links ${isMenuOpen ? "active" : ""}`}>
          {navLinks.map((link, index) => (
            <Link key={index} to={link.path} className="nav-link">
              {link.icon}
              <span>{link.title}</span>
            </Link>
          ))}
        </nav>

        <div className="nav-actions">
          <button className="action-button theme-toggle" onClick={toggleTheme}>
            {theme === 'light' ? <Moon size={24} /> : <Sun size={24} />}
          </button>
          <button className="action-button">
            <User size={24} />
          </button>
        </div>


      </div>
      <div className="nav-actions-mobile">
        <div className="nav-actions-mobile-input">
          <input type="text" placeholder="Быстрый поиск" />
          <button className="search-button">
            <Search size={24} />
          </button>
        </div>
      </div>

    </header>
  );
};

const BottomMobileNavbar = () => {
  const mobileNavLinks = [
    { title: 'Закладки', path: "/bookmarks", icon: <BookOpen size={20} /> },
    { title: 'Каталог', path: "/catalog", icon: <FolderTree size={20} /> },
    { title: 'Главная', path: "/", icon: "ГМ" },
    { title: 'Уведомления', path: "/notifications", icon: <Bell size={20} /> },
    { title: 'Меню', path: "/menu", icon: <Menu size={20} /> }
  ];

  return (
    <div className="bottom-mobile-navbar">
      {mobileNavLinks.map((link, index) => (
        <Link key={index} to={link.path} className="nav-link">
          {typeof link.icon === 'string' ? (
            <div className="main-icon">{link.icon}</div>
          ) : (
            link.icon
          )}
          <span>{link.title}</span>
        </Link>
      ))}
    </div>
  );
};

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>LokkitcDev 2024</p>
      </div>
    </footer>
  );
};

export { Navbar, BottomMobileNavbar, Footer };
