<template>
  <div class="full">
    <div class="cabinet-content">
      <tab-links :links="links" :active-tab="activeTab" @changeTab="changeTab"/>

      <div class="cabinet-body">
        <Table />
      </div>
    </div>
  </div>
</template>

<script>
  import TabLinks from "~/components/TabLinks";
  import Table from "~/components/cabinet/requests/Table";

  export default {
    components: {TabLinks, Table},
    data() {
      return {
        activeTab: 1
      }
    },
    computed: {
      links() {
        return [
          {name: 'Все заявки'},
          {name: 'Текущие'},
          {name: 'Завершенные'},
          {name: 'Удаленные'},
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
