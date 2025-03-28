import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';

// Ленивая загрузка компонентов
const Users = lazy(() => import('./pages/User/Users'));
const Home = lazy(() => import('./pages/Home/Home'));
const Offers = lazy(() => import('./pages/Offers'));

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <main>
          <Suspense fallback={<div>Загрузка...</div>}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/users" element={<Users />} />
              <Route path="/offers" element={<Offers />} />
            </Routes>
          </Suspense>
        </main>
      </div>
    </Router>
  );
}

export default App;