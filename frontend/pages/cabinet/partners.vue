<template>
  <div class="full">
    <div class="cabinet-content">
      <tab-links :links="links" :active-tab="activeTab" @changeTab="changeTab"/>

      <div class="cabinet-body">
        <program v-if="activeTab === 1"/>
        <export v-else-if="activeTab === 2"/>
        <reward v-else/>
      </div>
    </div>
  </div>
</template>

<script>
  import TabLinks from "~/components/TabLinks";
  import Program from "~/components/cabinet/partners/Program";
  import Export from "~/components/cabinet/partners/Export";
  import Reward from "~/components/cabinet/partners/Reward";

  export default {
    components: {TabLinks, Program, Export, Reward},
    data() {
      return {
        activeTab: 1
      }
    },
    computed: {
      links() {
        return [
          {name: 'Партнерская программа'},
          {name: 'Реферальная ссылка и экспорт курсов'},
          {name: 'Партнерские вознаграждения'},
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
