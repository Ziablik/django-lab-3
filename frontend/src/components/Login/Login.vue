<template>
  <div>
    <input v-model="login" type="text" placeholder="Имя">
    <input v-model="password" type="password" placeholder="Пароль">
    <button @click="setLogin">Войти</button>

  </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        props: {
        },
        data() {
          return {
            login: '',
            password: '',
          }
        },
        created() {
          if (localStorage.getItem("token")) {
            $.ajaxSetup({
              headers: {'Authorization': "Token " + localStorage.getItem("token")},
            })
            this.$router.push({name: "home"})
          }
        },
        methods: {
          setLogin() {
            $.ajax({
              url: "http://localhost:8000/rest-auth/login/",
              type: "POST",
              data: {
                username: this.login,
                password: this.password,
              },
              success: (response) => {
                localStorage.setItem("token", response.key)
                this.$router.push({name: "home"})
              },
              error: (response) => {
                if (response.status === 400) {
                  console.log("Error")
                }
              }
            })
          }
        }
    };

</script>
