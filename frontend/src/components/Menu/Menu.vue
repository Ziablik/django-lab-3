<template>
  <div class="Menu">
    <button @click="work_table">Рабочий стол</button>
    <button @click="book">Книги</button>
    <button @click="book_add">Добавить книгу</button>
    <button @click="reader">Читатели</button>
    <button @click="reader_add">Добавить читателя</button>
<!--    <button @click="rent">Выдача</button>-->
<!--    <button @click="returner">Возврат</button>-->
    <button @click="logout">Выйти</button>
  </div>
</template>

<script>
  export default {
    props: {},
    methods: {
      work_table() {
        this.$router.push({name: "home"})
      },
      reader() {
        this.$router.push({name: "reader"})
      },
      reader_add() {
        this.$router.push({name: "reader_add"})
      },
      book() {
        this.$router.push({name: "book"})
      },
      book_add() {
        this.$router.push({name: "book_add"})
      },
      // rent() {
      //   this.$router.push({name: "rent"})
      // },
      // returner() {
      //   this.$router.push({name: "return"})
      // },
      logout() {
        localStorage.removeItem("token")
        this.$router.push({name: "login"})
      }
    },
  };
</script>

<style>
  .Menu {
    background-color: #121212;
  }

  button {
    font-style: 'Helvetica';
    font-size: 12pt;
    color: #dfdfdf;
    background-color: #121212;
    padding: 10px;
    margin: 6px;
    border-width: 0px;
    max-width: 200px;
  }

  button:hover {
    background-color: #1b639b;
    color: #ffffff;
  }
</style>
