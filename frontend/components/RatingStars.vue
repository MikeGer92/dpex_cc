<template>
  <div ref="star" class="star">
    <div
      v-for="layer of starLayers"
      :key="layer"
      :class="`row star-${layer}`"
      :style="{ width: layer === 'front' ? width : 'initial' }"
    >
      <base-icon
        v-for="icon in 5"
        :key="icon"
        color="transparent"
        width="26"
        height="24"
        view-box="0 0 26 24"
      >
        <icon-star/>
      </base-icon>
    </div>
  </div>
</template>

<script>
  import BaseIcon from "./BaseIcon";
  import IconStar from "./icons/IconStar";

  export default {
    components: {BaseIcon, IconStar},
    props: {
      rating: {
        type: [Number, String],
        default: 0,
      },
    },
    data() {
      return {
        width: '0px',
        starLayers: [
          'back',
          'front',
        ],
      };
    },
    mounted() {
      const {star} = this.$refs;
      if (star) {
        this.width = `${(this.rating * star.clientWidth) / 5}px`;
      }
    },
  };
</script>
