<template>
  <div>
    <client-only>
      <modal name="thanks" :scrollable="false" @closed="closeModal" width="415" height="auto">
        <div class="modal modal-thanks">
          <div class="modal-close" @click="closeModal">
            <base-icon width="28" height="28" viewBox="0 0 43 46" fill="none">
              <icon-plus/>
            </base-icon>
          </div>
          <div class="modal-title">Спасибо за подписку!</div>
          <button class="btn modal-btn">Продолжить обмен</button>
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
        this.$modal.hide('thanks');

        document.body.classList.remove('no-scroll');
        document.body.style.width = `${100}%`
      }
    }
  }
</script>
