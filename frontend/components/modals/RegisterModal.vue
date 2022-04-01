<template>
  <div>
    <client-only>
      <modal name="register" :scrollable="false" @closed="closeModal" width="415" height="auto">
        <div class="modal modal-register">
          <div class="modal-close" @click="closeModal">
            <base-icon width="28" height="28" viewBox="0 0 43 46" fill="none">
              <icon-plus/>
            </base-icon>
          </div>
          <div class="modal-title">Регистрация</div>

          <form class="modal-form">
            <div class="input">
              <input type="text" placeholder="Имя и фамилия">
            </div>
            <div class="input">
              <input type="text" placeholder="Эл. почта">
            </div>
            <div class="input">
              <input type="text" placeholder="Пароль">
            </div>
            <div class="input">
              <input type="text" placeholder="Повторите пароль">
            </div>
            <button class="btn modal-btn">Зарегистрироваться</button>
          </form>

          <label class="align-top check">
            <input type="checkbox">
            <span class="row check-box"/>
            <span class="check-text">Нажимая кнопку «Войти» я принимаю условия пользовательского соглашения и согласен с политикой обработки персональных данных</span>
          </label>

          <div class="or"><span>или</span></div>

          <div class="join" @click="openLogin">
            Войти
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
        this.$modal.hide('register');
        document.body.classList.remove('no-scroll');
        document.body.style.width = `${100}%`
      },
      openLogin() {
        this.closeModal();
        this.$modal.show('login')
      }
    }
  }
</script>
