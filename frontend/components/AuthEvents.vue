<template>
  <div class="events">
    <div class="row">
      <button class="event login" @click="openLogin">Войти</button>
      <button class="event register" @click="openRegister">Регистрация</button>
    </div>
    <div v-if="false" class="row user">
      <div class="user-photo">
        <img src="/images/photo.jpg" alt="">
      </div>
      <div class="user-name">Руслан</div>

      <div class="user-toggle">
        <nuxt-link to="/cabinet/profile" class="user-link">Личный кабинет</nuxt-link>
        <div class="user-link">Выйти</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    components: {},
    methods: {
      openRegister() {
        this.openModal()
        this.$modal.show('register')
      },
      openLogin() {
        this.openModal()
        this.$modal.show('login')
      },
      openModal() {
        let wd = 17;
        if (window.innerWidth < 768) {
          wd = 0
        }
        document.body.classList.add('no-scroll');
        document.body.style.width = `${window.innerWidth - wd}px`
      },
    }
  }
</script>
