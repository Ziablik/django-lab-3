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
    props: {},
    data() {
      return {
        readerList: '',
        reader: '',
        book: ''
      }
    },
    created() {
      console.log(props);
      $.ajax({
        url: "http://localhost:8000/api/readers/",
        type: "GET",
        success: (resp) => {
          this.readerList = resp
          // console.log(resp)
        },
        error: (resp) => {
          // console.log(resp)
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
            book: '',
            reader: '',
          }

          $.ajax({
            url: "http://localhost:8000/api/readers/",
            type: "POST",
            data: data,
            success: (resp) => {
              this.msg = "Книга выдана"
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
