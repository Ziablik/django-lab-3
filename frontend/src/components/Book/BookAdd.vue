<template>
  <div class="Book">
    <Menu></Menu>
    <div class="container-fluid pt-2">
      <div class="form">
        <label>Шифр: <input type="text" name="code" v-model="code"></label>
        <label>Название книги: <input type="text" name="name" v-model="name"></label>
        <label>Автор книги: <input type="text" name="author" v-model="author"></label>
        <label>Издательство: <input type="text" name="publishing" v-model="publishing"></label>
        <label>Раздел: <input type="text" name="section" v-model="section"></label>
        <label>Зал:
          <select v-model="room">
            <option v-for="room in roomList" v-bind:value="room.id">
              {{room.room_name}}
            </option>
          </select>
        </label>

        <button @click="createBook">Добавить книгу</button>
      </div>
    </div>

    <p>{{msg}}</p>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Menu from "@/components/Menu/Menu"

  export default {
    props: {},
    components: {
      Menu
    },
    data() {
      return {
        roomList: '',
        code: '',
        name: '',
        author: '',
        publishing: '',
        section: '',
        room: '',
        msg: '',
      }
    },
    created() {
      $.ajax({
        url: "http://localhost:8000/api/reading-rooms/",
        type: "GET",
        success: (resp) => {
          this.roomList = resp
          // console.log(resp)
        },
        error: (resp) => {
          // console.log(resp)
        },
      })
    },
    methods: {
      checkForm: function (e) {
        if (this.code && this.name && this.author && this.publishing && this.section) {
          return true;
        }
      },
      createBook() {
        if (this.checkForm()) {
          let data = {
            code: this.code,
            name: this.name,
            author: this.author,
            publishing: this.publishing,
            section: this.section,
          }

          $.ajax({
            url: "http://localhost:8000/api/book/",
            type: "POST",
            data: data,
            success: (resp) => {
              this.msg = "Книга успешна добавлена"
            },
            error: (resp) => {
              this.msg = "Не удалось добавить книгу"
            }

          })
        } else {
          this.msg = "Введены не все поля"
          console.log("Введены не все поля")
        }
      }
    }
  };
</script>

<style type="text/css">
  .form {
    display: flex;
    flex-direction: column;
    align-items: center;

  }
</style>
