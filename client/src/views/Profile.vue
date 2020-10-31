<template>
  <div class="profile">
<body>	  
<div class="container main-secction">
        <div class="row">
            <div class="col-md-12 col-sm-12 col-xs-12 image-section">
                <img src="../images/mountain.jpeg">
            </div>
            <div class="row user-left-part">
                <div class="col-md-3 col-sm-3 col-xs-12 user-profil-part pull-left">
                    <div class="row">
                        <div class="col-md-12 col-md-12-sm-12 col-xs-12 user-image text-center">
                            <img src="https://www.jamf.com/jamf-nation/img/default-avatars/generic-user-purple.png" class="rounded-circle">
                        </div>
                        <div class="col-md-12 user-detail-section1 text-center">
							<div class="wrap-btns">
								
							<b-button variant="info" v-b-modal.changepw class = "change_btn">비밀번호 변경</b-button>
							<b-button variant="danger" v-b-modal.deluser class = "change_btn">회원탈퇴</b-button>
							</div>
							<b-modal
							id="changepw"
							ref="modal1"
							title="비밀번호 변경"
							@show="resetModal"
							@hidden="resetModal"
							@ok="handleOk"
							>
								<form ref="form" @submit.stop.prevent="handleSubmit">
									<b-form-group label="기존 비밀번호">
										<b-form-input
											id="prev-pw"
											v-model="prev.pw"
											:state="prev.state"
											required
										></b-form-input>
										<b-form-invalid-feedback id="prev-pw">
											기존 비밀번호를 입력해주세요.
										</b-form-invalid-feedback>
									</b-form-group>
									<b-form-group label="바꿀 비밀번호">
										<b-form-input
											id="want-pw"
											v-model="want.pw"
											:state="want.state"
											required
										></b-form-input>
										<b-form-invalid-feedback id="want-pw">
											{{wantmessage}}
										</b-form-invalid-feedback>
									</b-form-group>
									<b-form-group label="바꿀 비밀번호 확인">
										<b-form-input
											id="want-pw-chk"
											v-model="want_check.pw"
											:state="want_check.state"
											required
											@keyup.enter="handleOk"
										></b-form-input>
										<b-form-invalid-feedback id="want-pw-chk">
											{{checkmessage}}
										</b-form-invalid-feedback>
									</b-form-group>
								</form>
							</b-modal>
							<b-modal
								id="deluser"
								ref="modal2"
								title="회원탈퇴"
								@show="resetModal"
								@hidden="resetModal"
								@ok="deleteuser"
							>
								<form ref="form">
									<b-form-group label="기존 비밀번호 입력">
										<b-form-input
											id="delete-user-pw"
											v-model="deleteusr.pw"
											:state="deleteusr.state"
											required
										></b-form-input>
										<b-form-invalid-feedback id="delete-user-pw">
											기존 비밀번호 입력해주세요
										</b-form-invalid-feedback>
									</b-form-group>
								</form>
							</b-modal>
                        </div>
                    </div>
                </div>
                <div class="col-md-9 pull-right profile-right-section">
                    <div class="row profile-right-section-row">
                        <div class="col-md-12 profile-header">
                            <div class="row">
                                <div class="col-md-12 profile-header-section1 pull-left">
                                    <h1>{{userdata.user_id}}</h1>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-12 profile-content">
                            <div class="row">
                                <div class="col-md-8">
									<div class="row">
                                        <div class="col-md-5">
                                             <label>아이디</label>
                                        </div>
                                        <div class="col-md-7">
                                             <p>{{userdata.user_id}}</p>
                                        </div>
									</div>
                                    <div class="row">
                                        <div class="col-md-5">
												<label>이메일</label>
                                        </div>
                                        <div class="col-md-7">
											<p>{{userdata.user_email}}</p>
                                        </div>
                                    </div>
									<div class="row">
                                        <div class="col-md-5">
                                            <label>최근 접속일</label>
                                        </div>
                                        <div class="col-md-7">
                                            <p>{{(userdata.user_updatedAt+'').substring(0,10)+' '+(userdata.user_updatedAt+'').substring(11,19)}}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
	</body>
  </div>
</template>

<script>

