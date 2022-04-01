<template>
  <div>
    <client-only>
      <modal name="login" :scrollable="false" @closed="closeModal" width="415" height="auto">
        <div class="modal modal-register">
          <div class="modal-close" @click="closeModal">
            <base-icon width="28" height="28" viewBox="0 0 43 46" fill="none">
              <icon-plus/>
            </base-icon>
          </div>
          <div class="modal-title">Войти в аккаунт</div>

          <form class="modal-form">
            <div class="input">
              <input type="text" placeholder="Эл. почта">
            </div>
            <div class="input">
              <input type="text" placeholder="Пароль">
            </div>
            <button class="btn modal-btn">Войти</button>
          </form>

          <div class="or"><span>или</span></div>

          <div class="join" @click="openRegister">
            Регистрация
          </div>
        </div>
      </modal>
    </client-only>
  </div>
</template>

<script>
  import BaseIcon from "../BaseIcon";
  import IconPlus from "../icons/IconPlus";

  export default {
    components: {BaseIcon, IconPlus},
    methods: {
      closeModal() {
        this.$modal.hide('login');

        document.body.classList.remove('no-scroll');
        document.body.style.width = `${100}%`
      },
      openRegister() {
        this.closeModal();
        this.$modal.show('register')
      }
    }
  }
</script>
