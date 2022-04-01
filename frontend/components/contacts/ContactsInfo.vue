<template>
  <div class="contacts-items">
    <div class="contacts-item">
      <div class="contacts-icon">
        <base-icon width="148" height="148" view-box="0 0 148 148" fill="#422E93">
          <icon-cloak/>
        </base-icon>
      </div>
      <div class="contacts-text">
        <p>Пн-Пт 11:00-23:00</p>
        <p>Сб-Вс Выходной</p>
      </div>
    </div>
    <div class="contacts-item">
      <div class="contacts-icon">
        <base-icon width="148" height="148" view-box="0 0 148 148" fill="#422E93">
          <icon-email/>
        </base-icon>
      </div>
      <div class="contacts-text">
        <a href="#">Support@DPex.com</a>
      </div>
    </div>
    <div class="contacts-item">
      <div class="contacts-icon">
        <base-icon width="148" height="148" view-box="0 0 148 148" fill="#422E93">
          <icon-phone/>
        </base-icon>
      </div>
      <div class="contacts-text">
        <a href="#">+380947100330</a>
      </div>
    </div>
  </div>
</template>

<script>
  import BaseIcon from "../BaseIcon";
  import IconCloak from "../icons/IconCloak";
  import IconEmail from "../icons/IconEmail";
  import IconPhone from "../icons/IconPhone";

  export default {
    components: {BaseIcon, IconCloak, IconEmail, IconPhone},
  }
</script>
