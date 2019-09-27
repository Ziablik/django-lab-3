<template>
  <div class="ReaderAdd">
    <Menu></Menu>
    <div class="container-fluid pt-2">
      <div class="form">
        <label>Номер билета: <input type="text" name="library_ticket" v-model="library_ticket"></label>
        <label>Фамилия: <input type="text" name="surname" v-model="surname"></label>
        <label>Имя: <input type="text" name="first_name" v-model="first_name"></label>
        <label>Отчество: <input type="text" name="second_name" v-model="second_name"></label>
        <label>Номер паспорта: <input type="text" name="passport_number" v-model="passport_number"></label>
        <label>Дата рождения: <input type="date" name="birthday" v-model="birthday"></label>

        <label>Адресс: <input type="text" name="addr" v-model="addr"></label>
        <label>Номер телефона : <input type="tel" name="phone" v-model="phone"
                                       pattern="8[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}"
                                       placeholder="8___-___-__-__"></label>

        <label>Образование:
          <select v-model="education">
            <option v-for="education in educationList" v-bind:value="education.id">
              {{education.name}}
            </option>
          </select>
        </label>

        <label>Наличие ученой степени: <input type="checkbox" name="science_degree" v-model="science_degree"></label>


        <label>Зал:
          <select v-model="room">
            <option v-for="room in roomList" v-bind:value="room.id">
              {{room.room_name}}
            </option>
          </select>
        </label>


        <button @click="createReader">Добавить читателя</button>
      </div>
    </div>
    <p>{{msg}}</p>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Menu from "@/components/Menu/Menu"

  export default {
    props: {},
    data() {
      return {
        educationList: '',
        roomList: '',
        library_ticket: '',
        first_name: '',
        second_name: '',
        surname: '',
        passport_number: '',
        birthday: '',
        addr: '',
        phone: '',
        education: '',
        science_degree: '',
        room: '',
        msg: '',
      }
    },
    created() {
      $.ajax({
        url: "http://localhost:8000/api/reading-rooms/",
        type: "GET",
        success: (resp) => {
          this.roomList = resp
          // console.log(resp)
        },
        error: (resp) => {
          // console.log(resp)
        },
      })
      $.ajax({
        url: "http://localhost:8000/api/educations/",
        type: "GET",
        success: (resp) => {
          this.educationList = resp
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
        if (this.library_ticket && this.first_name && this.second_name && this.surname && this.passport_number && this.birthday && this.addr && this.phone && this.education && this.room) {
          return true;
        }
      },
      createReader() {
        if (this.checkForm()) {
          let data = {
            library_ticket: this.library_ticket,
            first_name: this.first_name,
            second_name: this.second_name,
            surname: this.surname,
            passport_number: this.passport_number,
            birthday: this.birthday,
            addr: this.addr,
            phone: this.phone,
            education: this.education,
            science_degree: this.science_degree,
            room: this.room,
          }

          $.ajax({
            url: "http://localhost:8000/api/readers/",
            type: "POST",
            data: data,
            success: (resp) => {
              this.msg = "Добавлен новый читатель!"
            },
            error: (resp) => {
              console.log('errorrr')
              this.msg = "Не удалось добавить"
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
