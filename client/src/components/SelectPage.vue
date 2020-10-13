<template>
  <div class="sidenav">
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
	<template v-if = "isUser">
		<!-- <router-link v-on:click.native = "logout" to="/">Logout</router-link> -->
		<a href="/" v-on:click = "logout">Logout</a>
	</template>
	<template v-else>
		<router-link to="/login">Login</router-link>
	</template>
  </div>
</template>

<script>
  const menuList = [
    { title: 'Home', link_to: '/'},
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
				return true
			}
			return false
		}
		
	}
  }

</script>

<style>
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

	.sidenav a, .dropdown-btn {
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

	/* When you mouse over the navigation links, change their color		*/
	.sidenav a:hover {
		color: #f1f1f1;
	}
	/* On smaller screens, where height is less than 450px, change the style of the sidebar (less padding and a smaller font size) */
	@media screen and (max-height: 450px) {
		.sidenav {padding-top: 15px;}
		.sidenav a {font-size: 18px;}
	}

	/* On mouse-over */
	.sidenav a:hover, .dropdown-btn:hover {
		color: #f1f1f1;
	}
	/* Add an active class to the active dropdown button */
	.active {
		background-color: green;
		color: white;
	}

	/* Dropdown container (hidden by default). Optional: add a lighter background color and some left padding to change the design of the dropdown content */
	.dropdown-container {
		display: none;
		background-color: #5eaf13;
		padding-left: 8px;
	}

	/* Optional: Style the caret down icon */
	.fa-caret-down {
		float: right;
		padding-right: 8px;
	}
</style>


<!-- <template>
  
	<div>
		<b-navbar toggleable="lg" type="dark" variant="info">
		<b-navbar-brand href="#">NavBar</b-navbar-brand>

		<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

		<b-collapse id="nav-collapse" is-nav>
			<b-nav>
				<b-nav-item><router-link to="/"><p class ="listyle">Home</p></router-link></b-nav-item>
				<b-nav-item><router-link to="/upload"><p class ="listyle">Upload</p></router-link></b-nav-item>
				<b-nav-item><router-link to="/login"><p class ="listyle">Login</p></router-link></b-nav-item>
			</b-nav>

			<b-navbar-nav class="ml-auto">
				<b-nav-form>
					<b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
					<b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
				</b-nav-form>

				<b-nav-item-dropdown text="Lang" right>
					<b-dropdown-item href="#">EN</b-dropdown-item>
					<b-dropdown-item href="#">ES</b-dropdown-item>
					<b-dropdown-item href="#">RU</b-dropdown-item>
					<b-dropdown-item href="#">FA</b-dropdown-item>
				</b-nav-item-dropdown>

				<b-nav-item-dropdown right>
					<template v-slot:button-content>
					<em>User</em>
					</template>
					<b-dropdown-item href="#">Profile</b-dropdown-item>
					<b-dropdown-item href="#"><router-link to="/login">LOG OUT</router-link></b-dropdown-item>
				</b-nav-item-dropdown>
			</b-navbar-nav>
		</b-collapse>
		</b-navbar>
	</div>
</template>
<style>
	.listyle{
		color : black;
		margin : 0;	
	}
</style>
 -->