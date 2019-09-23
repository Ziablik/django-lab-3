<template>
    <div class="Book">
        <Menu></Menu>
        <div style="font-size: 24pt; margin: 10px;">{{book.name}}</div>
        <div class="form">
            <label>Шифр: <input type="text" name="cipher" v-model="cipher"></label>
             <label>Зал: 
                <select v-model="room">
                  <option v-for="room in roomList" v-bind:value="room.id">
                      {{room.name}}
                  </option>
                </select>
            </label>
            <label>Дата регистрации: <input type="date" name="accounting_date" v-model="accounting_date"></label>


            <button @click="createCopy">Добавить экземпляр книги</button>
        </div>

        <p>{{msg}}</p>
    </div>
</template>

<script>
	import $ from 'jquery'
	import Menu from "@/components/Menu/Menu"

    export default {
        props: ['id'],
        components: {
        	Menu
        },
        data() {
        	return {
        		cipher: '',
                room: '',
                accounting_date: '',

                msg: '',
                roomList: '',
                book: '',
        	}
        },
        created() {
            $.ajax({
                url: "http://localhost:8000/api/book/" + this.id + '/',
                type: "GET",
                success: (resp) => {
                    this.book = resp
                },
                error: (resp) => {
                    // console.log(resp)
                },
            })
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
        methods: {
            checkForm: function (e) {
              if (this.cipher && this.room && this.accounting_date) {
                return true;
              }
            },
        	createCopy() {
                if (this.checkForm()) {
                    let data = {
                        book: this.id,
                        cipher: this.cipher,
                        room: this.room,
                        accounting_date: this.accounting_date,
                    }
                    
                    $.ajax({
                        url: "http://localhost:8000/api/copy/",
                        type: "POST",
                        data: data,
                        success: (resp) => {
                            console.log(resp)
                            this.msg = "экземпляр успешно добавлен"
                            // this.$emit('updatedata', true)
                        },
                        error: (resp) => {
                            console.log('errorrr')
                            this.msg = "Не удалось добавить экземпляр"
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