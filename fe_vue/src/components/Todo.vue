<template>
  <div class="todo">
    <div class="m-3 create-todo">
      <button class="btn btn-primary text-bold" @click="createTodo">Create Todo</button>
      <span class="pagination" v-if="todo_list.length">
        <a href="#" @click="getPrevPage()">&laquo;</a>
        <a> {{ skip/10 +1 }}  of {{Math.round(total/this.limit +1)}}  Pages</a>
        <a href="#" @click="getNextPage()">&raquo;</a>
      </span>
    </div>
    <table class="table table-striped table-bordered text-center" v-if="todo_list.length">
      <thead>
        <tr>
          <th scope="col">No.</th>
          <th scope="col">Title</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody  >
        <tr v-for="(todo, index) of todo_list" :key="index">
          <td>{{index+1}}</td>
          <td>{{todo.title}}</td>
          <td>
            <button class="btn">
              <i class="material-icons" @click="editTodo(todo)">edit</i>
            </button>
            <button class="btn" @click="viewTodo(todo)">
              <i class="material-icons">remove_red_eye</i>
            </button>
            <button class="btn" @click="delete_todo(todo._id)">
              <i class="material-icons">delete_forever</i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-else style="text-align:center">
      <b>
        No Todo Exist! Please create One!
      </b>
    </div>

  <view-todo v-if="isViewTodo" :todo="selectedTodo"></view-todo>
  <snackbar ref="message" baseSize="100px" :holdTime="2000" :multiple="true"/>

  </div>
</template>

<script>
import { EventBus } from "../event-bus.js";
import AddTodo  from "./AddTodo.vue";
import ViewTodo  from "./ViewTodo.vue";
import EditTodo  from "./EditTodo.vue";
import TodoService from "../mixins/todo";

export default {
  name: "Todo",
  mixins: [TodoService],
  data() {
    return {
      todo_list: [],
      totalPages: 0,
      skip: 0,
      limit: 10,
      search: "",
      loading: false,
      total: 0,
      isViewTodo:false,
      selectedTodo:{'title':'', 'description':''}
    };
  },
  methods: {
    async delete_todo(id){
        try {
          let response = await this.deleteTodo({todo_id:id});
          if(response.status_id){
            this.$refs.message.open(response.message)
          } else {
            this.$refs.message.error(response.reason)
          }

        } catch (error) {
          this.$refs.message.error(error)
        }
        this.loadTodoList();
    },
    viewTodo(todo){
      this.isViewTodo = !this.isViewTodo;
      this.selectedTodo = todo
    },
    editTodo(todo){
      this.$router.push('/edit_todo/'+todo._id);
    },
    async loadTodoList() {
      this.loading = true;
      try {
        let response = await this.getTodoList(this.filters);
        this.todo_list = response.todo_list;
        this.total = response.total;
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
      // this.totalPages = res.data.total
    },
    getNextPage() {
      console.log("Next")
      if(this.total > this.skip + 10){
        this.skip = this.skip +10
        this.loadTodoList();
      }
    },
    getPrevPage() {
      if(this.skip - 10 >= 0){
        this.skip = this.skip -10
        this.loadTodoList();
      }
    },
    createTodo() {
      this.$router.push('/add_todo')
    }
  },
  mounted() {
    this.loadTodoList();
  },
  components: { AddTodo, ViewTodo },
  computed: {
    filters() {
      return {
        skip: this.skip,
        limit: this.limit
      };
    }
  }
};
</script>

<style scoped>
  .active {
    background-color: green;
    color: white;
  }
  .hide-arrow {
    visibility: hidden;
  }
  th:hover .sorting-icon {
    visibility: visible !important;
    cursor: pointer;
  }
  .sorting-icon {
    padding-right: 2px;
  }
  .text-bold {
    font-weight: bold;
  }
  .fs-14 {
    font-size: 14px !important;
  }
  .pointer {
    cursor: pointer;
  }
  #add-restaurant-button {
    position: relative;
    float: left;
    width: 200px;
  }
  .pagination {
    display: inline-block;
    float: right;
  }

  .pagination a {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
  }

  .pagination a.active {
    background-color: #4CAF50;
    color: white;
  }
  .create-todo {
    text-align: left;
  }
</style>
