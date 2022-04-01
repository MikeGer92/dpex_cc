<template>
  <div class="faq-item" :class="{'active': open}">
    <div class="align-top faq-head" @click="hideItem">
      <div class="faq-ask">
        {{ ask }}
      </div>
      <div class="faq-icon">
        <base-icon width="43" height="46" viewBox="0 0 43 46" fill="none">
          <icon-plus/>
        </base-icon>
      </div>
    </div>
    <transition name="fade">
      <div v-show="open" class="row faq-body">
        <div class="faq-text">
          {{ answer }}
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
  import BaseIcon from "../BaseIcon";
  import IconPlus from "../icons/IconPlus";

  export default {
    components: {BaseIcon, IconPlus},
    props: {
      ask: {
        type: String,
        default: '',
      },
      answer: {
        type: String,
        default: '',
      },
    },
    data() {
      return {
        open: false,
      };
    },
    methods: {
      hideItem() {
        this.open = !this.open;
      },
    },
  };
</script>
