<template>
<div id="background-design">
  <div class="form-container">
    <h1>Login!</h1>
    <form autocomplete="off">
      <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" placeholder="Enter username" v-model="username">
      </div>
      
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password"  class="form-control" id="password" placeholder="Password" v-model="password">
      </div>
  
      <button @click="loginUser" class="btn btn-primary">Login</button>
    </form>
    <router-link  style="margin: 0 auto;" to="/register"> Not a user? Register here </router-link>
  </div>
  <snackbar ref="error_message" baseSize="100px" :holdTime="2000" :multiple="true"/>

</div>
</template>

<script>
import loginService from '../mixins/users'
export default {
    name: 'Login',
    mixins:[loginService],
    data(){
      return {
        username:'',
        password:''
      }
    },
    methods:{
      async loginUser(){
        try {
          let response = await this.loginuser({'username': this.username, 'password': this.password})
          if(response.status_id ==1 ){
            this.storeToken(response.token)
          } else {
            this.$refs.error_message.error(response.reason)
          }
        } catch (error) {
            this.$refs.error_message.error(error.reason)
        }
      },
      storeToken(token){
        localStorage.setItem('token',token);
        this.$router.push('/');
        window.location.reload();
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