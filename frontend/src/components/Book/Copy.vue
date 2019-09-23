<template>
    <div class="Book">
        <Menu></Menu>
        <div v-if="book">
        	<router-link tag="button" :to="{ name: 'copy_add', params: { id: book.id }}">Добавить копию</router-link>
	        <div style="font-size: 24pt">{{book.name}}</div>
	        <div>Всего копий {{book.copy_count}}</div>
	        <div>Копий зарегестрировано: {{copies.length}}</div></br>
	        <div v-if="copies" v-for="copy in copies">
	        	Книга {{copy.cipher}} находится в читательсокм зале {{copy.room.name}}
	        </div>

   		</div>
   		<div v-else>
   			Произошла ошибка
   		</div>
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
        		book: '',
        		copies: '',
        	}
        },
        created() {
        	this.getList()
        },
        methods: {
        	getList() {
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
        			url: "http://localhost:8000/api/book/" + this.id + '/copy/',
        			type: "GET",
        			success: (resp) => {
	        			this.copies = resp
	        			console.log(resp)
	        		},
	        		error: (resp) => {
	        			// console.log(resp)
	        		},
        		})
        	},
        }
    };
</script>


<style type="text/css">
	.book_card {
		margin: 10px;
		border: 3px solid #1b639b;
		padding: 10px;
		min-width: 400px;
		max-width: 600px;
	}
	.book_card .name{
		font-size: 18pt;
		margin: 8px;
	}
</style>