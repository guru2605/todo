import Vue from 'vue'
import Router from 'vue-router'
import Todo from '@/components/Todo'
import AddTodo from '@/components/AddTodo'
import EditTodo from '@/components/EditTodo'
import Login from '@/components/Login'
import Register from '@/components/Register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '',
      name: 'Todo',
      component: Todo
    },
    {
      path:'/add_todo',
      name:'AddTodo',
      component:AddTodo
    },
    {
      path:'/edit_todo/:todo_id',
      name:'EditTodo',
      component:EditTodo
    },
    {
      path:'/login',
      name:'Login',
      component:Login
    },
    {
      path:'/register',
      name:'Register',
      component:Register
    }
  ]
})
