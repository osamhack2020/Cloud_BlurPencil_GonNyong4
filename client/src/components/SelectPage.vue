<template>
  <div class="sidenav">
	<div class = "userwrap">
		<p class = "userinfo" v-html = "userdata"></p>
	</div>
	<div class = "menuwrap">
		<div v-if = "isUser" class = "sidemenu">
			<a href="/" v-on:click = "logout">Logout</a>
		</div>
		<div v-else class = "sidemenu">
			<router-link to="/">Login</router-link>
		</div>
		<div v-for="item in items" :key="item.link_to" class = "sidemenu" v-bind:class="{selected : item.isSelected}">
			<template>
				<router-link v-on:click.native="isSelected(item.title)" :to="item.link_to">{{item.title}}</router-link>
			</template>
		</div>
	</div>
    
	
  </div>
</template>

<script>

  const menuList = [
    { title: 'Upload', link_to: '/upload', isSelected : false},
    { title: 'Profile', link_to: '/profile',isSelected : false},
    { title: 'Main', link_to: '/main',isSelected : true},
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
		isSelected(item){
			for(var i =0;i<menuList.length;i++){
				if(menuList[i].title == item){
					menuList[i].isSelected = true;
				}
				else
					menuList[i].isSelected = false;
			}
		}
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
			this.userdata = response.data.data.user_id+''
		}).catch((err) =>{
			this.userdata = '로그인이 <br>필요합니다.';
			console.error(err);
		})
	}
  }

</script>

<style>
	.userwrap{
		font-size : x-large;
		font-weight : bold;	
		color : white;
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
		width: 15%;
		position: fixed;
		z-index: 1;
		top: 0;
		left: 0;
		background-color : #5f5fff;
		overflow-x: hidden;
		padding-top: 20px;
	}
	
	.sidemenu:hover{
		background-color : white;
	}
	.sidemenu{
		margin : 2vh;
	}
	.selected{
		
	}
	.menuwrap a, .dropdown-btn {
		padding: 6px 6px 6px 6px;
		text-decoration: none;
		font-size: 1.5vw;
		color: white;
		display: block;
		border: none;
		background: none;	
		width:100%;
		text-align: center;
		font-weight : bold;
		cursor: pointer;
		outline: none;
	}
	@media screen and (max-height: 450px) {
		.sidenav {padding-top: 15px;}
		.sidenav a {font-size: 18px;}
	}

	.sidenav a:hover, .dropdown-btn:hover {
		color: black;
		font-weight : normal;
	}
	.dropdown-container {
		display: none;
		background-color: #5eaf13;
		padding-left: 8px;
	}

</style>