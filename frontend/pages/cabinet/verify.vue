<template>
  <div class="full">
    <div class="cabinet-content">
      <tab-links :links="links" :active-tab="activeTab" @changeTab="changeTab"/>

      <div class="cabinet-body">
        <div class="cabinet-view">
          <h3 class="cabinet-subtitle">Реквизиты</h3>
          <div class="cabinet-empty">
            У вас нет ни одного
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import TabLinks from "~/components/TabLinks";

  export default {
    components: {TabLinks},
    data() {
      return {
        activeTab: 1
      }
    },
    computed: {
      links() {
        return [
          {name: 'Электронные валюты'},
          {name: 'Пользователь'},
          {name: 'Все'},
        ]
      }
    },
    methods: {
      changeTab(index) {
        this.activeTab = index;
      }
    }
  }
</script>
