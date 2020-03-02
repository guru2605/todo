<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
export default {
  name: "App",
  components: { NavBar },
  computed:{
    isLoggedIn(){
      return localStorage.getItem('token') || false
    }
  },
  mounted() {
    if(!this.isLoggedIn){
      if(!this.$route.path == '/login' || !this.$route.path == ''){
        this.$router.push('/login')
      }
    }
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
