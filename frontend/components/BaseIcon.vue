<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="width"
    :height="height"
    :viewBox="viewBox"
    role="presentation"
    class="svg-icon"
  >
    <g>
      <slot/>
    </g>
  </svg>
</template>

<script>
  export default {
    props: {
      height: {
        type: [String, Number],
        default: 24
      },
      width: {
        type: [String, Number],
        default: 24
      },
      viewBox: {
        type: [String, Number],
        default: '0 0 24 24'
      }
    }
  }
</script>
