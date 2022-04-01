<template>
  <header class="header">
    <div class="wrapper">
      <div class="row header-row">
        <div class="burger" @click="openMenu = true"><span/><span/><span/></div>

        <Logo/>

        <div class="row links">
          <nuxt-link v-for="link in links" :key="link.name" :to="link.path" class="link">{{ link.name }}</nuxt-link>
        </div>

        <!-- <lang-switcher/> -->

        <!-- <auth-events/> -->

        <div class="toggle-menu" :class="{active: openMenu}">

          <Logo/>

          <div class="toggle-close" @click="openMenu = false">
            <base-icon width="30" height="30" viewBox="0 0 43 46" fill="none">
              <icon-plus/>
            </base-icon>
          </div>

          <nuxt-link class="menu-link" v-for="link in links" :key="link.name" :to="link.path">{{ link.name }}
          </nuxt-link>

          <!-- <lang-switcher/> -->
        </div>
      </div>
    </div>
  </header>
</template>

<script>
  // import LangSwitcher from "./LangSwitcher";
  import Logo from "./Logo";
  import AuthEvents from "./AuthEvents";
  import {HOME} from "~/settings/const";
  import BaseIcon from "./BaseIcon";
  import IconPlus from "./icons/IconPlus"

  export default {
    components: { AuthEvents, Logo, BaseIcon, IconPlus},
    data() {
      return {
        openMenu: false
      }
    },
    computed: {
      links() {
        return HOME.links
      }
    }
  }
</script>
