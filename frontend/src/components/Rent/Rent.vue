<template>
    <div class="Rent">
        <Menu></Menu>
        <div style="display:flex; justify-content: space-evenly;">
	        <div style="display: flex; flex-direction: column">
	        	Шифр книги
	        	<input type="text" name="" v-model="copy_cypher">
	        	<button @click="findCopy">Найти</button>
	        	<div v-if="copy">
	        		<div>Найдена книга "{{copy.book.name}}"</div>
	        	</div>
	        	<div v-else>
	        		Такой книги нет
	        	</div>
	        </div>
	        <div style="display: flex; flex-direction: column">
	        	Читательский билет
	        	<input type="text" name="" v-model="reader_number">
	        	<button @click="findReader">Найти</button>
	        	<div v-if="reader">
	        		<div>Найден читатель {{reader.firstname[0]}}.{{reader.middlename[0]}}.{{reader.surname}}</div>
	        	</div>
	        	<div v-else>
	        		Читатель не найден
	        	</div>
	        </div>
        </div>
        <div v-if="copy && reader">
        	Дата возврата <input type="date" name="" v-model="return_date">
        	<button @click="rentCopy">Выдать книгу</button>
        </div>
        {{msg}}
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
        		copy_cypher: '',
        		reader_number: '',
        		copy: '',
        		reader: '',
        		return_date: '',
        		msg: ''
        	}
        },
        methods: {
        	findCopy() {
        		$.ajax({
        			url: "http://localhost:8000/api/copy/?cypher=" + this.copy_cypher,
        			type: "GET",
        			success: (resp) => {
	        			this.copy = resp
	        		},
	        		error: (resp) => {
	        			// console.log(resp)
	        		},
        		})
        	},
        	findReader() {
        		$.ajax({
        			url: "http://localhost:8000/api/reader/?number=" + this.reader_number,
        			type: "GET",
        			success: (resp) => {
	        			this.reader = resp
	        		},
	        		error: (resp) => {
	        			// console.log(resp)
	        		},
        		})
        	},
        	rentCopy() {
        		let data = {
                    reader: this.reader.id,
                    book_copy: this.copy.id,
                    return_date: this.return_date,
                }

        		$.ajax({
	                url: "http://localhost:8000/api/rent/",
	                type: "POST",
	                data: data,
	                success: (resp) => {
	                    this.msg = "Книга выдана"
	                },
	                error: (resp) => {
	                    this.msg = "Не удалось выдать книгу"
	                }   

	            })
        	}

        }
    };
</script>
