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
			받아온것 : {{ workData }}
		</h2>
		<div v-for="(i, idx) in workData" v-bind:key="idx" >
			<img class="worked-image" v-bind:src="serverUrl + i.fileName"/>
			{{ i }}
		</div>
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
			workData : '',
			finduser : this.$route.params.userid
		}
	},
	created () {
		var userid = sessionStorage.getItem("userid");

		this.$http.get('/api/works?user_id=' + userid)
			.then((response) => {
				this.workData = response.data;
				if (this.workData.length > 0) {
					// 작업물이 한개 이상이라도 있으면
				}
			})
			.catch((err) =>{
				this.workData = err;
			})
	}
}
</script>
<style>
.worked-image {
	width: 100px;
}
</style>
