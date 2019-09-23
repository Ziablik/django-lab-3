<template>
    <div class="Book">
        <Menu></Menu>
        <div class="form">
            <label>Шифр: <input type="text" name="cipher" v-model="cipher"></label>
            <label>Название книги: <input type="text" name="name" v-model="name"></label>
            <label>Автор книги: <input type="text" name="author" v-model="author"></label>
            <label>Год публикации: <input type="number" name="publication_year" v-model="publication_year"></label>
            <label>Издательство: <input type="text" name="publishing" v-model="publishing"></label>
            <label>Раздел: <input type="text" name="section" v-model="section"></label>
            <label>Количество экзепляров: <input type="number" name="copy_count" v-model="copy_count"></label>
            <button @click="createBook">Добавить книгу</button>
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
        components: {
        	Menu
        },
        data() {
        	return {
        		cipher: '',
                name: '',
                author: '',
                publishing: '',
                section: '',
                active: '',
                registration_date: '',
                copy_count: '',
                code: '',
                msg: '',
        	}
        },
        methods: {
            checkForm: function (e) {
              if (this.cipher && this.name && this.author && this.publication_year && this.publishing && this.section && this.copy_count) {
                return true;
              }
            },
        	createBook() {
                if (this.checkForm()) {
                    let data = {
                        cipher: this.cipher,
                        name: this.name,
                        author: this.author,
                        publication_year: this.publication_year,
                        publishing: this.publishing,
                        section: this.section,
                        copy_count: this.copy_count,
                    }
                    
                    $.ajax({
                        url: "http://localhost:8000/api/book/",
                        type: "POST",
                        data: data,
                        success: (resp) => {
                            this.msg = "Книга успешна добавлена"
                        },
                        error: (resp) => {
                            this.msg = "Не удалось добавить книгу"
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
