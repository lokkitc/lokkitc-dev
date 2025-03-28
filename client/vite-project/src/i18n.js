import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources: {
      en: {
        translation: {
          nav: {
            home: 'HOME',
            users: 'USERS',
            categories: 'CATEGORIES',
            blog: 'BLOG',
            hotOffers: 'HOT OFFERS'
          },
          header: {
            openSource: 'YOU CAN USE MY OPEN SOURCE CODE FOR FREE'
          },
          search: {
            placeholder: 'Search users...',
            loading: 'Loading...',
            noResults: 'No results found'
          },
          languages: {
            english: 'ENGLISH',
            russian: 'RUSSIAN',
            kazakh: 'KAZAKH'
          }
        }
      },
      ru: {
        translation: {
          nav: {
            home: 'ГЛАВНАЯ',
            users: 'ПОЛЬЗОВАТЕЛИ',
            categories: 'КАТЕГОРИИ',
            blog: 'БЛОГ',
            hotOffers: 'ГОРЯЧИЕ ПРЕДЛОЖЕНИЯ'
          },
          header: {
            openSource: 'ВЫ МОЖЕТЕ ИСПОЛЬЗОВАТЬ МОЙ ОТКРЫТЫЙ КОД БЕСПЛАТНО'
          },
          search: {
            placeholder: 'Поиск пользователей...',
            loading: 'Загрузка...',
            noResults: 'Ничего не найдено'
          },
          languages: {
            english: 'АНГЛИЙСКИЙ',
            russian: 'РУССКИЙ',
            kazakh: 'КАЗАХСКИЙ'
          }
        }
      },
      kz: {
        translation: {
          nav: {
            home: 'БАСТЫ БЕТ',
            users: 'ПАЙДАЛАНУШЫЛАР',
            categories: 'САНАТТАР',
            blog: 'БЛОГ',
            hotOffers: 'ЫСТЫҚ ҰСЫНЫСТАР'
          },
          header: {
            openSource: 'СІЗ МЕНІҢ АШЫҚ БАСТАПҚЫ КОДЫМДЫ ТЕГІН ПАЙДАЛАНА АЛАСЫЗ'
          },
          search: {
            placeholder: 'Пайдаланушыларды іздеу...',
            loading: 'Жүктелуде...',
            noResults: 'Нәтиже табылмады'
          },
          languages: {
            english: 'АҒЫЛШЫН',
            russian: 'ОРЫС',
            kazakh: 'ҚАЗАҚ'
          }
        }
      }
    },
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;