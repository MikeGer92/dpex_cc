<template>
  <div>
    <modal name="mainmodal" :scrollable="false" width="520px" height="auto">
      <div class="modal modal-mainmodal">
        <div class="modal-close" @click="closeModal">
          <base-icon width="28" height="28" viewBox="0 0 43 46" fill="none">
            <icon-plus />
          </base-icon>
        </div>

        <div v-if="paymentVisible">
          <div class="modal-title bank_title">ВЫБРАТЬ БАНК</div>
          <input
            type="text"
            id="FIO"
            v-model="fio"
            placeholder="Фамилия, Имя, Отчество"
          />
          <div class="input-error" v-if="inputError.length" v-bind="inputError">
            {{ inputError }}
          </div>
          <div class="modal-content">
            <div class="modal-choose-bank">
              <p>ВЫБЕРИТЕ БАНК ПОЛУЧАТЕЛЯ:</p>
            </div>
            <Loader v-if="bankLoading" />
            <div class="modal-bank-block">
              <div
                class="modal-bank-list"
                v-for="(bank, index) in banks"
                :key="`bank-item-${index}`"
              >
                <div class="bank-id">{{ index + 1 }}.</div>
                <div class="bank-name">
                  {{ bank.bank }}
                </div>
                <button
                  type="button"
                  class="modal-button"
                  @click="getBankData(bank)"
                >
                  Выбрать
                </button>
              </div>
            </div>

            <Loader v-if="invoiceLoading" />
          </div>
        </div>
        <div v-if="confirmVisible">
          <div class="modal-title">ВЫПОЛНИТЬ ПЕРЕВОД</div>

          <Loader v-if="propsLoading" />
          <div class="modal-content">
            <div class="payment-title">
              Переведите {{ bankprops.amount }} {{ bankprops.currency }} на
              карту по следующим реквизитам:
            </div>
            <div class="modal-payment-data">
              <div class="wrapp">
                <div class="modal-card-text">Сумма:</div>
                <div class="modal-card-num">
                  {{ bankprops.amount }} {{ bankprops.currency }}
                </div>
              </div>
              <div class="wrapp bank">
                <div class="modal-card-text">Банк:</div>
                <div class="modal-card-num">
                  {{ bankprops.bank }}
                </div>
              </div>
              <div class="wrapp card">
                <div class="modal-card-text">Карта:</div>
                <div class="modal-card-num">
                  {{ bankprops.card }}
                </div>
              </div>
            </div>
            <div class="margin-top30">
              Вы можете приложить изображение подверждающее оплату
            </div>
            <div class="scren-send">
              <div class="wrapp-screen">
                <div class="input__wrapper">
                  <input
                    name="file"
                    type="file"
                    id="input__file"
                    ref="input__file"
                    class="input input__file"
                    multiple
                    v-on:change="handleFileUpload()"
                  />
                  <label for="input__file" class="input__file-button">
                    <span class="input__file-icon-wrapper">
                      <img
                        class="input__file-icon"
                        src="@/assets/images/upFile.png"
                        alt="Выбрать файл"
                        width="25px"
                      />
                    </span>
                    <span class="input__file-button-text" v-if="file">
                      Выбран файл: {{ trimFileName }}
                    </span>
                    <span class="input__file-button-text" v-else>
                      Выберите файл
                    </span>
                  </label>
                </div>
              </div>
              <div class="conf-block">
                <button type="button" class="pay-end" @click="postDoneRequest">
                  Проведен
                </button>
              </div>
              <Loader v-if="invoiceLoading" />
            </div>
          </div>
        </div>
        <div class="result_modal" v-if="resultVisible">
          <div class="modal-title">РЕЗУЛЬТАТ ПЛАТЕЖА</div>

          <div class="result">
            <div class="errors" v-if="errors">
              <div
                class="error_descr"
                v-for="(error, index) in errors"
                :key="`error-${index}`"
              >
                {{ error }}
              </div>
            </div>
            <div class="success" v-if="status">
              <div class="modal-subtitle">ПЕРЕВОД УСПЕШНО ВЫПОЛНЕН</div>
              <div class="margin-top30">
                <p class="modal-description">
                  Вы можете скачать чек по
                  <a
                    :href="check_url"
                    target="_blank"
                    style="text-decoration: underline; cursor: pointer"
                    ><strong>ссылке</strong></a
                  >
                </p>
              </div>
              <div class="succes-billing">
                <img alt="check" src="~assets/images/checkList.png" />
              </div>
            </div>
            <Loader v-if="statusLoading" />
          </div>
        </div>
      </div>
    </modal>
  </div>
</template>

<script>
import BaseIcon from "../BaseIcon";
import IconPlus from "../icons/IconPlus";
import Loader from "~/components/Loader.vue";

