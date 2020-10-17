<template>
  <div class="sidenav">
	<div class = "userwrap">
		<p class = "userinfo" v-html = "userdata"></p>
		<div class = "userprofile" v-if ="isUser">
			<img src= "../images/profile.png">
			<router-link class = "profile_text" to="/profile">profile</router-link>
		</div>
	</div>
	<div class = "menuwrap">
		<div v-if = "isUser" class = "sidemenu">
		<!-- <router-link v-on:click.native = "logout" to="/">Logout</router-link> -->
			<a href="/" v-on:click = "logout">Logout</a>
		</div>
		<div v-else class = "sidemenu">
			<router-link to="/login">Login</router-link>
		</div>
		<div v-for="item in items" :key="item.link_to" class = "sidemenu">
			<template v-if="item.link_to !== ''">
				<router-link :to="item.link_to">{{item.title}}</router-link>
			</template>
			<template v-else>
				<button @click="clickMenuBtn($event)" class="dropdown-btn">{{item.title}}</button>
				<div class="dropdown-container">
					<div v-for="subItem in item.sub_menu" :key="subItem.link_to">
				<router-link :to="subItem.link_to">{{subItem.title}}</router-link>
					</div>
				</div>
			</template>
		</div>
	</div>
    
	
  </div>
</template>

<script>

  const menuList = [
    { title: 'Upload', link_to: '/upload'},
    // { title: 'Test', link_to: '', sub_menu:
    //   [
    //     { title: 'Test1', link_to: '/test1' },
    //     { title: 'Test2', link_to: '/test2' },
    //     { title: 'Test3', link_to: '/test3' }
    //   ]
    // },
	// { title: 'Login', link_to: '/login'},
  ]
  export default {
    data(){
		return{
			items : menuList,
			userdata : '',
		}
    },
    methods: {
      clickMenuBtn: function(event) {
        if(event.target.nextElementSibling.style.display === 'none' ) {
          event.target.nextElementSibling.style.display = 'block';
        } else {
          event.target.nextElementSibling.style.display = 'none';
        }
      },
		logout(){
			sessionStorage.setItem("userid",'');
		},
    },
	computed :{
		isUser(){
			var userid = sessionStorage.getItem("userid");
			if(userid){
				return true;
			}
			return false
		},
		// userinfo(){
		// 	var userid = sessionStorage.getItem("userid");
		// 	if(userid){
		// 		return userid+'<br>님 환영합니다.'
		// 	}
		// 	else
		// 		return '로그인이 <br>필요합니다.';
		// }
	},
	created(){
		const userid = sessionStorage.getItem("userid");
		this.$http.get('/api/users?user_id='+userid)
			.then((response) => {
			this.userdata = response.data.data.user_id+'님<br>환영합니다.'
		}).catch((err) =>{
			this.userdata = '로그인이 <br>필요합니다.';
			console.error(err);
		})
	}
  }

</script>

<style>
	.userwrap{
		background-color : #796943;
		width : 6vw;
		height : 14vh;
		margin : 0 auto;
		border-radius : 8px;
		opacity: 0.6;
	}
	.userinfo{
		color : white;
		padding-top : 1.4vh;
	}
	.userprofile{
		width : fit-content;
		height : 3.5vh;
		margin : 0 auto;
		border : 2px solid white;
		border-radius : 6px;
	}
	.userprofile img{
		width : 15px;
		height : 15px;
		float : left;
		margin-top : 6px;
	}
	.profile_text{
		float : left;
		color : black;
	}
	.menuwrap{
		padding-top : 2.2vh;
	}
	.sidenav {
		height: 100%;
		width: 10%;
		position: fixed;
		z-index: 1;
		top: 0;
		left: 0;
		background-color: #262115;
		overflow-x: hidden;
		padding-top: 20px;
	}
	.sidemenu:hover{
		background-color : #898870;
	}

	.menuwrap a, .dropdown-btn {
		padding: 6px 6px 6px 6px;
		text-decoration: none;
		font-size: 1.5vw;
		color: #818181;
		display: block;
		border: none;
		background: none;
		width:100%;
		text-align: center;
		cursor: pointer;
		outline: none;
	}

	.menuwrap a:hover {
		color: #f1f1f1;
	}
	@media screen and (max-height: 450px) {
		.sidenav {padding-top: 15px;}
		.sidenav a {font-size: 18px;}
	}

	.sidenav a:hover, .dropdown-btn:hover {
		color: #f1f1f1;
	}
	.dropdown-container {
		display: none;
		background-color: #5eaf13;
		padding-left: 8px;
	}

</style>