<template>
  <div class="profile">
	<div class = "user_profile_wrap">
		유저 아이디 : {{userdata.user_id}}
		
		<p v-b-modal.changepw class = "change_btn">비밀번호 변경</p>

		<b-modal
			id="changepw"
			ref="modal"
			title="비밀번호 변경"
			@show="resetModal"
			@hidden="resetModal"
			@ok="handleOk"
		>
			<form ref="form" @submit.stop.prevent="handleSubmit">
				<b-form-group
					:state="prev.state"
					label="기존 비밀번호"
					invalid-feedback="기존 비밀번호를 입력해주세요"
				>
					<b-form-input
						id="name-input"
						v-model="prev.pw"
						:state="prev.state"
						required
					></b-form-input>
				</b-form-group>
				<b-form-group
					:state="want.state"
					label="바꿀 비밀번호"
					invalid-feedback="바꿀 비밀번호를 입력해주세요"
				>
					<b-form-input
						id="name-input"
						v-model="want.pw"
						:state="want.state"
						required
					></b-form-input>
				</b-form-group>
				<b-form-group
					:state="want_check.state"
					label="바꿀 비밀번호 확인"
					invalid-feedback="바꿀 비밀번호를 입력해주세요"
				>
					<b-form-input
						id="name-input"
						v-model="want_check.pw"
						:state="want_check.state"
						required
					></b-form-input>
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
		checkFormValidity() {
			const valid = this.$refs.form.checkValidity()
			if (this.prev.pw == '')
				this.prev.state = valid
			else
				this.prev.state = !valid
			if (this.want.pw == '')
				this.want.state = valid
			else
				this.want.state = !valid
			if (this.want_check.pw == '')
				this.want_check.state = valid
			else
				this.want_check.state = !valid
			return valid
		},
		resetModal() {
			this.prev.pw = ''
			this.prev.state = null
			this.want.pw = ''
			this.want.state = null
			this.want_check.pw = ''
			this.want_check.state = null
		},
		handleOk(bvModalEvt) {
			bvModalEvt.preventDefault()
			this.handleSubmit()
		},
		checkWantpw(){
			if(this.want.pw != this.want_check.pw){
				return false;
			}
			return true;
		},
		handleSubmit() {
			
			if (!this.checkFormValidity()) {
				return
			}
			const userid = sessionStorage.getItem('userid');
			const userpw = this.prev.pw;
			const wantpw = this.want.pw;
			this.$http.put('/api/users/password',{
				user_id: userid,
				user_prev_pw : userpw,
				user_want_pw : wantpw,
			}).then((response) => {
				alert(response.data.message);
			}).catch((err) =>{
				console.log(err);
				alert("기존 비밀번호를 잘못입력하셨습니다.");
			})
			this.$nextTick(() => {
				this.$bvModal.hide('changepw')
			})
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
