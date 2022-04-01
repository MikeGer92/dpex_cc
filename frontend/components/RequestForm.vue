<template>
  <div>
    <Loader v-if="formLoading"/>
    <form class="request" id='request'>
      <div class="request-content">
        <h3 class="title request-title">{{ title }}</h3>

        <div class="input" >
          <input type="text" placeholder="Эл.почта" v-model="formData.email">
        </div>

        <div class="input">
          <input type="text" placeholder="Telegram" v-model="formData.telegram">
        </div>

        <div v-if="needQuestion" class="input">
          <textarea :placeholder="textareaPlaceholder"></textarea>
        </div>

        <button class="btn request-btn" :disabled="!isAccepted" @click="postFormData">
          Отправить
        </button>

        <label class="align-top check">
          <input type="checkbox" v-model="isAccepted">
          <span class="row check-box" />
          <span class="check-text">
            Нажимая кнопку «отправить» я принимаю условия пользовательского соглашения и согласен с политикой обработки персональных данных
          </span>
        </label>
      </div>
      <div class="request-image">
        <img src="~assets/images/form-bg.svg" :alt="title" class="request-bg">
        <img :src="image" :alt="title" class="request-pic">
      </div>
    </form>
  </div>
</template>

<script>
import Loader from './Loader.vue';
export default {
  components: {Loader},
  props: {
    title: {
      type: String,
      default: ''
    },
    image: {
      type: String,
      default: ''
    },
    needQuestion: {
      type: Boolean,
      default: false
    },
    textareaPlaceholder: {
      type: String,
      default: 'Ваш вопрос'
    }
  },
  data () {
    return {
      isAccepted: false,
      formData: {
        email: '',
        telegram: ''
      },
      formLoading: false
    }
  },
  methods: {
    postFormData(event) {
      event.preventDefault()
      if(this.formData.email.length &&  this.formData.telegram.length) {
        this.formLoading = true
        this.$axios.post('/api/feedback', this.formData)
          .then((response) => {
            if (response.data == '') {
              this.$toast.success('Данные успешно отправлены')
              this.formData.email = ''
              this.formData.telegram = ''
              this.formLoading = false
            }
          })
          .catch(function (error) {
            this.$toast.error('Произошла ошибка отравки данных')
          })


      } else {
        this.$toast.error('Вы не заполнили все поля формы')
      }
    }
  }
}
</script>