export default {
  components: {
    BaseIcon,
    IconPlus,
    Loader,
  },
  props: {
    banks: {
      type: Array,
      // mock
      // default() {
      //   return [
      //     { bank: "sber", id: 1 },
      //     { bank: "vtb", id: 2 },
      //     { bank: "alfa", id: 3 },
      //   ];
      // }, // mock
      default: () => [],
    },
    bankprops: {
      type: Object,
      required: true,
      // mock
      // default() {
      //   return {
      //     bank: "vtb",
      //     card: "12345678901234",
      //     currency: "some",
      //   };
      // },
      // mock
      default() {
        return {};
      },
    },
    invoiceprops: {
      type: Object,
      required: true,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      bankLoading: false,
      propsLoading: false,
      invoiceLoading: false,
      statusLoading: false,
      paymentVisible: true, // default true
      confirmVisible: false,
      resultVisible: false,
      errors: [],
      successes: [],
      fio: "",
      invoice_id: "",
      token: "",
      scrPath: "/frontend/assets/images/",
      invReq: null,
      invoiceTimeout: null,
      status: true, // default null
      invData: null,
      inputError: "",
      file: null,
      check_link: null,

      bodyFormData: null,
    };
  },
  methods: {
    closeModal() {
      this.$modal.hide("mainmodal");
      document.body.classList.remove("no-scroll");
      document.body.style.width = `${100}%`;
    },
    getBankData(bank) {
      this.inputError = "";
      this.bankprops.bank = bank.bank;
      this.invoiceprops.ad_id = bank.id;
      this.invoiceprops.payment_info = this.fio;
      this.invReq = this.invoiceprops;
      this.checkFio(this.invReq);
    },

    checkFio(data) {
      if (this.fio) {
        this.invData = data;
        this.getInvoice(this.invData);
      } else {
        this.inputError = "Введите фамилию!";
      }
    },
    async getInvoice(data) {
      this.invoiceLoading = true;
      try {
        const response = await this.$axios.post("/api/grow/invoices", data);
        this.invoice_id = response.data.invoice_id;
        this.token = response.data.token;
        this.checkInvoiceStatus(this.token, this.invoice_id);
      } catch (e) {
        this.$toast.error(e.response.data);
      }
    },
    checkInvoiceStatus(token, invoice_id) {
      if (this.invoiceTimeout) {
        clearInterval(this.invoiceTimeout);
      }
      this.invoiceTimeout = setInterval(() => {
        this.getInvoiceStatus(token, invoice_id);
      }, 3000);
    },
    async getInvoiceStatus(token, invoice_id) {
      const data = {
        fiat_amount: "",
        fiat: this.invoiceprops.currency,
        crypto: this.invoiceprops.coin,
        fio: this.invoiceprops.payment_info,
        wallet_address: this.invoiceprops.address,
        token: token,
        invoice_id: invoice_id,
      };
      try {
        const response = await this.$axios.post(
          "/api/grow/invoices/status",
          data
        );
        if (response.data.data !== null) {
          clearInterval(this.invoiceTimeout);
          this.status = response.data.status;
          this.bankprops = response.data.data;
          this.invoiceLoading = false;
          this.paymentVisible = false;
          this.confirmVisible = true;
        }
      } catch (e) {
        this.$toast.error(e.response.data);
      }
    },
    postDoneRequest() {
      this.invoiceLoading = true;
      const data = new FormData();
      data.append("invoice_id", this.invoice_id);
      if (this.file) {
        data.append("file", this.file);
      }

      this.$axios({
        method: "post",
        url: "/api/grow/invoices/done",
        data: data,
        headers: {
          "Content-type": "multipart/form-data",
          accept: "application/json",
        },
      })
        .then((response) => {
          if (response.data) {
            this.status = response.data.status;
            this.successes = response.data;
            const data = {
              fiat_amount: this.bankprops.amount,
              fiat: this.invoiceprops.currency,
              crypto: this.invoiceprops.coin,
              fio: this.invoiceprops.payment_info,
              wallet_address: this.invoiceprops.address,
              invoice_id: this.invoice_id,
              token: this.token,
            };
            this.checkInvoiceResult(data);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    async getInvoiceStatusDone() {
      this.invoiceLoading = true;
      const data = {
        fiat_amount: this.bankprops.amount,
        fiat: this.invoiceprops.currency,
        crypto: this.invoiceprops.coin,
        fio: this.invoiceprops.payment_info,
        wallet_address: this.invoiceprops.address,
        invoice_id: this.invoice_id,
        token: this.token,
      };
      try {
        const response = await this.$axios.post(
          "/api/grow/invoices/done",
          data
        );
        this.status = response.data.status;
        this.successes = response.data;
        this.confirmVisible = false;
        this.resultVisible = true;
      } catch (e) {
        this.$toast.error(e.response.data);
      }
      this.invoiceLoading = false;
      this.checkInvoiceResult(data);
    },
    async getInvoiceResult(data) {
      try {
        const response = await this.$axios.post(
          "/api/grow/invoices/payed/status",
          data
        );
        if (response.data.status === "ready") {
          clearInterval(this.invoiceTimeout);
          this.status = response.data.status;
          this.check_url = response.data.check_url;
          this.statusLoading = false;
          this.confirmVisible = false;
          this.resultVisible = true;
          this.$toast("Оплата прошла успешно!");
        }
      } catch (e) {
        this.$toast("Ошибка проведения платежа");
      }
    },
    checkInvoiceResult(data) {
      if (this.invoiceTimeout) {
        clearInterval(this.invoiceTimeout);
      }
      this.invoiceTimeout = setInterval(() => {
        this.getInvoiceResult(data);
      }, 3000);
    },
    handleFileUpload() {
      this.file = this.$refs.input__file.files[0];
    },
  },
  computed: {
    trimFileName() {
      return this.file.name.replace(
        new RegExp("(^[^\\.]{" + 5 + "})[^\\.]+"),
        "$1"
      );
    },
  },
};
</script>

<style scoped>
#FIO {
  width: 90%;
  /* background: rgba(0, 0, 0, 0.08); */
  height: 56px;
  font-size: 20px;
  line-height: 132%;
  color: rgba(0, 0, 0, 0.64);
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-family: "Roboto-Regular", sans-serif;
  font-weight: 400;
}

.input-error {
  font-family: "Roboto-Regular", sans-serif;
  font-weight: 600;
  font-size: 20px;
  color: red;
  text-align: center;
}

.bank-id {
  padding-left: 24px;
}

.bank-name {
  text-align: left;
  padding-left: 24px;
  width: 200px;
}

button {
  width: 130px;
  height: 30px;
  border: 1px solid #000000;
  border-radius: 8px;
}

.wrapp-confirm {
  margin: 36px 36px;
  font-family: "Roboto-Regular", sans-serif;
  font-weight: 400;
  font-size: 20px;
  line-height: 132%;
}

.margin-top30 {
  margin-top: 30px;
}

.payment-title {
  margin-bottom: 30px;
}

.payment-data {
  padding-top: 19px;
}

.wrapp {
  display: flex;
  padding: 10px 0;
}

.cash-num,
.bank-name,
.card-num {
  padding-left: 20px;
}

.succes-billing {
  width: 100%;
  display: flex;
  justify-content: center;
}

.succes-billing > img {
  margin-top: 200px;
  margin-bottom: 20px;
}

.scren-send {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
}

.wrapp-screen {
  padding-top: 12px;
  display: flex;
  justify-content: space-between;
}

.conf-block {
  padding-top: 12px;
  display: flex;
}

.pay-end {
  width: 90%;
  height: 50px;
  background-color: #1b223d;
  border: 1px gray;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 500;
  font-size: 20px;
  line-height: 132%;
  color: white;
  overflow-x: hidden;
}

.wrapp-result {
  margin: 36px 36px;
}

.errors,
.success,
.success_descr,
.status {
  font-family: "Roboto-Regular", sans-serif;
  font-weight: 400;
  font-size: 20px;
  line-height: 132%;
}

.input__wrapper {
  width: 100%;
  display: flex;
  text-align: center;
}

.input__file {
  opacity: 0;
  visibility: hidden;
  position: absolute;
}

.input__file-icon-wrapper {
  height: 50px;
  width: 50px;
  margin-right: 15px;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}

.input__file-button-text {
  line-height: 1;
  margin: 1px 0 0 30px;
}

.input__file-button {
  width: 90%;
  height: 50px;
  /* background: #161616; */
  color: #1b223d;
  font-family: "Montserrat-Bold", sans-serif;
  /* font-size: 20px; */
  font-weight: 500;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
  border: 2px solid #1b223d;
  border-radius: 10px;
  cursor: pointer;
}

@media screen and (max-width: 767px) {
  /* .bank_title {
    margin-left: 12px;
  } */

  #FIO {
    width: 70%;
    padding: 8px;
    margin: 12px 12px 12px 1px;
  }

  .choose-bank {
    width: 70%;
    margin: 12px 6px;
  }

  .bank-id {
    padding-left: 0px;
  }

  .wrapp-confirm {
    margin: 12px 12px;
  }

  .input__file-button-text {
    line-height: 1;
    margin: 1px 0 0 0px;
  }

  .cash-num,
  .bank-name,
  .card-num {
    padding-left: 5px;
  }
}
</style>
