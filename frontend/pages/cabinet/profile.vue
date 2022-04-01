<template>
  <div class="full">
    <div class="cabinet-content">
      <tab-links :links="links" :active-tab="activeTab" @changeTab="changeTab"/>

      <div class="cabinet-body">
        <personal-data v-if="activeTab === 1"/>
        <alerts v-else-if="activeTab === 2"/>
        <password v-else/>
      </div>
    </div>
  </div>
</template>

<script>
  import TabLinks from "~/components/TabLinks";
  import PersonalData from "~/components/cabinet/profile/PersonalData";
  import Alerts from "~/components/cabinet/profile/Alerts";
  import Password from "~/components/cabinet/profile/Password";

  export default {
    components: {TabLinks, PersonalData, Alerts, Password},
    data() {
      return {
        activeTab: 1
      }
    },
    computed: {
      links() {
        return [
          {name: 'Личные данные'},
          {name: 'Уведомления'},
          {name: 'Пароль'},
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
