<template>
  <div class="Book">
    <Menu></Menu>
    <button @click="add">Добавить книгу</button>
    <div style="display: flex; align-items:center; flex-wrap:wrap;">
      <div v-for="book in books" class="book_card">
        <label class="name">{{book.name}}</label></br>
        <div style="display: flex;
							align-items: center;
							justify-content: space-evenly;">
          <div style="display: flex;
								flex-direction: column;">
            <label>Шифр: {{book.cipher}}</label>
            <label>Количество копий: {{book.copy_count}}</label>
          </div>
          <div style="display: flex;
								flex-direction: column;">
            <label>Автор: {{book.author}}</label>
            <label>Год издания: {{book.publication_year}}</label>
            <label>Издательство: {{book.publishing}}</label>
          </div>
        </div>
        <router-link :to="{ name: 'copy', params: { id: book.id, book:book }}">Перейти</router-link>
      </div>
    </div>
    <div class="container-fluid">
      <div class="row">
        <div v-for="book in books" class="col-md-4">
          <div class="card text-white bg-success">
            <h5 class="card-header">
              Название книги: {{ book.name }}
            </h5>
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <p class="card-text">
                    Автор: {{ book.author }}
                  </p>
                  <p>
                    Раздел: {{ book.section }}
                  </p>
                </div>
                <div class="col-md-6">
                  <p>Год издания: {{book.publication_year}}</p>
                  <p>Издательство: {{book.publishing}}</p>
                </div>
              </div>

            </div>
            <div class="card-footer">
              Шифр: {{book.cipher}}
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
      }
    }
  };
</script>


<style type="text/css">
  .book_card {
    margin: 10px;
    border: 3px solid #1b639b;
    padding: 10px;
    min-width: 400px;
    max-width: 600px;
  }

  .book_card .name {
    font-size: 18pt;
    margin: 8px;
  }
</style>
