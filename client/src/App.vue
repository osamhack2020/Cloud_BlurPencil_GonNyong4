<template>
  <div id="app">
	<router-view></router-view>  
  </div>
</template>


<script>

export default {
  name: 'App',
  components: {
  }
}
</script>
<style>
body{
	
    background-image: url(./images/background.jpg);
    background-position: center;
    background-size: cover;
}
#app {
  text-align: center; 
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
