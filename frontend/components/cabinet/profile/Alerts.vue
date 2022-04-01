<template>
  <form class="cabinet-view">
    <h3 class="cabinet-subtitle">Уведомления</h3>
    <div class="row wrap">
      <label class="row check">
        <input type="checkbox">
        <span class="row check-box"/>
        <span class="check-text">Получать уведомления об изменении пароля</span>
      </label>
      <label class="row check">
        <input type="checkbox">
        <span class="row check-box"/>
        <span class="check-text">Получать уведомления о входе в мой аккаунт</span>
      </label>
    </div>
    <div class="inputs">
      <div class="row buttons">
        <button class="btn save">Сохранить</button>
        <div class="btn cancel">Отмена</div>
      </div>
    </div>
  </form>
</template>

<script>
  export default {}
</script>
