<template>
  <div class="Menu">
    <button @click="reader">Добавить читателя</button>
    <button @click="book">Книги</button>
    <button @click="rent">Выдача</button>
    <button @click="returner">Возврат</button>
    <button @click="logout">Выйти</button>
  </div>
</template>

<script>
  export default {
    props: {},
    methods: {
      reader() {
        this.$router.push({name: "reader"})
      },
      book() {
        this.$router.push({name: "book"})
      },
      rent() {
        this.$router.push({name: "rent"})
      },
      returner() {
        this.$router.push({name: "return"})
      },
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
