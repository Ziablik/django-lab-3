import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home/Home'
import Login from '@/components/Login/Login'

import Book from '@/components/Book/Book'
import BookAdd from '@/components/Book/BookAdd'

import Reader from '@/components/Reader/Reader'
import ReaderAdd from "../components/Reader/ReaderAdd";

import BookReaderAdd from "../components/BookReader/BookReaderAdd";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/book',
      name: 'book',
      component: Book
    },
    {
      path: '/book/add',
      name: 'book_add',
      component: BookAdd
    },
    {
      path: '/reader',
      name: 'reader',
      component: Reader
    },
    {
      path: '/reader/add',
      name: 'reader_add',
      component: ReaderAdd
    },
    {
      path: 'book/reader/add/:id',
      name: 'book-reader',
      component: BookReaderAdd,
      props: true,

    },
  ]
})
