<template>
  <div class="page cabinet">
    <page-info :link="currentLink"/>

    <div class="wrapper">
      <div class="align-top cabinet-row">
        <div class="cabinet-links">
          <nuxt-link v-for="link in profileNavigation" :key="link.name" class="row cabinet-link" :to="link.path">
            <base-icon>
              <g :is="link.icon"></g>
            </base-icon>
            <span>{{ link.name }}</span>
          </nuxt-link>
        </div>

        <NuxtChild/>
      </div>
    </div>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import BaseIcon from "../components/BaseIcon";
  import IconUser from "../components/icons/IconUser";
  import IconVerify from "../components/icons/IconVerify";
  import IconDeal from "../components/icons/IconDeal";
  import IconOrder from "../components/icons/IconOrder";
  import IconApi from "../components/icons/IconApi";

  export default {
    components: {PageInfo, BaseIcon, IconUser, IconVerify, IconDeal, IconOrder, IconApi},
    computed: {
      currentLink() {
        return {title: 'Профиль', path: '/cabinet'}
      },
      profileNavigation() {
        return [
          {name: 'Профиль', path: '/cabinet/profile', icon: 'icon-user'},
          {name: 'Верификация', path: '/cabinet/verify', icon: 'icon-verify'},
          {name: 'Партнерская программа', path: '/cabinet/partners', icon: 'icon-deal'},
          {name: 'Заявки на обмен', path: '/cabinet/requests', icon: 'icon-order'},
          {name: 'API', path: '/cabinet/api', icon: 'icon-api'},
        ]
      }
    }
  }
</script>