export default {
	name: 'Profile',
	data () {
		return {
			userdata : '',
			prev : {
				pw : '',
				state : null,
			},
			want : {
				pw : '',
				state : null,
			},
			want_check : {
				pw : '',
				state : null,
			},
			checkmessage : '새로운 비밀번호를 확인해주세요',
			wantmessage : "새로운 비밀번호를 입력해주세요",
			deleteusr : {
				pw : '',
				state : null,
			
			}
		}
	},
	created () {
		const userid = sessionStorage.getItem("userid");
		this.$http.get('/api/users?user_id='+userid)
			.then((response) => {
			this.userdata = response.data.data;
		}).catch((err) =>{
			this.usedata = err;
		})
	},
	methods: {
		resetModal() {
			this.prev.pw = ''
			this.prev.state = null
			this.want.pw = ''
			this.want.state = null
			this.want_check.pw = ''
			this.want_check.state = null
			this.deleteusr.pw = ''
			this.deleteusr.state = null
		},
		handleOk(bvModalEvt) {
			bvModalEvt.preventDefault()
			this.handleSubmit()
		},
		isSame(){
			if(this.want.pw == this.want_check.pw){
				this.want.state = true
				this.want_check.state = true
				return true;
				
			}
			else{
				this.want_check.state = false
				this.checkmessage = "비밀번호가 일치하지 않습니다."
				return false
			}
		},
		handleSubmit() {
			if (this.prev.pw == ''){
				this.prev.state = false
				return false
			}
			else
				this.prev.state = true
			
			if (this.want.pw == ''){
				this.want.state = false
				return false
			}
			else
				this.want.state = true
			
			if (this.want_check.pw == ''){
				this.want_check.state = false
				return false
			}
			else
				this.want_check.state = true
			
			if(this.isSame()){
				const userid = sessionStorage.getItem('userid');
				const userpw = this.prev.pw;
				const wantpw = this.want.pw;
				this.$http.patch('/api/users/password',{
					user_id: userid,
					user_prev_pw : userpw,
					user_want_pw : wantpw,
				}).then((response) => {
					alert(response.data.message);
				}).catch((err) =>{
					console.log(err);
					alert("기존 비밀번호가 일치하지 않습니다.");
					this.resetModal();
				})
				this.$nextTick(() => {
					this.$bvModal.hide('deluser')
				})
			}
		},
		deleteuser(bvModalEvt){
			bvModalEvt.preventDefault()
			if (this.deleteusr.pw == ''){
				this.deleteusr.state = false
				return false
			}
			else
				this.deleteusr.state = true
			
			var isok = confirm("정말 회원탈퇴하시겠습니까?");
			if(isok){
				const userid = this.userdata.user_id;
				const userpw = this.deleteusr.pw;
				this.$http.post('/api/users/delete', { 
					user_id : userid,
					user_pw : userpw,
				}).then((res) => {
					if (res.data.success == true) {
						alert("정상적으로 회원탈퇴 되었습니다.");
						sessionStorage.setItem("userid",'');
						location.href = "/";
					} else {
						alert("입력하신 비밀번호가 일치하지 않습니다.");
					}
				}).catch(function (error) {
					console.log(error)
				})
			}
		}
    }
}
</script>
<style>
	/* body{
		background-color :  #f1f5f6 !important;
	} */
	.main-secction{
		margin-top : 5%;
		box-shadow : 0px 2px 3px gray;
	}
	.image-section{
		padding: 0px;
	}
	.image-section img{
		width: 100%;
		height:40vh;
		position: relative;
	}
	.user-image{
		position: absolute;
		margin-top:-50px;
	}
	.user-left-part{
		margin: 0px;
	}
	.user-image img{
		width:13vh;
		height:13vh;
	}
	.user-profil-part{
		padding-bottom:30px;
	}
	.user-detail-row{
		margin:0px; 
	}
	.wrap-btns{
		padding-top : 1rem;
	}
	.profile-right-section{
		padding: 20px 0px 10px 15px;
	}
	.profile-right-section-row{
		margin: 0px;
	}
	.profile-header-section1 h1{
		font-size: 25px;
		margin: 0px;
	}
	.profile-header-section1 h5{
		color: #0062cc;
	}
	.profile-content{
		padding-top : 1.5rem;
	}
	.change_btn{
		margin-bottom : 2px;
	}
</style>
