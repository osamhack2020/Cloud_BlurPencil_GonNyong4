<template>
  <div id="dashboard">
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
  name: 'Dashboard',
  components: {
    SelectPage
  }
}
</script>
<style>
body{
	width : 100%;
	height : 100%;
    background-image: url(../images/background.jpg);
    background-position: center;
    background-size: cover;
}
#dashboard {
  text-align: center;
  display : flex;   
}
	.child_1{
		flex : 1;
		width : 10%;
	}
	.child_2{
		flex : 9;
		width : 90%;
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
