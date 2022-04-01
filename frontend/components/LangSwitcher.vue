<template>
  <div class="lang">
    <div class="row lang-selected">
      <div class="lang-flag">
        <base-icon>
          <icon-russian-flag />
        </base-icon>
      </div>
      <div class="lang-arrow">
        <base-icon width="14" height="8" view-box="0 0 14 8" fill="none">
          <icon-stroked-arrow />
        </base-icon>
      </div>
    </div>
    <div class="lang-toggle">
      <a href="#" class="lang-flag">
        <base-icon>
          <icon-russian-flag />
        </base-icon>
      </a>
      <a href="#" class="lang-flag">
        <base-icon>
          <icon-american-flag />
        </base-icon>
      </a>
    </div>
  </div>
</template>

<script>
  import BaseIcon from "./BaseIcon";
  import IconRussianFlag from "./icons/IconRussianFlag"
  import IconAmericanFlag from "./icons/IconAmericanFlag"
  import IconStrokedArrow from "./icons/IconStrokedArrow"

  export default {
    components: {BaseIcon, IconRussianFlag, IconAmericanFlag, IconStrokedArrow}
  }
</script>
