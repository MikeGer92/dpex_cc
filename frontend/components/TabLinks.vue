<template>
  <div class="align-bottom cabinet-head">
    <div class="cabinet-tab-link" v-for="(link, index) in links" :key="index"
         :class="{active: activeTab === (index + 1)}" @click="changeTab(index)">{{ link.name }}
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      links: {
        type: Array,
        default() {
          return []
        }
      },
      activeTab: {
        type: [String, Number],
        default: 1
      }
    },
    methods: {
      changeTab(index) {
        this.$emit('changeTab', index + 1);
      }
    }
  }
</script>
