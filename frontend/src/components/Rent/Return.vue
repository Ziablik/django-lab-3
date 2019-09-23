 <template>
    <div class="Rent">
        <Menu></Menu>
        <div style="display:flex; justify-content: space-evenly;">
	        <div style="display: flex; flex-direction: column">
	        	Читательский билет
	        	<input type="text" name="" v-model="reader_number">
	        	<button @click="findCopyByReader">Найти</button>
	        </div>
        </div>
        <div v-if="copies">
            <div style="font-size:20pt;">Читатель {{copies[0].reader.firstname[0]}}. {{copies[0].reader.middlename[0]}}. {{copies[0].reader.surname}}.</div>
            <div v-for="copy in copies" class="returnbook">
                <label>Книга {{copy.book_copy.book.name}} // Автор: {{copy.book_copy.book.author}}</label>
                <label>Шифр {{copy.book_copy.cipher}}</label>
                <label>Дата выдачи {{copy.date}}</label>
                <label>Дата необходимого возврата {{copy.return_date}}</label>
                <a @click="returnBook(copy.id)">Вернуть</a>
            </div>
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
        		reader_number: '',
        		msg: '',
                copies: '',
        	}
        },
        methods: {
        	findCopyByReader() {
        		$.ajax({
        			url: "http://localhost:8000/api/rent/?reader=" + this.reader_number,
        			type: "GET",
        			success: (resp) => {
	        			this.copies = resp
	        		},
	        		error: (resp) => {
	        			this.msg = "Книг не найдено"
	        		},
        		})
        	},
            returnBook(copy_id) {
                $.ajax({
                    url: "http://localhost:8000/api/rent/" + copy_id + "/?returner=1",
                    type: "GET",
                    success: (resp) => {
                        this.msg = "Книга возвращена"
                    },
                    error: (resp) => {
                        this.msg = "Не удалось вернуть книгу"
                    },
                })
            }

        }
    };
</script>

<style type="text/css">
    .returnbook {
        border: 2px solid #121212;
        padding: 8px;
        margin: 8px;
        display: flex;
        flex-direction: column;
        max-width: 400px;

    }
    .returnbook a {
        cursor: pointer;
        color: #1e66ae;
    }
</style>
