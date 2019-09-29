<template>
  <div class="Book">
    <Menu></Menu>
    <button @click="add" class="btn btn-dark" type="button">Добавить книгу</button>
    <div class="container-fluid">
      <div class="row">
        <div v-for="book in books" class="col-md-4">
          <div v-if="book.active" class="card text-white bg-success">
            <h5 class="card-header">
              Название книги: {{ book.name }}
            </h5>
            <div class="card-body">
              <p class="card-text">
                Автор: {{ book.author }}
              </p>
              <p class="card-text">
                Описание раздела: {{ book.section }}
              </p>
              <p class="card-text">
                Издательство: {{ book.publishing }}
              </p>
            </div>
            <div class="card-footer">
              Шифр: {{book.code}}
            </div>
            <div class="btn-group" role="group">
              <button class="btn btn-dark" type="button">
                <!--                Выдача книги-->
                <router-link :to="{ name: 'book-reader', params: { id: book.id, book:book }}">Выдача книги</router-link>
              </button>
              <button @click="bookDelete(book.id)" class="btn btn-dark" type="button">
                Списать книгу
              </button>
            </div>
          </div>
          <div v-else class="card text-white bg-danger">
            <h5 class="card-header">
              Название книги: {{ book.name }}
            </h5>
            <div class="card-body">
              <p class="card-text">
                Автор: {{ book.author }}
              </p>
              <p class="card-text">
                Описание раздела: {{ book.section }}
              </p>
              <p class="card-text">
                Издательство: {{ book.publishing }}
              </p>
            </div>
            <div class="card-footer">
              Шифр: {{book.code}}
            </div>
            <div class="btn-group text-center" role="group">
              <button @click="bookReturn(book.id)" class="btn btn-dark" type="button">
                Возврат книги
              </button>
              <button @click="bookDelete(book.id)" class="btn btn-dark" type="button">
                Списать книгу
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
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
        books: '',
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        $.ajax({
          url: "http://localhost:8000/api/book/",
          type: "GET",
          success: (resp) => {
            this.books = resp
          },
          error: (resp) => {
            // console.log(resp)
          },
        })
      },
      add() {
        this.$router.push({name: "book_add"})
      },
      bookReturn(pk) {
        $.ajax({
          url: "http://localhost:8000/api/book-return/",
          type: "POST",
          data: {
            id: pk,
          },
          success: (resp) => {
            this.getList()
          },
          error: (resp) => {
            console.log([resp, "Error"])
          },
        })
      },
      bookDelete(pk) {
        $.ajax({
          url: 'http://localhost:8000/api/book/',
          type: 'DELETE',
          data: {
            id: pk,
          },
          success: (resp) => {
            this.getList()
          },
          error: (resp) => {
            console.log([resp, "Error"])
          },
        })
      }
    }
  };
</script>
