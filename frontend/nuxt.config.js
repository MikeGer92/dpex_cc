export default {
  server: {
    port: 8000,
    host: '0.0.0.0'
  },
  target: 'static',
  head: {
    title: 'finTrade',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.png'}
    ]
  },

  css: [
    '@/assets/styles/main.less'
  ],
  plugins: [
    {src: '~/plugins/select.js'},
    {src: '~/plugins/modal.js'},
    {src: '~/plugins/loaderModule.js'},
    {
      src: '~/plugins/ymapPlugin.js',
      mode: 'client'
    }
  ],
  components: true,
  buildModules: [],
  modules: [
    '@nuxtjs/axios',
    'vue-toastification/nuxt'
  ],
  axios: {
    proxy: true
  },
  proxy: [
    'https://dpex.relabs.ru/api'
  ],
  build: {
  }
}
