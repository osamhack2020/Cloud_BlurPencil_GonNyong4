<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
	<div>
		<login-page></login-page>
	</div>
  </div>
</template>

<script>
import LoginPage from '@/components/Login.vue'

export default {
  name: 'Home',
  components: {
    LoginPage
  }
}
</script>
<style>

</style>
