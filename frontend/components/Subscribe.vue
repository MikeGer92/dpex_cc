<template>
  <form class="subscribe" @submit.prevent="subscribe">
    <h2 class="subscribe-title">Подпишись на новости</h2>
    <div class="input">
      <input type="text" placeholder="Эл.почта">
      <button type="submit" class="input-btn" >
        <base-icon width="67" height="32" view-box="0 0 67 32" fill="none">
          <icon-submit-arrow/>
        </base-icon>
      </button>
    </div>
  </form>
</template>

<script>
  import BaseIcon from "./BaseIcon";
  import IconSubmitArrow from "./icons/IconSubmitArrow"

  export default {
    components: {BaseIcon, IconSubmitArrow},
    methods: {
      subscribe() {
        this.openModal();
        this.$modal.show('thanks');
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
