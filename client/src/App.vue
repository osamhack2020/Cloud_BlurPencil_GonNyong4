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
    background-position: center;
    background-size: cover;
	/* background-color: white; */
}
#app {
  text-align: center; 
	height: 100%;
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
