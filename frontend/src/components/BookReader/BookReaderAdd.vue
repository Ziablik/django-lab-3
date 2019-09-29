<template>
  <div class="BookReader">
    <Menu></Menu>
    <div class="container-fluid pt-2">
      <div class="form">
        <label>Читатель:
          <select v-model="reader">
            <option v-for="reader in readerList" v-bind:value="reader.id">
              {{reader.surname}} {{reader.name}} {{reader.second_name}}
            </option>
          </select>
        </label>

        <button @click="createBookReader">Добавить читателя</button>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Menu from "@/components/Menu/Menu"

  export default {
    props: ['id'],
    data() {
      return {
        readerList: '',
        reader: '',
        'start_date': '',
      }
    },
    created() {
      var date = new Date()

      var dd = date.getDate();
      if (dd < 10) dd = '0' + dd;

      var mm = date.getMonth() + 1;
      if (mm < 10) mm = '0' + mm;

      var yy = date.getFullYear() % 100;
      if (yy < 10) yy = '0' + yy;
      this.start_date = '20'+yy + '-' + mm + '-' + dd;
      $.ajax({
        url: "http://localhost:8000/api/readers/",
        type: "GET",
        success: (resp) => {
          this.readerList = resp
        },
        error: (resp) => {
        },
      })
    },
    components: {
      Menu
    },
    methods: {
      checkForm: function (e) {
        if (this.reader) {
          return true;
        }
      },
      createBookReader() {
        if (this.checkForm()) {
          let data = {
            reader: this.reader,
            book: this.id,
            start_date: this.start_date,
          }

          $.ajax({
            url: "http://localhost:8000/api/book-reader/",
            type: "POST",
            data: data,
            success: (resp) => {
              this.$router.push({name: "book"})
            },
            error: (resp) => {
              console.log('errorrr')
              this.msg = "Не удалось выдать книгу"
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
