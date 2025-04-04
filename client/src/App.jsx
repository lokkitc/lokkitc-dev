import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar, Footer, BottomMobileNavbar } from './components/Base';
import Auth from './pages/Auth/Auth';

// Ленивая загрузка компонентов
const Users = lazy(() => import('./pages/User/Users'));
const Home = lazy(() => import('./pages/Home/Home'));
const Offers = lazy(() => import('./pages/Offers'));
const UserProfile = lazy(() => import('./pages/User/User-profile'));

function App() {
  return (
    <Router>
      <div className='main-container'>
        <Navbar />
        <main>
          <div className='container'>
            <Suspense fallback={<div>Загрузка...</div>}>
              <Routes>
                <Route path="/" element={<Home />} />
              <Route path="/users" element={<Users />} />
              <Route path="/offers" element={<Offers />} />
              <Route path="/users/:username" element={<UserProfile />} />
              <Route path="/auth" element={<Auth />} />
            </Routes>
          </Suspense>
          </div>
        </main>
        <BottomMobileNavbar />
        <Footer />
      </div>
    </Router>
  );
}

export default App;