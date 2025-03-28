import React, { useState, useRef, useEffect } from "react";
import { Search, User, Heart, ShoppingBag, Menu, X } from "lucide-react";
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from "react-icons/fa";
import "./Navbar.css";
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const navRef = useRef(null);

  useEffect(() => {
    if (navRef.current) {
      setNavHeight(navRef.current.offsetHeight);
    }
  }, []);

  const navLinks = [
    { title: "HOME", path: "/" },
    { title: "USERS", path: "/users" },
    { title: "CATEGORIES", path: "/categories" },
    { title: "MEN'S", path: "/mens" },
    { title: "WOMEN'S", path: "/womens" },
    { title: "JEWELRY", path: "/jewelry" },
    { title: "PERFUME", path: "/perfume" },
    { title: "BLOG", path: "/blog" },
    { title: "HOT OFFERS", path: "/offers" },
  ];

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
          YOU CAN USE MY OPEN SOURCE CODE FOR FREE
        </div>
        <div className="language-currency">
          <select className="currency-select">
            <option value="USD">USD $</option>
            <option value="RUB">RUB ₽</option>
            <option value="EUR">KZT ₸</option>
          </select>
          <select className="language-select">
            <option value="EN">ENGLISH</option>
            <option value="RU">RUSSIAN</option>
            <option value="KZ">KAZAKH</option>
          </select>
        </div>
      </div>

      <div className="main-nav">
        <div className="logo">LokkitcDev</div>

        <div className="search-bar">
          <input
            type="text"
            placeholder="Search..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button className="search-button">
            <Search size={20} />
          </button>
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
