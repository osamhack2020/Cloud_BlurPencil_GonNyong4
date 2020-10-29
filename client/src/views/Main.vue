<template>
	<div class="main">
		<div class="folders-section">
			<h3>내 폴더들</h3>
			<button class="btn folder create" @click="showCreateFolder = true">
				<p class="folder-text">폴더생성</p>
			</button>
			<button class="btn folder" :class="{ 'mine' : folder.owner === user_oid, 'share' : folder.owner !== user_oid }" v-for="(folder, idx) in folderList" :key="idx">
				<p class="folder-text folder-title">{{ folder.folderName }}</p>
			</button>
		</div>
		<div class="recents-section">
			<h3>최근 작업내역</h3>
			<div>
				<div class="recent-work" v-for="(recent, idx) in recentWorks" :key="idx">
					<img class="recent-image" :src="serverUrl + recent.fileName" />
					<p class="recent-fileName">{{ recent.fileName }}</p>
					<p class="recent-fileName">{{ recent.workedAt }}</p>
				</div>
			</div>
		</div>
		<div class="create-folder-modal" v-if="showCreateFolder">
			<div class="modal-box">
				<b-form-group label="폴더 이름을 입력해주세요." style="text-align: left; font-weight: 600; font-size: 1.2rem; margin-bottom: 1rem;">
					<b-form-input
						id="folder-input"
						v-model="folderName"
						required
					></b-form-input>
					<b-form-invalid-feedback id="folder-input">
						폴더명을 입력해주세요.
					</b-form-invalid-feedback>
				</b-form-group>
				<button class="btn btn-primary" @click="createFolder" >폴더생성</button>
				<button class="btn" @click="showCreateFolder = false">취소</button>
			</div>
		</div>
		<div v-if="showShareFolder">
			<b-form-group id="input-group-email" label="이메일" label-for="input-email">
				<b-form-input
					id="invite-email"
					v-model="inviteEmail"
					required
				></b-form-input>
				<b-form-invalid-feedback id="invite-email">
					이메일을 입력해주세요.
				</b-form-invalid-feedback>
			</b-form-group>
			<button @click = "inviteFolder" >초대</button>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Main',
	props: {
		userid: {
			type: String,
            default : '',
		},
    },
	data () {
		return {
			user_oid: '5f82cb8b9e963310f13f5129',
			inviteEmail: '',
			folderName: '',
			folderList: '',
			recentWorks: '',
			showCreateFolder: false,
			showShareFolder: false
		}
	},
	methods : {
		inviteFolder() {
			this.$http.post('/api/folders/share',{
				email: this.inviteEmail,
				folder_oid : '5f9a976ac0eb60083b2ecf18'
			}).then((response) => {
				alert(response.data);
			}).catch((err) =>{
				console.log(err);
			})
		},
		createFolder() {
			this.$http.post('/api/folders',{
				folderName: this.folderName,
				owner : this.user_oid
			}).then((response) => {
				alert(response.data.message);
				this.showCreateFolder = false;
			}).catch((err) =>{
				console.log(err);
			})
		},
		getFolders() {
			this.$http.get(`/api/folders?user_oid=${this.user_oid}`)
				.then((response) => {
					this.folderList = response.data;
				}).catch((err) =>{
					console.log(err);
				})
		}
	},
	created(){
		this.getFolders();
		
		var userid = sessionStorage.getItem("userid");
		this.user_id = userid;
		var skip = 0;	// 뛰어넘기	(default 0)
		var limit = 5;	// 개수	(default 5)
		var sort = -1;	// -1 최신순부터, 1 예전순부터 (default -1)
		
		this.$http.get(`/api/works/${userid}/?skip=${skip}&limit=${limit}&sort=${sort}`)
			.then((response) => {
				this.recentWorks = response.data;
				if (this.recentWorks.length > 0) {
					// 작업물이 한개 이상이라도 있으면
				}
			})
			.catch((err) =>{
				this.recentWorks = err;
			})
	}
}
</script>
<style lang="scss" sc>
	.main {
		padding: 5rem;
		position: relative;
	}
	.folders-section {
		text-align: left;
		margin-bottom: 5rem;
		h3 {
			font-weight: 700;
		}
		.folder {
			width: 12rem;
			height: 10rem;
			border-radius: 1rem;
			position: relative;
			background-color: tomato;
			box-shadow: 3px 5px 10px 2px #00000030;
			& + .folder {
				margin-left: 1rem;
			}
			&.create {
				color: #7f7ffb;
				border: 2px dashed #7f7ffb;
				background-color: white;
			}
			&.mine {
				background-color: #7f7ffb;
			}
			&.share {
				color: #7f7ffb;
				border: 2px solid #7f7ffb;
			}
			.folder-text {
				left: 0px;
				bottom: 0px;
				text-align: left;
				position: absolute;
				margin-left: 24px;
				margin-bottom: 24px;
				font-weight: 600;
			}
			.folder-title {
				color: white;
			}
		}
	}
	.recents-section {
		text-align: left;
		h3 {
			font-weight: 700;
		}
		.recent-work {
			display: flex;
			align-items: center;
			justify-content: space-between;
			cursor: pointer;
			padding: 1rem 1rem;
			border-radius: .5rem;
			transition: background .3s ease;
			box-shadow: 0px 4px 5px 2px #0000000d;
			&:hover {
				background-color: #7f7ffb1c !important;
				box-shadow: 0px 4px 5px 2px #0000000d !important;
			}
			& + .recent-work {
				margin-top: 1rem;
			}
			.recent-image {
				// max-width: 3rem;
				max-height: 3rem;
			}
			.recent-fileName {
				margin-bottom: 0px;
			}
		}
	}
	.create-folder-modal {
		position: absolute;
		left: 0px;
		top: 0px;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, .7);
		z-index: 10;
		display: flex;
		align-items: center;
		justify-content: center;
		.modal-box {
			padding: 4rem 2rem;
			width: 30rem;
			border-radius: 1rem;
			background-color: white;
			box-shadow: 0px 5px 15px 5px #ffffff17;
			.btn-primary {
				margin-top: 16px;
				width: 100%;
			}
		}
	}
</style>
