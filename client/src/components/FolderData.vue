<template>
	<div class="container data-section">
		<button class="btn before-btn" @click="cancelFolderData();">
			<div class="before-btn-circle">
				<p>＜</p>
			</div>
			뒤로가기</button>
		<h3 style="text-align:left; display: inline-block">{{ clicked_folder.folderName }}</h3>
		<div v-show="user_oid === clicked_folder.owner" style="float: right;">
			<!-- <button class="btn" v-on:click="downloadWork(clicked_folder.fileName)" style="float:right; background-color:white;">
				<img src = "../images/import.svg" class="btn_image"/>
				다운로드
			</button> -->
			<button class="btn" v-on:click="showShareFolder = true;" style="background-color:white; margin-right:1rem;">
				<img src = "../images/share.svg" class="btn_image">
				폴더 공유
			</button>
			<button class="btn" v-on:click="removeWork(clicked_folder._id, clicked_folder.fileName)" style="background-color:white;">
				<img src = "../images/trash-alt.svg" class="btn_image">
				폴더 삭제
			</button>
		</div>
		<div class="show-shared-user">
			<p>공유한 사람들 : </p>
			<div @click="unSharedClickedUser = user.user_id; showUnShared = true;" class="share-user-profile" v-for="(user, idx2) in clicked_folder.share" :key="idx2">{{ user.user_id }}</div>
		</div>
		<div>
			{{ fileList }}
		</div>
		<div class="custom-modal" v-if="showShareFolder" style="text-align:center;">
			<div class="modal-box">
				<b-form-group id="input-group-email" label="초대할 상대방의 이메일을 입력해주세요." style="font-weight: 600; font-size: 1.2rem; margin-bottom: 1rem;">
					<b-form-input
						id="invite-email"
						v-model="inviteEmail"
						required
					></b-form-input>
					<b-form-invalid-feedback id="invite-email">
						이메일을 입력해주세요.
					</b-form-invalid-feedback>
				</b-form-group>
				<button class="btn btn-primary" @click="inviteFolder" >초대</button>
				<button class="btn" @click="showShareFolder = false">취소</button>
			</div>
		</div>
		<div class="custom-modal unsharedUserModal" v-if="showUnShared" style="text-align:center;">
			<div class="modal-box">
				<b-form-group label="공유를 해제하시겠습니까?" style="font-weight: 600; font-size: 1.2rem; margin-bottom: 1rem;">
					해제 대상 : {{ unSharedClickedUser }}
				</b-form-group>
				<button class="btn btn-primary" @click=" cancelShareToUser()" >공유 해제</button>
				<button class="btn" @click="showUnShared = false">취소</button>
			</div>
		</div>
	</div>
</template>


<script>	
export default {
	name: 'WorkData',
	props: {
		userid: {
			type: String,
            default : '',
		},
		/*eslint no-dupe-keys: "error"*/
		clicked_folder: {
		}
    },
	data () {
		return {
			user_oid: '',
			fileList: [],
			inviteEmail: '',
			showShareFolder: false,
			showUnShared: false,
			unSharedClickedUser: ''
		}
	},
	created(){
		this.getFolderFiles();
		this.user_oid = sessionStorage.getItem("user_oid");
	},
	methods : {	
		cancelFolderData : function() {
			this.$emit('cancelFolderData');
		},
		getFolderFiles () {
			this.$http.get(`/api/folders/files/${this.clicked_folder._id}`)
				.then((response) => {	// eslint-disable-line no-unused-vars
					console.log(response);
					this.fileList = response.data;
				})
				.catch((err) =>{
					this.workData = err;
				})
		},
		inviteFolder() {
			if (!this.inviteEmail || this.inviteEmail == '') {
				alert(`이메일을 입력해주세요.`);
				return;
			}
			
			this.$http.post('/api/folders/share',{
				email: this.inviteEmail,
				folder_oid : this.clicked_folder._id
			}).then((response) => {
				if (response.data.success) {
					alert(`${this.inviteEmail}님을 초대하였습니다.`);
					this.showShareFolder = false;
					this.refreshFolderSharing();
				} else {
					alert(`존재하지 않는 이메일입니다.`);
				}
			}).catch((err) =>{
				console.log(err);
			})
		},
		downloadWork (fileName) {
			this.$http ({
				url: `${this.serverUrl}${fileName}`,
				method: 'GET',
				responseType: 'blob',
			}).then((response) => {
				var fileURL = window.URL.createObjectURL(new Blob([response.data]));
				var fileLink = document.createElement('a');

				fileLink.href = fileURL;
				fileLink.setAttribute('download', fileName);
				document.body.appendChild(fileLink);

				fileLink.click();
			});
		},
		removeWork(work_oid, fileName) {
			var user_id = sessionStorage.getItem("userid");
			this.$http.post(`/api/works/delete/${user_id}`, {
				work_oid: work_oid,
				fileName: fileName
			})
			.then((response) => {
				console.log(response.data);
				location.reload();
			})
			.catch((err) =>{
				this.workData = err;
			})
		},
		removeFolder() {
			this.$http.post(`/api/folders/delete/`, {
				owner: this.user_oid,
				folder_oid: this.clicked_folder._id
			})
			.then((response) => {
				console.log(response.data);
				location.reload();
			})
			.catch((err) =>{
				this.workData = err;
			})
		},
		cancelShareToUser() {
			this.$http.post(`/api/folders/unshare/`, {
				share_id: this.unSharedClickedUser,
				folder_oid: this.clicked_folder._id
			})
			.then((response) => {
				this.showUnShared = false;
				if (response.data.success)
					this.refreshFolderSharing();
			})
			.catch((err) =>{
				this.workData = err;
			})
		},
		refreshFolderSharing() {
			this.$http.get(`/api/folders/sharing/?folder_oid=${this.clicked_folder._id}`)
			.then((response) => {
				this.clicked_folder.share = response.data;
			})
			.catch((err) =>{
				this.workData = err;
			})
		}
	}
};
</script>

<style lang="scss">
.before-btn {
	margin-top: 2.5rem;
	margin-left: 2rem;
	position: absolute;
	left: 1rem;
	top: 1rem;
	font-size: 1.2rem !important;
	opacity: .7;
	.before-btn-circle {
		width: 2.5rem;
		height: 2.5rem;
		border: 1px solid rgba(black, .5);
		border-radius: 3rem;
		display: inline-flex;
		justify-content: center;
		align-items: center;
		margin-right: .5rem;
		p {
			font-size: .7rem;
			line-height: 2rem;
			margin-bottom: 0px;
		}
	}
}
.data-section {
	margin-top: 5rem;
	text-align: left;
	.data-image {
		padding: 1rem;
		background-color: white;
		border-radius: .25rem;
	}
	.data-setting {
		padding: 1rem 1rem 2rem 1rem;
		background-color: white;
		border-radius: .25rem;
		.setting-comment {
			font-weight : bold;
			padding-top: 1rem;
			padding-bottom: 1rem;
			transition: none;
			cursor: auto;
			&:hover {
				background: none;
			}
			.show-value {
				color: black;
				font-size: 1rem;
				bottom: 0px;
				position: relative;
				font-weight: 500 !important;
				margin-left: .5rem !important;
			}
		}
	}
}
.show-shared-user {
	display: flex;
	margin-bottom: 1rem;
	align-items: center;
	.share-user-profile {
		margin-left: .5rem;
		width: 2.5rem;
		border-radius: 2.5rem;
		height: 2.5rem;
		cursor: pointer;
	}
}
</style>

