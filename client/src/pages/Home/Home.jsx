import React from 'react';
import './Home.css';
const mangas = [
  {
    id: 1,
    title: 'One Piece adventure, comedy, action',
    description: 'The story of Monkey D. Luffy and his crew on a journey to find the One Piece treasure.',
    image: 'https://resizing.flixster.com/lEjBo6I5ghDk3u1TFpHbsMok0Sc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p186423_b_v9_ae.jpg',
    link: 'https://mangalib.me/one-piece',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 2,
    title: 'Naruto',
    description: 'The story of Naruto Uzumaki and his quest to become the strongest ninja in the world.',
    image: 'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
    link: 'https://mangalib.me/naruto',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 3,
    title: 'Attack on Titan',
    description: 'The story of Eren Yeager and his quest to defeat the Titans.',
    image: 'https://m.media-amazon.com/images/M/MV5BNzVjOWEwYjEtNDJhOC00YjUyLThjMWItMDQwZGY1ODM4YzI3XkEyXkFqcGc@._V1_.jpg',
    link: 'https://mangalib.me/attack-on-titan',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  }, {
    id: 4,
    title: 'One Piece',
    description: 'The story of Monkey D. Luffy and his crew on a journey to find the One Piece treasure.',
    image: 'https://resizing.flixster.com/lEjBo6I5ghDk3u1TFpHbsMok0Sc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p186423_b_v9_ae.jpg',
    link: 'https://mangalib.me/one-piece',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 5,
    title: 'Naruto',
    description: 'The story of Naruto Uzumaki and his quest to become the strongest ninja in the world.',
    image: 'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
    link: 'https://mangalib.me/naruto',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 6,
    title: 'Attack on Titan',
    description: 'The story of Eren Yeager and his quest to defeat the Titans.',
    image: 'https://m.media-amazon.com/images/M/MV5BNzVjOWEwYjEtNDJhOC00YjUyLThjMWItMDQwZGY1ODM4YzI3XkEyXkFqcGc@._V1_.jpg',
    link: 'https://mangalib.me/attack-on-titan',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  }, {
    id: 7,
    title: 'One Piece',
    description: 'The story of Monkey D. Luffy and his crew on a journey to find the One Piece treasure.',
    image: 'https://resizing.flixster.com/lEjBo6I5ghDk3u1TFpHbsMok0Sc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p186423_b_v9_ae.jpg',
    link: 'https://mangalib.me/one-piece',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 8,
    title: 'Naruto',
    description: 'The story of Naruto Uzumaki and his quest to become the strongest ninja in the world.',
    image: 'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
    link: 'https://mangalib.me/naruto',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 9,
    title: 'Attack on Titan',
    description: 'The story of Eren Yeager and his quest to defeat the Titans.',
    image: 'https://m.media-amazon.com/images/M/MV5BNzVjOWEwYjEtNDJhOC00YjUyLThjMWItMDQwZGY1ODM4YzI3XkEyXkFqcGc@._V1_.jpg',
    link: 'https://mangalib.me/attack-on-titan',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },{
    id: 10,
    title: 'One Piece',
    description: 'The story of Monkey D. Luffy and his crew on a journey to find the One Piece treasure.',
    image: 'https://resizing.flixster.com/lEjBo6I5ghDk3u1TFpHbsMok0Sc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p186423_b_v9_ae.jpg',
    link: 'https://mangalib.me/one-piece',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 11,
    title: 'Naruto',
    description: 'The story of Naruto Uzumaki and his quest to become the strongest ninja in the world.',
    image: 'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
    link: 'https://mangalib.me/naruto',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 12,
    title: 'Attack on Titan',
    description: 'The story of Eren Yeager and his quest to defeat the Titans.',
    image: 'https://m.media-amazon.com/images/M/MV5BNzVjOWEwYjEtNDJhOC00YjUyLThjMWItMDQwZGY1ODM4YzI3XkEyXkFqcGc@._V1_.jpg',
    link: 'https://mangalib.me/attack-on-titan',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  }, {
    id: 13,
    title: 'One Piece',
    description: 'The story of Monkey D. Luffy and his crew on a journey to find the One Piece treasure.',
    image: 'https://resizing.flixster.com/lEjBo6I5ghDk3u1TFpHbsMok0Sc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p186423_b_v9_ae.jpg',
    link: 'https://mangalib.me/one-piece',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 14,
    title: 'Naruto',
    description: 'The story of Naruto Uzumaki and his quest to become the strongest ninja in the world.',
    image: 'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
    link: 'https://mangalib.me/naruto',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 15,
    title: 'Attack on Titan',
    description: 'The story of Eren Yeager and his quest to defeat the Titans.',
    image: 'https://m.media-amazon.com/images/M/MV5BNzVjOWEwYjEtNDJhOC00YjUyLThjMWItMDQwZGY1ODM4YzI3XkEyXkFqcGc@._V1_.jpg',
    link: 'https://mangalib.me/attack-on-titan',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  }, {
    id: 16,
    title: 'One Piece',
    description: 'The story of Monkey D. Luffy and his crew on a journey to find the One Piece treasure.',
    image: 'https://resizing.flixster.com/lEjBo6I5ghDk3u1TFpHbsMok0Sc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p186423_b_v9_ae.jpg',
    link: 'https://mangalib.me/one-piece',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 17,
    title: 'Naruto',
    description: 'The story of Naruto Uzumaki and his quest to become the strongest ninja in the world.',
    image: 'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
    link: 'https://mangalib.me/naruto',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  },
  {
    id: 18,
    title: 'Attack on Titan',
    description: 'The story of Eren Yeager and his quest to defeat the Titans.',
    image: 'https://m.media-amazon.com/images/M/MV5BNzVjOWEwYjEtNDJhOC00YjUyLThjMWItMDQwZGY1ODM4YzI3XkEyXkFqcGc@._V1_.jpg',
    link: 'https://mangalib.me/attack-on-titan',
    rating: 4.5,
    status: 'ongoing',
    genres: ['action', 'adventure', 'comedy'],
    chapters: 1000,
    views: 1000000,
    favorites: 100000,
    comments: 1000,
    created_at: '2021-01-01',
  }

];


const Home = () => {
  const scrollLeft = () => {
    const grid = document.querySelector('.manga-grid');
    grid.scrollBy({ left: -400, behavior: 'smooth' });
  };

  const scrollRight = () => {
    const grid = document.querySelector('.manga-grid');
    grid.scrollBy({ left: 400, behavior: 'smooth' });
  };

  return (
    <div className="container">
      <div className="scroll-container">
        <button className="scroll-button left" onClick={scrollLeft}>
          ←
        </button>
        
        <div className="manga-grid">
          {mangas.map((manga) => (
            <div key={manga.id} className="manga-card">
              <div className="manga-image">
                <img src={manga.image} alt={manga.title} />
                <div className="manga-chapter">Глава {manga.chapters}</div>
              </div>
              <div className="manga-info">
                <h3 className="manga-title">{manga.title}</h3>
                <p className="manga-status">{manga.status}</p>
              </div>
            </div>
          ))}
        </div>
        
        <button className="scroll-button right" onClick={scrollRight}>
          →
        </button>

      
      </div>
    </div>
  );
};

export default Home;