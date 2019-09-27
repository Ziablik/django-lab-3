<template>
  <div class="Book">
    <Menu></Menu>
    <button @click="add" class="btn btn-dark" type="button">Добавить книгу</button>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <table class="table table-bordered table-striped">
            <thead>
            <tr>
              <th>
                #
              </th>
              <th>
                ФИО
              </th>
              <th>
                Номер читательского билета
              </th>
              <th>
                Дата регистрации
              </th>
              <th>
                Кнопки управления
              </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(reader, index) in readers" class="table-success">
              <td>
                {{index + 1}}
              </td>
              <td>
                {{ reader.surname }} {{reader.second_name}} {{reader.first_name}}
              </td>
              <td>
                {{ reader.library_ticket }}
              </td>
              <td>
                {{ reader.registration_date }}
              </td>
              <td>
                <!--                                <a href="{% url 'active_books_reader' pk=reader.id %}">-->
                <button class="btn btn-secondary" type="button">
                  Книги
                </button>
                <!--                                </a>-->
                <!--                                {% if reader.active %}-->
                <!--                                <a href="{% url 'reader_delete' pk=reader.id %}">-->
                <button class="btn btn-secondary" type="button">
                  Удалить читателя
                </button>
                <!--                                </a>-->
                <!--                                {% endif %}-->
              </td>
            </tr>
            </tbody>
          </table>
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
        readers: ''
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        $.ajax({
          url: "http://localhost:8000/api/readers/",
          type: "GET",
          success: (resp) => {
            this.readers = resp
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
