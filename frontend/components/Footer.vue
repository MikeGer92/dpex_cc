<template>
  <footer class="footer">
    <div class="wrapper">
      <div class="align-top footer-row">
        <div class="footer-logo">
          <Logo />
          <div class="description">
            <p>UAB "FinTrade Systems"</p>
            <p>Com. No. 306006721</p>
            <p>Vilnius, Švitrigailos g. 11K-109</p>
          </div>
        </div>

        <div class="row footer-links">
          <nuxt-link
            v-for="link in links"
            :key="link.name"
            :to="link.path"
            class="link"
            >{{ link.name }}</nuxt-link
          >
          <nuxt-link to="#" class="link">Правила и условия</nuxt-link>
          <nuxt-link to="#" class="link">Политика конфиденциальности</nuxt-link>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import Logo from "./Logo";
import { HOME } from "~/settings/const";

export default {
  components: { Logo },
  computed: {
    links() {
      return HOME.links;
    },
  },
};
</script>
