<template>
  <div class="reserve">
    <div class="reserve-title">
      <div class="reserve-name">{{ reserve.title }}</div>
      <div class="reserve-icon">
        <img
          :src="require(`~/assets/images/${reserve.title.toLowerCase()}.png`)"
          alt=""
        />
      </div>
    </div>
    <div class="reserve-info">

        <div class="reserve-course">
          {{ reserve.courseRub }}
          <div class="row reserve-exchange">
            <span @click="getHandle(reserve.title, reserve.courseRub)"
              >Обменять</span
            >
            <base-icon width="14" height="8" view-box="0 0 14 8" fill="none">
              <icon-stroked-arrow />
            </base-icon>
          </div>
        </div>
        <div
          class="reserve-course"
          v-if="reserve.title != 'Tether non KYC'"
        >
          {{ reserve.courseUsd }}
          <div class="row reserve-exchange">
            <span @click="getHandle(reserve.title, reserve.courseUsd)"
              >Обменять</span
            >
            <base-icon width="14" height="8" view-box="0 0 14 8" fill="none">
              <icon-stroked-arrow />
            </base-icon>
          </div>
        </div>

    </div>
  </div>
</template>

<script>
import BaseIcon from "./BaseIcon";
import IconStrokedArrow from "./icons/IconStrokedArrow";
import IconUpArrow from "./icons/IconUpArrow";

export default {
  components: { BaseIcon, IconStrokedArrow, IconUpArrow },
  props: {
    reserve: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      val: "",
    };
  },
  methods: {
    getHandle(title, val) {
      if (val.includes("₽")) {
        val = "RUB";
      } else {
        val = "USD";
      }
      this.$emit("handleExchange", title, val);
    },
  },
};
</script>

<style scoped>

.exchange-btn {
  margin-top: 20px;
  width: 100%;
  height: 50px;
  background-color: black;
  border: 1px gray;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Roboto-Regular", sans-serif;
  font-weight: 400;
  font-size: 20px;
  line-height: 132%;
  color: white;
}
</style>
