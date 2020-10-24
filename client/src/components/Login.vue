<template>
    <div class = "Login">
			<div class = "message">
				<!-- <p>자동 모자이크 웹 서비스</p>	 -->
			</div>
            <div class="form-wraps">
                <div class="button-wraps">
                    <div id="btns" :style = "{left : btnLeft}"></div>
                    <button type="button" class="togglebtns" @click = "loginbtn">로그인</button>
                    <button type="button" class="togglebtns" @click = "registerbtn">회원가입</button>
                </div>
				
				<div class = "login">
					<div class="input-groups" :style = "{left : loginLeft}">
						<b-form-group id="input-group-2" label="아이디" label-for="input-2">
							<b-form-input
								id="login-1"
								v-model="loginUser.id"
								required
								:state = "loginState.id"
							></b-form-input>
							<b-form-invalid-feedback id="login-1">
								아이디를 입력해주세요.
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group id="input-group-2" label="비밀번호" label-for="input-2">
							<b-form-input
								id="login-2"
								v-model="loginUser.password"
								required
								:state = "loginState.password"
								@keyup.enter="login"
							></b-form-input>
							<b-form-invalid-feedback id="login-2">
								비밀번호를 입력해주세요.
							</b-form-invalid-feedback>
						</b-form-group>
						<button class="submit" @click = "login" >로그인</button>
					</div>
				</div>	
				<div class = "Register">
					<div class="input-groups" :style = "{left : registerLeft}">
						<b-form-group id="input-group-2" label="아이디" label-for="input-2">
							<b-form-input
								id="register-1"
								v-model="registerUser.id"
								required
								:state = "registerState.id"
							></b-form-input>
							<b-form-invalid-feedback id="register-1">
								아이디를 입력해주세요.
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group id="input-group-2" label="이메일" label-for="input-2">
							<b-form-input
								id="register-2"
								v-model="registerUser.email"
								required
								:state = "registerState.email"
							></b-form-input>
							<b-form-invalid-feedback id="register-2">
								이메일을 입력해주세요.
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group id="input-group-2" label="비밀번호" label-for="input-2">
							<b-form-input
								type = "password"
								id="register-3"
								v-model="registerUser.password"
								required
								:state = "registerState.password"
								@keyup.enter="register"
							></b-form-input>
							<b-form-invalid-feedback id="register-3">
								비밀번호를 입력해주세요.
							</b-form-invalid-feedback>
						</b-form-group>
						<button class="submit" @click = "register">회원가입</button>
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
					email : '',
				},
				loginUser : {
					id : '',
					password : '',
				},
				loginState : {
					id : null,
					password : null,
				},
				registerState : {
					id : null,
					password : null,
					email : null
				}
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
				if(this.loginUser.id == ''){
					this.loginState.id = false
					return false;
				}
				else{
					this.loginState.id = true;
				}
				if(this.loginUser.password == ''){
					this.loginState.password = false
					return false;
				}
				else{
					this.loginState.password = true;
				}
				this.$http.post('/api/users/login', {
				user: this.loginUser
				}).then(
				(res) => {  //로그인 
					if (res.data.success == true){
						alert("로그인에 성공하였습니다.");
						this.$router.push({name: 'Main', params: {userid : this.loginUser.id}})
						this.$router.go()
						sessionStorage.setItem("userid",this.loginUser.id);
					}
					else{
						if(res.data.message == '아이디도 비밀번호도 틀림'){
							alert("존재하지 않는 아이디입니다.");
							this.loginState.id = false;
							this.loginState.password = false;
						}
						else{
							alert("비밀번호가 잘못되었습니다.");
							this.loginState.password = false;
						}
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
				if(this.registerUser.id == ''){
					this.registerState.id = false
					return false;
				}
				else{
					this.registerState.id = true;
				}
				if(this.registerUser.email == ''){
					this.registerState.email = false;
					return false
				}
				else{
					this.registerState.email = true;
				}
				if(this.registerUser.password == ''){
					this.registerState.password = false
					return false;
				}
				else{
					this.registerState.password = true;
				}
				
				this.$http.post('/api/users/register', { 
					user: this.registerUser
				}).then((res) => {
					if (res.data.success == true) {
						alert(res.data.message);
						// this.$router.push('/login')  // 로그인한 뒤 메인 페이지로 이동시켜야함
						this.registerUser.id= '';
						this.registerUser.password = '';
						this.registerUser.email = '';
						this.registerState.id = null;
						this.registerState.email = null;
						this.registerState.password = null;
						this.loginbtn();
					}
					if (res.data.success == false) {
						alert(res.data.message);
						
						
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
