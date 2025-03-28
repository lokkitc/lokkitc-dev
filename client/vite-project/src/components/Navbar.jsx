import React, { useState, useRef, useEffect } from "react";
import { Search, User, Heart, ShoppingBag, Menu, X } from "lucide-react";
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from "react-icons/fa";
import "./Navbar.css";
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

const Navbar = () => {
  const { t, i18n } = useTranslation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [showResults, setShowResults] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const navRef = useRef(null);
  const searchTimeoutRef = useRef(null);
  const cachedResults = useRef(new Map());

  useEffect(() => {
    if (navRef.current) {
      setNavHeight(navRef.current.offsetHeight);
    }
  }, []);

  const navLinks = [
    { title: t('nav.home'), path: "/" },
    { title: t('nav.users'), path: "/users" },
    { title: t('nav.categories'), path: "/categories" },
    { title: t('nav.blog'), path: "/blog" },
    { title: t('nav.hotOffers'), path: "/offers" },
  ];

  const searchUsers = async (query) => {
    if (cachedResults.current.has(query)) {
      setSearchResults(cachedResults.current.get(query));
      setShowResults(true);
      return;
    }

    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/users/');
      if (!response.ok) throw new Error('Ошибка при получении пользователей');
      
      const data = await response.json();
      const filtered = data.filter(user => 
        user.name.toLowerCase().includes(query.toLowerCase()) ||
        user.surname.toLowerCase().includes(query.toLowerCase()) ||
        user.email.toLowerCase().includes(query.toLowerCase())
      );

      cachedResults.current.set(query, filtered);
      
      if (cachedResults.current.size > 20) {
        const firstKey = cachedResults.current.keys().next().value;
        cachedResults.current.delete(firstKey);
      }

      setSearchResults(filtered);
      setShowResults(true);
    } catch (error) {
      console.error('Ошибка при поиске:', error);
      setSearchResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  const debouncedSearch = (query) => {
    if (searchTimeoutRef.current) {
      clearTimeout(searchTimeoutRef.current);
    }

    if (query.length < 2) {
      setSearchResults([]);
      setShowResults(false);
      return;
    }

    searchTimeoutRef.current = setTimeout(() => {
      searchUsers(query);
    }, 300);
  };

  useEffect(() => {
    return () => {
      if (searchTimeoutRef.current) {
        clearTimeout(searchTimeoutRef.current);
      }
    };
  }, []);

  const handleSearchChange = (e) => {
    const query = e.target.value;
    setSearchQuery(query);
    debouncedSearch(query);
  };

  const handleUserSelect = async (userId) => {
    try {
      const response = await fetch(`http://localhost:8000/users/${userId}`);
      if (!response.ok) {
        throw new Error('Пользователь не найден');
      }
      setShowResults(false);
      setSearchQuery('');
    } catch (error) {
      console.error('Ошибка при получении пользователя:', error);
    }
  };

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (!event.target.closest('.search-bar')) {
        setShowResults(false);
      }
    };

    document.addEventListener('click', handleClickOutside);
    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, []);

  const handleLanguageChange = (event) => {
    const language = event.target.value;
    i18n.changeLanguage(language.toLowerCase());
  };

  return (
    <header className="header">
      <div className="top-bar">
        <div className="social-links">
          <div className="social-link-container">
            <a
              href="https://facebook.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaFacebook size={20} />
            </a>
          </div>
          <div className="social-link-container">
            <a
              href="https://twitter.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaTwitter size={20} />
            </a>
          </div>
          <div className="social-link-container">
            <a
              href="https://instagram.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaInstagram size={20} />
            </a>
          </div>
          <div className="social-link-container">
            <a
              href="https://linkedin.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaLinkedin size={20} />
            </a>
          </div>

          {/* <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
          <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
          <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a>
          <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a> */}
        </div>
        <div className="shipping-info">
          {t('header.openSource')}
        </div>
        <div className="language-currency">
          <select className="currency-select">
            <option value="USD">USD $</option>
            <option value="RUB">RUB ₽</option>
            <option value="KZT">KZT ₸</option>
          </select>
          <select 
            className="language-select" 
            onChange={handleLanguageChange}
            value={i18n.language.toUpperCase()}
          >
            <option value="EN">{t('languages.english')}</option>
            <option value="RU">{t('languages.russian')}</option>
            <option value="KZ">{t('languages.kazakh')}</option>
          </select>
        </div>
      </div>

      <div className="main-nav">
        <div className="logo">LokkitcDev</div>

        <div className="search-bar">
          <input
            type="text"
            placeholder={t('search.placeholder')}
            value={searchQuery}
            onChange={handleSearchChange}
          />
          <button className="search-button">
            <Search size={20} />
          </button>
          
          {showResults && (
            <div className="search-results">
              {isLoading ? (
                <div className="search-result-item">Загрузка...</div>
              ) : searchResults.length > 0 ? (
                searchResults.map((user) => (
                  <Link
                    key={user.user_id}
                    to={`/users/${user.user_id}`}
                    className="search-result-item"
                    onClick={() => {
                      setShowResults(false);
                      setSearchQuery('');
                    }}
                  >
                    <div>{user.name} {user.surname}</div>
                    <div className="search-result-email">{user.email}</div>
                  </Link>
                ))
              ) : (
                <div className="search-result-item">Ничего не найдено</div>
              )}
            </div>
          )}
        </div>

        <div className="nav-actions">
          <button className="action-button">
            <User size={24} />
          </button>
        </div>

        <button
          className="mobile-menu-button"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      <nav className={`nav-links ${isMenuOpen ? "active" : ""}`}>
        {navLinks.map((link, index) => (
          <Link key={index} to={link.path} className="nav-link">
            {link.title}
          </Link>
        ))}
      </nav>
    </header>
  );
};

export default Navbar;
