<template>
  <div>
    <nav class="navbar navbar-dark bg-dark">
      <a class="navbar-brand">
          <h4 @click="$router.push('/')">
            My Todo Application
          </h4>
      </a>

      <form class="form-inline">
        <button v-if="isLoggedIn" class="btn btn-outline-primary my-2 my-sm-0 mr-3" @click="$router.push('/')"><b>Home</b></button>
        <button v-if="isLoggedIn" class="btn btn-outline-danger my-2 my-sm-0 mr-3" @click="logout"><b>Logout</b></button>
        <router-link class="btn btn-outline-primary my-2 my-sm-0 mr-3" to="/login" v-if="!isLoggedIn"><b>Login</b></router-link>
        <router-link class="btn btn-outline-success my-2 my-sm-0" to="/register" v-if="!isLoggedIn"><b>Register</b></router-link>
      </form>
    </nav>
  </div>
</template>

<script>
import { EventBus } from "../event-bus.js";

export default {
    computed: {
        isLoggedIn(){
            return localStorage.getItem('token') || false
        }
    },
    methods:{
      logout(){ 
        console.log('dsf')
        localStorage.removeItem('token');
        this.$router.push('/login');
        window.location.reload();
      }
    }
};
</script>

<style>
</style>