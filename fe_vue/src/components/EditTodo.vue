<template>
  <div class="add-todo mt-5 mb-3">
    <h3 >Edit Todo</h3>
    <form class="edit-todo-form">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title" aria-describedby="title" placeholder="Enter Title" v-model="todo.title">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" class="form-control" id="description" placeholder="Description" v-model="todo.description">
      </div>
      <button type="submit" class="btn btn-primary" @click="editTodo" v-if="isValid">Update Todo!</button>
      <button type="submit" class="btn btn-primary" @click="editTodo" v-else disabled>Update Todo!</button>
    </form>    
    <snackbar ref="message" baseSize="100px" :holdTime="2000" :multiple="true"/>

  </div>
</template>

<script>
import TodoService from "../mixins/todo.js";
export default {
  name: "EditTodo",
  mixins: [TodoService],
  data(){
      return {
          todo:{title:'', description:''}
      }
  },
  methods: {
    async editTodo(){
      let todo = {
        todo_id: this.todo._id,
        title: this.todo.title,
        description: this.todo.description
      }
      try {
        let response = await this.updateTodo(todo)
        if(response.status_id){
          this.$refs.message.open(response.message)
          setTimeout(() => {
              this.$router.push('/')
          }, 1000);
        } else{
          this.$refs.message.error(response.reason)
        }
      } catch (error) {
        this.$refs.message.error(error)
      }
    },
    async getTodo(){
        try {
            let response = await this.getTodoList({todo_id: this.todo_id})
            this.todo = response.todo_list[0]
        } catch (error) {
            console.log(error)
        }
    }
  },
  computed:{
    isValid(){
      return !this.todo.title.trim() == "" && !this.todo.description.trim() == ""
    }
  },
  mounted(){
      this.todo_id = this.$route.params.todo_id;
      this.getTodo();
  }
};
</script>

<style scoped>
.edit-todo-form{ 
  width: 50%;
  margin: 0 auto;
}
</style>
