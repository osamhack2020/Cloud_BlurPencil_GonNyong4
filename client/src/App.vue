<template>
  <div id="app">
    <div class ="child_1">
		<select-page/>
		
	</div>
    <div class = "child_2">
		<router-view/>	
	</div>
    </div>
</template>


<script>
import SelectPage from '@/components/SelectPage.vue'

export default {
  name: 'App',
  components: {
    SelectPage
  }
}
</script>
<style>
body{
	height: 100%;
    width: 100%;
    background-image: url(./images/background.jpg);
    background-position: center;
    background-size: cover;
}
#app {
  text-align: center;
  display : flex;   
}
	.child_1{
		flex : 1;
	}
	.child_2{
		flex : 9;
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
