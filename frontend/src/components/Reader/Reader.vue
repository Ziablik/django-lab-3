<template>
    <div class="Reader">
    	<Menu></Menu>
        <div class="form">
            <label>Номер билета: <input type="text" name="number" v-model="number"></label>
            <label>Имя: <input type="text" name="firstname" v-model="firstname"></label>
            <label>Отчество: <input type="text" name="middlename" v-model="middlename"></label>
            <label>Фамилия: <input type="text" name="surname" v-model="surname"></label>
            <label>Номер паспорта: <input type="text" name="passport_number" v-model="passport_number"></label>
            <label>Дата рождения: <input type="date" name="birth_date" v-model="birth_date"></label>

            <label>Адресс: <input type="text" name="adress" v-model="adress"></label>
            <label>Номер телефона : <input type="tel" name="t_number" v-model="t_number" pattern="8[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}" placeholder="8___-___-__-__"></label>

            <label>Образование:
	            <select v-model="education">
		          <option value="s">Начальное</option>
		          <option value="s">Среднее</option>
		          <option value="s">Высшее</option>
		        </select>
		    </label>

            <label>Наличие ученой степени: <input type="checkbox" name="hasDegree" v-model="hasDegree"></label>


            <label>Зал: 
            	<select v-model="room">
		          <option v-for="room in roomList" v-bind:value="room.id">
		              {{room.name}}
		          </option>
		        </select>
            </label>


            <button @click="createReader">Добавить читателя</button>
        </div>
        <p>{{msg}}</p>
    </div>
</template>

<script>
	import $ from 'jquery'
	import Menu from "@/components/Menu/Menu"

    export default {
        props: {
        },
        data() {
        	return {
        		roomList: '',
        		number: '',
        		firstname: '',
        		middlename: '',
        		surname: '',
        		passport_number: '',
        		birth_date: '',
        		adress: '',
        		t_number: '',
        		education: '',
        		hasDegree: '',
        		room: '',
        		msg: '',
        	}
        },
        created() {
            $.ajax({
                url: "http://localhost:8000/api/room/",
                type: "GET",
                success: (resp) => {
                    this.roomList = resp
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
              if (this.number && this.firstname && this.middlename && this.surname && this.passport_number && this.birth_date && this.adress && this.t_number && this.education  && this.room) {
                return true;
              }
            },
        	createReader() {
                if (this.checkForm()) {
                    let data = {
                        number: this.number,
                        firstname: this.firstname,
                        middlename: this.middlename,
                        surname: this.surname,
                        passport_number: this.passport_number,
                        birth_date: this.birth_date,
                        adress: this.adress,
                        t_number: this.t_number,
                        education: this.education,
                        hasDegree: this.hasDegree,
                        room: this.room,
                    }
                    
                    $.ajax({
                        url: "http://localhost:8000/api/reader/",
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
