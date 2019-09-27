<template>
  <div class="Book">
    <Menu></Menu>
    <button @click="add" class="btn btn-dark" type="button">Добавить книгу</button>
    <div class="container-fluid">
      <div class="row">
        <div v-for="book in books" class="col-md-4">
          <div class="card text-white bg-success">
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
          </div>
          <div class="btn-group" role="group">
              <button v-if="book.active" @click="addBookReader(book.id)" class="btn btn-dark" type="button">
                Выдача книги
              </button>
              <button v-else class="btn btn-dark" type="button">
                Возврат книги
              </button>
              <button class="btn btn-dark" type="button">
                Списать книгу
              </button>
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
        books: ''
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
      addBookReader(pk){
        this.$router.push({name: "book-reader", props:pk})
      }
    }
  };
</script>
