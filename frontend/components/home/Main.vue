<template>
  <main class="main">
    <div class="wrapper">
      <div class="title main-title">
        <h3 class="significant significant-title">меняйте криптовалюты</h3>
        <h5>по самым выгодным тарифам</h5>
      </div>
      <form class="row main-form">
        <div class="main-block main-give">
          <Loader v-if="giveForm.loading" />
          <h3 class="main-subtitle main-subtitle-left">
            <span>отдаете</span>
          </h3>
          <div class="main-select">
            <v-select
              v-model="giveForm.data"
              class="style-chooser"
              :options="giveForm.currencies"
              label="name"
              :clearable="false"
              @option:selected="onGiveSelect"
              placeholder="Выбор валюты"
            >
              <template #option="{ label, icon }">
                <div class="main-row row">
                  <img :src="icon" :alt="label" />
                  <span>{{ label }}</span>
                </div>
              </template>
              <template id="givecurr" #selected-option="{ label, icon }">
                <div v-if="label" class="main-row row">
                  <img :src="icon" :alt="label" />
                  <span>{{ label }}</span>
                </div>
              </template>
            </v-select>
          </div>
          <div
            v-if="giveForm.data && giveForm.data.type === 'crypto'"
            class="main-page-input input"
          >
            <input
              v-model="giveForm.wallet"
              type="text"
              placeholder="Адрес кошелька"
            />
          </div>
          <div class="main-page-input input">
            <input
              v-model="giveForm.amount"
              :disabled="
                !receiveForm.data ||
                !giveForm.data ||
                !receiveForm.wallet.length
              "
              type="text"
              placeholder="Сумма"
              @input="onGiveAmountChange"
            />
            <div class="input-info">
              {{ giveForm.data ? giveForm.data.name : "" }}
            </div>
          </div>
          <div class="row video-instruction">
            <img
              alt="video instruction icon"
              src="~assets/images/videoIcon.png"
            />
            <div class="video-link">
              <a href="#" class="main-link"
                >Видеоинструкция к переводам с KYC
              </a>
              <a href="#" class="main-link"
                >Видеоинструкция к переводам без KYC
              </a>
            </div>
          </div>
        </div>

        <div class="main-exchange-icon">
          <icon-arrows @click="openMainModal()" />
        </div>

        <div class="main-block main-receive">
          <Loader v-if="receiveForm.loading" />
          <h3 class="main-subtitle"><span>получаете</span></h3>
          <div class="main-select">
            <v-select
              v-model="receiveForm.data"
              class="style-chooser"
              :options="receiveForm.currencies"
              label="name"
              :clearable="false"
              @option:selected="onReceiveSelect"
              placeholder="Выбор валюты"
            >
              <template #option="{ label, icon }">
                <div class="main-row row">
                  <img :src="icon" :alt="label" />
                  <span>{{ label }}</span>
                </div>
              </template>
              <template #selected-option="{ label, icon }">
                <div v-if="label" class="main-row row">
                  <img :src="icon" :alt="label" />
                  <span>{{ label }}</span>
                </div>
              </template>
            </v-select>
          </div>
          <div
            v-if="receiveForm.data && receiveForm.data.type === 'crypto'"
            class="main-page-input input"
          >
            <input
              v-model="receiveForm.wallet"
              :disabled="!receiveForm.data || !giveForm.data"
              type="text"
              placeholder="Адрес кошелька"
            />
          </div>
          <div class="main-page-input input">
            <input
              v-model="receiveForm.amount"
              readonly
              type="text"
              placeholder="Сумма"
            />
            <div class="input-info">
              {{ receiveForm.data ? receiveForm.data.name : "" }}
            </div>
          </div>
          <div
            v-if="receiveForm.buttons.length && receiveForm.wallet.length"
            class="buttons"
          >
            <button
              v-for="(button, index) in receiveForm.buttons"
              :key="`receive-button-${index}`"
              type="button"
              class="amount-btn"
              @click="checkLink(button.link)"
            >
              {{ button.label }}
            </button>
          </div>
        </div>
      </form>
      <MainModal
        :bankprops="bankdata"
        :banks="banks"
        :invoiceprops="invoiceData"
      />
      <Reserves
        @forMain="
          (title, val) => {
            getReserveItem(title, val);
          }
        "
      />
    </div>
  </main>
</template>

<script>
import IconArrows from "../icons/IconArrows";
import "vue-select/dist/vue-select.css";
import Loader from "~/components/Loader.vue";
import MainModal from "~/components/modals/MainModal.vue";
import Reserves from "~/components/home/Reserves.vue";

