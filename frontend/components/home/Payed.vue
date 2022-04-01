<template>
  <main class="main">
    <div class="wrapper">
      <div class="main-block">
        <Loader v-if="loading" />
        <h1 class="title main-title">
            Платеж успешно прошел
        </h1><br>
        <h3 v-if="!loading && link">Вы можете скачать чек по <a :href="link" target="_blank" style="text-decoration: underline;">ссылке</a></h3>
      </div>
    </div>
  </main>
</template>

<script>
  import 'vue-select/dist/vue-select.css';
  import Loader from '~/components/Loader.vue';

  export default {
    components: { Loader },
    mounted () {
      this.$axios.get(`/api/check?address=${this.$route.query.address}`)
          .then((response) => {
            this.link = response.data.link
          })
          .catch((err) => {
            this.$toast.error(err.response.data)
          })
          .finally(() => {
            this.loading = false
          })
    },
    data() {
      return {
        loading: true,
        link: null
      }
    },
    methods: {
    }
  }
</script>

<style>
</style>
