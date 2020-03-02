<template>
<div id="background-design">
  <div class="form-container">
    <h1>Register!</h1>
    <form autocomplete="off">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" placeholder="Enter Name" v-model="name">
      </div>
      <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" placeholder="Enter username" v-model="username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password"  class="form-control" id="password" placeholder="Password" v-model="password">
      </div>
  
      <button @click="registerUser()" class="btn btn-primary">Register</button>
    </form>
    <router-link  style="margin: 0 auto;" to="/login"> Already a user? Login here </router-link>
  </div>
  <snackbar ref="error_message" baseSize="100px" :holdTime="2000" :multiple="true"/>
  <snackbar ref="success_message" baseSize="100px" :holdTime="2000" :multiple="true"/>
</div>
</template>

<script>
import UserService from '../mixins/users';
export default {
    name: 'Register',
    mixins:[UserService],
    data(){
      return{
        name: '',
        username:'',
        password:''
      }
    },
    methods:{
      async registerUser(){
        try {
          let response = await this.registeruser(this.user)
          if(response.status_id){
            this.$refs.success_message.open("User Registered Successfully");
            this.$router.push('/login')
          } else {
            this.$refs.error_message.error(response.reason);
          }
        } catch (error) {
          this.$refs.error_message.error("Cannot create user");
        }
      }
    },
    computed:{
      user(){
        return{
          name: this.name,
          username: this.username,
          password: this.password
        }
      }
    }

}
</script>

<style scoped>

form {
    display: grid;
    align-self: center;
    vertical-align: middle;
    width: 50%;
    margin: 0 auto;
}
h1 {
    text-align: center;
    margin: 20px;
    color: black;
}
label {
    color: black;
    font-weight: bold;
}

.form-group {
    width: 50%;
    margin: 20px auto;
}

button {
    width: 30%;
    margin: 25px auto;
}

a {
    color:blue;
    margin: 0 auto;
    display: grid;
    text-align: center; 
}
</style>