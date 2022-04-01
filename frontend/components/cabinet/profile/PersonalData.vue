<template>
  <form class="cabinet-view">
    <h3 class="cabinet-subtitle">Персональные данные</h3>
    <div class="align-top inputs">
      <div class="input">
        <div class="input-placeholder">Имя:</div>
        <input type="text">
        <div class="input-icon">
          <base-icon width="18" height="18" view-box="0 0 18 18">
            <icon-edit/>
          </base-icon>
        </div>
      </div>
      <div class="input">
        <div class="input-placeholder">Email:</div>
        <input type="text">
        <div class="input-icon">
          <base-icon width="18" height="18" view-box="0 0 18 18">
            <icon-edit/>
          </base-icon>
        </div>
      </div>
      <div class="input">
        <div class="input-placeholder">Телефон:</div>
        <input type="text">
        <div class="input-icon">
          <base-icon width="18" height="18" view-box="0 0 18 18">
            <icon-edit/>
          </base-icon>
        </div>
      </div>
      <div class="row buttons">
        <button class="btn save">Сохранить</button>
        <div class="btn cancel">Отмена</div>
      </div>
    </div>
  </form>
</template>

<script>
  import BaseIcon from "~/components/BaseIcon";
  import IconEdit from "~/components/icons/IconEdit";

  export default {
    components: {BaseIcon, IconEdit}
  }
</script>
