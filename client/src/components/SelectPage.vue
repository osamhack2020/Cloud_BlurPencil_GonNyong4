<template>
  <div class="sidenav">
	<div class = "logowrap">
		<img src="../images/logo(250x250).png" class="nav_logo"/>
	</div>
	<div class = "menuwrap">
		<!-- <button class="btn btn-primary rounded-pill fast-btn">
			<img src = "../images/upload_hov.svg" class = "menu_icon">
			Upload
		</button> -->
		<div v-for="item in items" :key="item.link_to" 
			class = "sidemenu" 
			v-bind:class="{selected : item.isSelected}"
			@click = "isSelected(item)"
		>	
			<img v-if = "item.isSelected" :src=item.icon_hov class="menu_icon">
			<img v-else :src="item.icon" class="menu_icon">
			<a class="menu_a">{{item.title}}</a>
		</div>
		
		<div class="bottom-menu" style="bottom:7rem; padding:1rem;">
			<div class="notice">
				공지하고자 하는 내용이 있다면 이런식으로
				<button class="btn" type="button" onclick="location.href='https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4'">바로가기</button>
			</div>
		</div>
		<div class = "sidemenu bottom-menu"
			v-if = "isUser"
			@click = "logout"	
		>
			<img src = "../images/sign-out.svg" class = "menu_icon">
			<a class="menu_a">Logout</a>
		</div>
	</div>
    
		
  </div>
</template>

<script>
  const menuList = [
    { title: 'Dashboard', link_to: '/main',isSelected : false,icon : require("../images/dashboard.svg"),icon_hov : require('../images/dashboard_hov.svg')},
    { title: 'Recent', link_to: '/recent', isSelected : false, icon : require('../images/current.svg'),icon_hov : require('../images/current_hov.svg')},
    { title: 'Profile', link_to: '/profile',isSelected : false,icon : require('../images/profile.svg'), icon_hov : require('../images/profile_hov.svg')},
    { title: 'Upload', link_to: '/upload', isSelected : false, icon : require('../images/upload.svg'),icon_hov : require('../images/upload_hov.svg')},
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
			alert("로그아웃 되었습니다.");
			sessionStorage.setItem("userid",'');
			this.$router.push('/');
		},
		isSelected(item){
			for(var i =0;i<menuList.length;i++){
				if(menuList[i].title == item.title){
					menuList[i].isSelected = true;
				}
				else
					menuList[i].isSelected = false;
			}
			this.selectmenu(item.link_to);
		},
		selectmenu(item){
			this.$router.push(item).catch(()=>{});
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
		var para = document.location.href.split("/");
		for(var i =0;i<menuList.length;i++){
			if(menuList[i].link_to == ('/'+para[3])){
				menuList[i].isSelected = true;
			}
		}

	}
  }

</script>

<style lang="scss">
	.nav_logo {
		width: 5rem;
	}
	.logowrap{
		font-size : x-large;
		font-weight : bold;	
		color : #0d112a;
		padding-top: 1rem;
		padding-bottom: 1rem;
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
		background-color : white;
		overflow-x: hidden;
		padding-top: 20px;
		-webkit-box-shadow: 5px 0px 12px -2px rgba(164,171,219,0.3);
		-moz-box-shadow: 5px 0px 12px -2px rgba(164,171,219,0.3);
		box-shadow: 5px 0px 12px -2px rgba(164,171,219,0.3);
	}
	.sidemenu{
		text-align : left;
		padding : 1.5vh 2vh 1.5vh 2vh;
		/* padding: 6px 6px 6px 6px; */	
		font-size: 18px;
		font-weight : 500;
		cursor : pointer;
		transition: background .5s;
	}
	@media (max-width: 1200px) {
		.sidemenu{
			/* font-size: 1.25vw; */
			padding : 1.5vh 1vh 1.5vh 1vh;
		}
		.menu_icon{
			margin-right : 1.25vh !important;
			margin-left : 1.25vh !important;
		}
	}
	@media (max-width: 992px) {
		.sidemenu{
			font-size: 1.5vw;
		}
	}
	@media (max-width: 768px) {
		.sidemenu { text-align: center;	}
	}
	.sidemenu:hover{
		background-color : #ebebff;
	}
	.sidemenu a{
		color : black;
	}
	.sidemenu a:hover{
		text-decoration: none;
		color : black;
	}
	.menu_icon{
		width : 1.6vw;
		margin-right : 1.8vh;
		margin-left : 1.8vh;
	}
	.selected {
		/* background: linear-gradient( to right, #3e0ecc, #7c60cd ); */
		background: linear-gradient( to right, #5f5fff, #5f5fff );
		/* background-color: #5f5fff; */
		color : white;
	}
	.selected a:hover {
		color : white;
		/* background-color: darken(#5f5fff, 10%) !important; */
	}
	.selected .menu_a {
		color: white;
	}
	@media screen and (max-height: 450px) {
		.sidenav {padding-top: 15px;}
		.sidenav a {font-size: 18px;}
	}
	@media (max-width: 768px) {
		.menu_icon{
			width: 50%;
			margin: 0px !important;
		}
		.menu_a {
			display: none;
		}
	}
	.bottom-menu {
		position: absolute;
		width: 100%;
		bottom: 2rem;
	}
	.fast-btn {
		margin-bottom: 32px !important;
		padding: .5rem 2.5rem !important;
		font-size: 1.5rem !important;
	}
	.notice {
		color: white;
		background: #5f5fff;
		border-radius: 1rem;
		padding: 1rem;
		box-shadow: 0px 5px 15px 5px #0000004a;
		.btn {
			background: white;
			position: relative;
			border-radius: .5rem;
			margin-bottom: -50px;
			box-shadow: 0px 10px 15px 1px #0000004a;
		}
	}
</style>