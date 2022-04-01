<template>
  <div class="reserves">
    <div class="wrapper">
      <h2 class="title reserves-title significant">АКТУАЛЬНЫЕ КУРСЫ</h2>
      <div class="align-top reserves-items">
        <reserve-item
          v-for="reserve in newReserves"
          :key="reserve.title"
          :reserve="reserve"
          @handleExchange="
            (title, val) => {
              listenReserveItem(title, val);
            }
          "
        />
      </div>
    </div>
  </div>
</template>

<script>
import ReserveItem from "../ReserveItem";

export default {
  data() {
    return {
      resReserve: null,
      newReserves: "",
      exchangeTimeout: "",
    };
  },
  mounted() {
    this.fetchReserves();
    this.getReservesRates();
  },
  components: { ReserveItem },
  methods: {
    getReservesRates() {
      this.exchangeTimeout = setInterval(() => {
        this.fetchReserves();
      }, 30000);
    },
    fetchReserves() {
      this.$axios
        .get("/api/rates")
        .then((response) => {
          this.resReserve = response.data;
          this.newReserves = [
            {
              title: "Bitcoin",
              courseRub: `₽${this.resReserve.btc.rub.toFixed(2)}`,
              courseUsd: `$ ${this.resReserve.btc.usd.toFixed(2)}`,
            },
            {
              title: "Tether",
              courseRub: `₽ ${this.resReserve.tether.rub.toFixed(2)}`,
              courseUsd: `$ ${this.resReserve.tether.usd.toFixed(2)}`,
            },
            {
              title: "Tether non KYC",
              courseRub: `₽${this.resReserve.tether_grow.rub.toFixed(2)}`,
              courseUsd: `$ ${this.resReserve.tether_grow.usd.toFixed(2)}`,
            },
            {
              title: "ETH",
              courseRub: `₽ ${this.resReserve.eth.rub.toFixed(2)}`,
              courseUsd: `$ ${this.resReserve.eth.usd.toFixed(2)}`,
            },
          ];
        })
        .catch((err) => {
          this.$toast.error(err.response.data);
        });
    },
    listenReserveItem(title, val) {
      console.log(title);
      this.$emit("forMain", title, val);
    },
  },
};
</script>

<style>
</style>
