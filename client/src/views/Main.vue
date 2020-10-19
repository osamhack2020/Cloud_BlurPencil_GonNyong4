<template>
  <div class="main">
	<div>
		<div class="recent-worked">
			<h2 class="recent-title">Recently work</h2>
			<div v-for="(i, idx) in workData" v-bind:key="idx" class="row worked-list">
				<div class="col-md-2">
					<img class="worked-image" v-bind:src="serverUrl + i.fileName"/>
				</div>
				<div class="col-md-8">
					{{ i.fileName }}
				</div>
				<div class="col-md-2">
					{{ i.workedAt }}
				</div>
				<!-- {{ i }} -->
			</div>
		</div>
		<!-- <b-button>Button</b-button>
		<b-button variant="danger">Button</b-button>
		<b-button variant="success">Button</b-button>
		<b-button variant="outline-primary">Button</b-button> -->
		<h1>Query</h1>

		<h2>userid: {{ $route.params.userid}}</h2>
		<h2>
			받아온것 : {{ workData }}
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
			workData : '',
			finduser : this.$route.params.userid
		}
	},
	created () {
		var userid = sessionStorage.getItem("userid");
		var skip = 0;	// 뛰어넘기	(default 0)
		var limit = 5;	// 개수	(default 5)
		var sort = -1;	// -1 최신순부터, 1 예전순부터 (default -1)
		
		this.$http.get(`/api/works/${userid}/?skip=${skip}&limit=${limit}&sort=${sort}`)
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
.main {
	padding: 5rem;
}
	
.worked-image {
	height: 5rem;
}
	
.recent-worked {
	text-align: left;
}
.recent-worked .recent-title {
	font-weight: 700;
}
.recent-worked .worked-list {
	padding: 1rem;
	vertical-align: center;
	align-items: center;
}
</style>
