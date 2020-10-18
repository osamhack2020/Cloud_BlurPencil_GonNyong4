<template>
  <div class="profile">
	<div class = "user_profile_wrap">
		유저 아이디 : {{userdata.user_id}}
		<br>
		<p v-b-modal.changepw class = "change_btn">비밀번호 변경</p>
		<p v-b-modal.deluser class = "change_btn">회원탈퇴</p>
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
						@keyup.enter="deleteuser"
					></b-form-input>
					<b-form-invalid-feedback id="delete-user-pw">
						기존 비밀번호 입력해주세요
					</b-form-invalid-feedback>
				</b-form-group>
			</form>
		</b-modal>
	</div>
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
			checkmessage : '바꿀 비밀번호를 확인해주세요',
			wantmessage : "바꿀 비밀번호를 입력해주세요",
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
		isEmpty(){
			
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
		// isChanged(){
		// 	if(this.prev.pw != this.want.pw){
		// 		this.prev.pw = false;
		// 		this.want.pw = false;
		// 		this.wantmessage = "기존 비밀번호와 일치하지 않습니다."
		// 		return false;
		// 	}
		// 	else{
		// 		return true;
		// 	}
		// },
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
					this.$bvModal.hide('changepw')
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
				alert(userid + userpw);
				this.$http.post('/api/users/delete', { 
					user_id : userid,
					user_pw : userpw,
				}).then((res) => {
					if (res.data.success == true) {
						alert(res.data.message);
						sessionStorage.setItem("userid",'');
						location.href = "/";
					}
				}).catch(function (error) {
					console.log(error)
					alert("기존 비밀번호가 일치하지 않습니다.");
				})
			}
		}
    }
}
</script>
<style>
	.change_btn{
		width : 200px;
		margin : 0 auto;
	}
</style>
