<template>
    <div>
    	<Menu></Menu>
    	Сайт библиотеки
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
        bookreaders_month: '',
        bookreaders_enought: '',
        readers: '',
        data: ''
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        $.ajax({
          url: "http://localhost:8000/api/work-table/",
          type: "GET",
          success: (resp) => {
            console.log(resp);
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
