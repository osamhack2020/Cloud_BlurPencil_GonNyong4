<template>
  <div class="main">
	<div>
		<!-- <b-button>Button</b-button>
		<b-button variant="danger">Button</b-button>
		<b-button variant="success">Button</b-button>
		<b-button variant="outline-primary">Button</b-button> -->
		<h1>Query</h1>

		<h2>userid: {{ $route.params.userid}}</h2>
		<h2>
			받아온것 : {{users}}
		</h2>
	</div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
	name: 'Main',
	props: {
		userid: {
			type: String,
            default : ''
		},
    },
	components: {
	// HelloWorld
	},
	data () {
		return {
			users : '',
			finduser : this.$route.params.userid
		}
	},
	created () {
		this.$http.post('/api/users/checkuser',{
			user: this.finduser
		}).then((response) => {
			this.users = response.data.data
		})
	}
}
</script>
<style>

</style>
