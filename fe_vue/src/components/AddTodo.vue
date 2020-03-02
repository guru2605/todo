<template>
  <div class="add-todo mt-5 mb-3">
    <h3 >Add New Todo</h3>
    <form class="add-todo-form">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title" aria-describedby="title" placeholder="Enter Title" v-model="title">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" class="form-control" id="description" placeholder="Description" v-model="description">
      </div>
      <button type="submit" class="btn btn-primary" @click="createTodo" v-if="isValid">Create Todo!</button>
      <button type="submit" class="btn btn-primary" @click="createTodo" v-else disabled>Create Todo!</button>
    </form>    
    <snackbar ref="message" baseSize="100px" :holdTime="2000" :multiple="true"/>

  </div>
</template>

<script>
import TodoService from "../mixins/todo.js";
export default {
  name: "AddTodo",
  mixins: [TodoService],
  data() {
    return {
        title: "",
        description: ""
    };
  },
  methods: {
    async createTodo(){
      let todo = {
        title: this.title,
        description: this.description
      }
      try {
        let response = await this.storeTodo(todo)
        if(response.status_id){
          this.$refs.message.open(response.message)
          this.title = ""
          this.description = ""
        } else{
          this.$refs.message.error(response.reason)
        }
      } catch (error) {
        this.$refs.message.error(error)
      }
    }
  },
  computed:{
    isValid(){
      return !this.title.trim() == "" && !this.description.trim() == ""
    }
  }
};
</script>

<style scoped>
.add-todo-form{ 
  width: 50%;
  margin: 0 auto;
}
</style>
