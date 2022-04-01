export const HOME = {
  reviewsSlider: {
    slidesPerView: 3,
    spaceBetween: 24,
    pagination: {
      el: '.reviews-pagination',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1
      },
      768: {
        slidesPerView: 2
      },
      1024: {
        slidesPerView: 3
      }
    }
  },

  links: [
    { name: 'Правила обмена', path: '/rules' },
    { name: 'Партнерам', path: '/partners' },
    { name: 'Контакты', path: '/contacts' },
    { name: 'FAQ', path: '/faq' },
    // {name: 'Новости', path: '/news'}
  ]
};

export const NEWS = {
  items: [
    {
      title: 'В сети Ethereum произошел хардфорк London',
      description: '5 августа 2021. в сети  Ethereum произошел  хардфорк London...',
      image: '/images/news1.jpg'
    },
    {
      title: 'Добавлено новое направление обмена-Сбербанк RUB.',
      description: 'Наша команда продолжает вести работу над развитием сервиса. На этот...',
      image: '/images/news2.jpg'
    },
    {
      title: 'Обнавление дизайна',
      description: 'Команда DPex привествует своих клиентов, а также гостей сервиса! Последние...',
      image: '/images/news3.jpg'
    },
  ]
};
