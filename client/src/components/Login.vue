<template>
    <div class = "Login">
			<div class = "message">
				<p>자동 모자이크 웹 서비스</p>	
			</div>
            <div class="form-wraps">
                <div class="button-wraps">
                    <div id="btns" :style = "{left : btnLeft}"></div>
                    <button type="button" class="togglebtns" @click = "loginbtn">LOG IN</button>
                    <button type="button" class="togglebtns" @click = "registerbtn">REGISTER</button>
                </div>
				
				<div class = "login">
					<div class="input-groups" :style = "{left : loginLeft}">
						<b-form-group id="input-group-2" label="Your ID:" label-for="input-2">
							<b-form-input
								id="input-2"
								v-model="loginUser.id"
								required
								placeholder="Enter ID"
							></b-form-input>
						</b-form-group>
						<b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
							<b-form-input
								id="input-2"
								v-model="loginUser.password"
								required
								placeholder="Enter password"
								@keyup.enter="login"
							></b-form-input>
						</b-form-group>
						<button class="submit" @click = "login" >Login</button>
					</div>
				</div>	
				<div class = "Register">
					<div class="input-groups" :style = "{left : registerLeft}">
						<b-form-group id="input-group-2" label="Your ID:" label-for="input-2">
							<b-form-input
								id="input-2"
								v-model="registerUser.id"
								required
								placeholder="Enter ID"
							></b-form-input>
						</b-form-group>
						<b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
							<b-form-input
								id="input-2"
								v-model="registerUser.password"
								required
								placeholder="Enter password"
								@keyup.enter="register"
							></b-form-input>
						</b-form-group>
						<button class="submit" @click = "register">Register</button>
					</div>
				</div>	
            </div>
	</div>
</template>

<script>
  
	export default{
		data(){
			return {
				btnLeft : "0px",
				loginLeft : "50px",
				registerLeft : "450px",
				registerUser : {
					id : '',
					password : '',
				},
				loginUser : {
					id : '',
					password : '',
				},
			}
		},
		methods:{
			loginbtn(){
				this.btnLeft = "0px";
				this.loginLeft = "50px";
				this.registerLeft = "450px";
			},
			registerbtn(){
				this.btnLeft = "110px";
				this.loginLeft = "-400px";
				this.registerLeft = "50px";
			},
			login(){
				if(this.loginUser.id == '' || this.loginUser.password == ''){
					alert("로그인할 아이디나 패스워드를 입력해주세요");
					return false;
				}
				this.$http.post('/api/users/login', {
				user: this.loginUser
				}).then(
				(res) => {  //로그인 성공
					alert(res.data.message);
					// this.$router.push('/main')  // 로그인한 뒤 메인 페이지로 이동시켜야함
					if (res.data.success == true){
						this.$router.push({name: 'Main', params: {userid : this.loginUser.id}})
						this.$router.go()
						sessionStorage.setItem("userid",this.loginUser.id);
					}
				},
				(err) => { // error 를 보여줌
					alert('Login failed! please check your id or password');
					console.log(err);
					this.loginUser.id= '';
					this.loginUser.password = '';
				}).catch((err) => {
					console.log(err);
				})
			},
			register(){
				if(this.registerUser.id == '' || this.registerUser.password == ''){
					alert("등록할 아이디나 패스워드를 입력해주세요");
					return false;
				}
				this.$http.post('/api/users/register', { 
					user: this.registerUser
				}).then((res) => {
					if (res.data.success == true) {
						alert(res.data.message);
						// this.$router.push('/login')  // 로그인한 뒤 메인 페이지로 이동시켜야함
						this.loginbtn();
					}
					if (res.data.success == false) {
						alert(res.data.message);
						this.registerUser.id= '';
						this.registerUser.password = '';
					}
				}).catch(function (error) {
					alert('error')
					console.log(error)
				})
			}
		}
		
	}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
	
    @import '../assets/style.css'
</style>
