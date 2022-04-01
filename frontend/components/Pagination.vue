<template>
  <div class="row pag">
    <div class="pag-btn pag-prev">
      <base-icon fill="none">
        <icon-double-arrows/>
      </base-icon>
    </div>
    <div class="pag-btn active">1</div>
    <div class="pag-btn">2</div>
    <div class="pag-btn">3</div>
    <div class="pag-btn">4</div>
    <div class="pag-btn pag-next">
      <base-icon fill="none">
        <icon-double-arrows/>
      </base-icon>
    </div>
  </div>
</template>

<script>
  import BaseIcon from "./BaseIcon";
  import IconDoubleArrows from "./icons/IconDoubleArrows"

  export default {
    components: {BaseIcon, IconDoubleArrows}
  }
</script>