export default {
  components: { IconArrows, Loader, MainModal, Reserves },
  data() {
    return {
      giveForm: {
        currencies: [],
        data: null,
        amount: "",
        wallet: "",
        loading: false,
      },
      receiveForm: {
        currencies: [],
        data: null,
        amount: "",
        wallet: "",
        loading: false,
        buttons: [],
      },
      invoiceData: {
        ad_id: "",
        amount: "",
        coin: "",
        address: "",
        currency: "",
        payment_info: "",
      },
      bankdata: {
        amount: "",
        bank: "",
        card: "",
        currency: "",
      },
      amountTimeoutID: null,
      banks: [],
      icon: require("~/assets/images/no_image.png"),
      handleChoise: {
        currenciesG: "RUB",
        currenciesR: "",
      },
      handleCurrencies: null,
      currData: null,
      cryptoName: "",
      handleRecieve: null,
    };
  },
  mounted() {
    this.getGiveCurrencies();
    // this.$modal.show('mainmodal'); // to check modal
  },
  methods: {
    getGiveCurrencies() {
      this.giveForm.loading = true;
      this.$axios
        .get("/api/currencies/sell")
        .then((response) => {
          this.giveForm.currencies = response.data;
        })
        .catch((err) => {
          this.$toast.error(err.response.data);
        })
        .finally(() => {
          this.giveForm.loading = false;
        });
    },
    getReceiveCurrencies() {
      const params = {
        a: this.giveForm.data.name,
      };
      this.receiveForm.loading = true;
      this.$axios
        .get(`/api/currencies/buy`, { params })
        .then((response) => {
          this.receiveForm.currencies = response.data;
        })
        .catch((err) => {
          this.$toast.error(err.response.data);
        })
        .finally(() => {
          this.receiveForm.loading = false;
        });
    },
    openModal() {
      let wd = 17;
      if (window.innerWidth < 768) {
        wd = 0;
      }
      document.body.classList.add("no-scroll");
      document.body.style.width = `${window.innerWidth - wd}px`;
    },
    closeModal() {
      this.$modal.hide("mainmodal");
      document.body.classList.remove("no-scroll");
      document.body.style.width = `${100}%`;
    },
    openMainModal() {
      this.openModal();
      this.$modal.show("mainmodal");
    },
    onGiveSelect() {
      this.giveForm.amount = "";
      this.giveForm.wallet = "";
      this.resetReceiveForm();
      this.getReceiveCurrencies();
    },
    resetReceiveForm() {
      this.receiveForm.data = null;
      this.receiveForm.currencies = [];
      this.receiveForm.buttons = [];
      this.receiveForm.amount = "";
      this.receiveForm.wallet = "";
    },
    onReceiveSelect() {
      this.receiveForm.wallet = "";
      this.receiveForm.amount = "";
      this.receiveForm.buttons = [];
      this.giveForm.amount = "";
    },
    onGiveAmountChange() {
      this.receiveForm.amount = "";
      this.receiveForm.buttons = [];
      if (this.amountTimeoutID) {
        clearTimeout(this.amountTimeoutID);
      }
      this.amountTimeoutID = setTimeout(() => {
        if (
          this.giveForm.data &&
          this.receiveForm.data &&
          this.giveForm.amount.length
        ) {
          this.getAmount();
        }
      }, 1000);
    },
    async getAmount() {
      this.receiveForm.loading = true;
      this.receiveForm.buttons = [];
      const data = {
        currency_a: {
          name: this.giveForm.data.name,
          label: "",
          icon: "",
          type: this.giveForm.data.type,
        },
        currency_b: {
          name: this.receiveForm.data.name,
          label: "",
          icon: "",
          type: this.receiveForm.data.type,
        },
        amount_a: this.giveForm.amount,
        amount_b: "",
        wallet_address: this.receiveForm.wallet,
      };
      try {
        const response = await this.$axios.post("/api/amount", data);
        this.receiveForm.buttons = response.data.buttons;
        this.receiveForm.amount =
          this.receiveForm.data.type === "fiat"
            ? response.data.amount_fiat
            : response.data.amount_crypto;

        this.invoiceData.amount = response.data.amount_fiat;
        this.invoiceData.coin = this.receiveForm.data.name;
        this.invoiceData.address = this.receiveForm.wallet;
        this.invoiceData.currency = this.giveForm.data.name;
        this.bankdata.amount = response.data.amount_fiat;
        this.bankdata.currency = this.giveForm.data.name;
        if (
          this.receiveForm.buttons.length &&
          this.receiveForm.buttons[0].link === ""
        ) {
          await this.getBanks(data);
        }
      } catch (e) {
        this.$toast.error(e.response.data);
      }
      this.receiveForm.loading = false;
    },
    checkLink(link) {
      if (link) {
        window.location.href = link;
      } else {
        this.openMainModal();
      }
    },
    async getBanks(data) {
      this.bankLoading = true;
      try {
        const response = await this.$axios.post("/api/grow/ads/list", data);
        this.banks = response.data;
      } catch (e) {
        this.$toast.error(e.response.data);
      }
      this.bankLoading = false;
    },
    getReserveItem(title, val) {
      this.getCryptoName(title);
      this.getHandleCurrencies(val);
    },
    getCryptoName(title) {
      let cryptObj = [
        { Bitcoin: "BTC" },
        { Tether: "USDT" },
        { "Tether non KYC": "USDT_TRC20" },
        { ETH: "ETH" },
      ];
      this.cryptoName = cryptObj.filter((item) => item[title])[0][title];
    },
    getHandleCurrencies(val) {
      this.giveForm.amount = "";
      this.giveForm.wallet = "";
      this.giveForm.data = this.giveForm.currencies.filter(
        (item) => item.name == val
      )[0];
      const params = {
        a: this.giveForm.data.name,
      };
      this.receiveForm.loading = true;
      this.$axios
        .get(`/api/currencies/buy`, { params })
        .then((response) => {
          this.receiveForm.currencies = response.data;
          this.handleRecieve = this.receiveForm.currencies.filter(
            (item) => item.name === this.cryptoName
          )[0];
          this.receiveForm.data = this.handleRecieve;
        })
        .catch((err) => {
          this.$toast.error("Произошла ошибка выбора валюты");
        })
        .finally(() => {
          this.receiveForm.loading = false;
        });
    },
  },
};
</script>

<style>
input::placeholder {
  color: rgba(0, 0, 0, 0.48) !important;
  font-family: "Montserat-Reqular", sans-serif;
  font-size: 16px;
}
.main-page-input {
  border-radius: 5px;
}
.main-page-input input:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
.buttons {
  display: flex;
  flex-direction: column;
}
.amount-btn {
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
.main-block {
  align-self: normal;
}
.video-link {
  margin-left: 20px;
  /* display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center; */
}
.video-link > a {
  display: inline-block;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>
