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
}
#dashboard {
  text-align: center;
  display : flex;   
}
	.child_1{
		flex : 1.5;
		width : 15%;
	}
	.child_2{
		flex : 8.5;
		width : 85%;
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
