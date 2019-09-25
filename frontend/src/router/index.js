import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home/Home'
import Login from '@/components/Login/Login'

import Book from '@/components/Book/Book'
import BookAdd from '@/components/Book/BookAdd'
import Copy from '@/components/Book/Copy'
import CopyAdd from '@/components/Book/CopyAdd'

import Rent from '@/components/Rent/Rent'
import Return from '@/components/Rent/Return'
import Reader from '@/components/Reader/Reader'
import ReaderAdd from "../components/Reader/ReaderAdd";

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
      path: '/book/:id',
      name: 'copy',
      component: Copy,
      props: true,
    },
    {
      path: '/book/:id/add',
      name: 'copy_add',
      component: CopyAdd,
      props: true,
    },
    {
      path: '/rent',
      name: 'rent',
      component: Rent
    },
    {
      path: '/return',
      name: 'return',
      component: Return
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
  ]
})
