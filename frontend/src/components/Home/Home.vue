<template>
  <div class="Home">
    <Menu></Menu>
    <div class="container-fluid pt-2">
      <div class="row">
        <div class="col-md-6">
          <div class="jumbotron card card-block">
            <h2>
              Список читателей взявших книгу более месяца назад
            </h2>
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-12">
                  <table class="table table-bordered table-striped table-dark">
                    <thead>
                    <tr>
                      <th>
                        #
                      </th>
                      <th>
                        ФИО
                      </th>
                      <th>
                        Читательский билет
                      </th>
                      <th>
                        Книга
                      </th>
                      <th>
                        Дата закрепления книги
                      </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(bookreader, index) in bookreaders_month">
                      <td>
                        {{index + 1}}
                      </td>
                      <td>
                        {{ bookreader.reader.surname }}
                      </td>
                      <td>
                        {{ bookreader.reader.library_ticket }}
                      </td>
                      <td>
                        {{ bookreader.book.name }}
                      </td>
                      <td>
                        {{ bookreader.start_date }}
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <div class="jumbotron card card-block">
            <h2>
              Список читателей, взявших книги, количество экзепляров которых равно двум
            </h2>
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-12">
                  <table class="table table-bordered table-striped table-dark">
                    <thead>
                    <tr>
                      <th>
                        #
                      </th>
                      <th>
                        ФИО
                      </th>
                      <th>
                        Читательский билет
                      </th>
                      <th>
                        Книга
                      </th>
                      <th>
                        Дата закрепления книги
                      </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(bookreader, index) in bookreaders_enought">
                      <td>
                        {{index + 1}}
                      </td>
                      <td>
                        {{ bookreader.reader }}
                      </td>
                      <td>
                        {{ bookreader.reader.library_ticket }}
                      </td>
                      <td>
                        {{ bookreader.book.name }}
                      </td>
                      <td>
                        {{ bookreader.start_date }}
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

          </div>
        </div>
        <div class="col-md-6">
          <div class="jumbotron card card-block">
            <h2>
                          Список читателей младших 20 лет
            </h2>
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-12">
                  <table class="table table-bordered table-striped table-dark">
                    <thead>
                    <tr>
                      <th>
                        #
                      </th>
                      <th>
                        ФИО
                      </th>
                      <th>
                        Читательский билет
                      </th>
                      <th>
                        Дата рождения
                      </th>
                      <th>
                        Дата регистрации
                      </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(reader, index) in readers_json">
                      <td>
                        {{index +  1}}
                      </td>
                      <td>
                        {{ reader.fio }}
                      </td>
                      <td>
                        {{ reader.library_ticket }}
                      </td>
                      <td>
                        {{ reader.birthday }}
                      </td>
                      <td>
                        {{ reader.registration_date }}
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <div class="jumbotron card card-block">
            <h2>
              Соотношение читателей по образованию
            </h2>
            <vc-donut
              background="white" foreground="grey"
              :size="200" unit="px" :thickness="30"
              hasLegend legendPlacement="top"
              :sections="data_dgrm" :total="100"
            >
              <h1>100%</h1>
            </vc-donut>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
        </div>
        <div class="col-md-6">
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
        bookreaders_month: '',
        bookreaders_enought: '',
        readers_json: '',
        data_dgrm: '',
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
            console.log(resp[0].data_dgrm);
            this.bookreaders_month = resp[0].bookreaders_month;
            this.bookreaders_enought = resp[0].bookreaders_enought;
            this.readers_json = resp[0].readers_json;
            this.data_dgrm = resp[0].data_dgrm;

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
