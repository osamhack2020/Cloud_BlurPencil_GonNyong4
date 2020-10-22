<template>
  <div class="sidenav">
	<div class = "logowrap">
		<p><img src="../images/logo(125x125).png" class="nav_logo"/>
			Blur Pencil
		</p>
	</div>
	<div class = "menuwrap">
		
		<div v-for="item in items" :key="item.link_to" 
			class = "sidemenu" 
			v-bind:class="{selected : item.isSelected}"
			@click = "isSelected(item)"
		>	
			<a>{{item.title}}</a>
		</div>
		
		<div class = "sidemenu bottom-menu"
			v-if = "isUser"
			@click = "logout"	
		>
			<a>Logout</a>
		</div>
	</div>
    
	
  </div>
</template>

<script>

  const menuList = [
    { title: 'Main', link_to: '/main',isSelected : false},
    { title: 'Profile', link_to: '/profile',isSelected : false},
    { title: 'Upload', link_to: '/upload', isSelected : false},
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
			this.$router.push(item);
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
		var para = document.location.href.split("/");
		for(var i =0;i<menuList.length;i++){
			if(menuList[i].link_to == ('/'+para[3])){
				menuList[i].isSelected = true;
			}
		}

	}
  }

</script>

<style>
	.nav_logo {
		width: 3rem;
	}
	.logowrap{
		font-size : x-large;
		font-weight : bold;	
		color : #0d112a;
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
		box-shadow : 0 2px 2px black;
	}
	.sidemenu{
		padding : 1vh 2vh 1vh 2vh;
		/* padding: 6px 6px 6px 6px; */	
		font-size: 1.5vw;
		font-weight : bold;
		cursor : pointer;
	}
	.sidemenu:hover{
		background-color : #efeded;
	}
	.sidemenu a{
		color : black;
	}
	.sidemenu a:hover{
		text-decoration: none;
		color : black;
	}
	.selected{
		background: linear-gradient( to right, #3e0ecc, #7c60cd );
		color : white;
	}
	@media screen and (max-height: 450px) {
		.sidenav {padding-top: 15px;}
		.sidenav a {font-size: 18px;}
	}
	.bottom-menu {
		position: absolute;
		width: 100%;
		bottom: 2rem;
	}
</style>