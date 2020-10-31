<template>
	<div class="main">
		<div class="folders-section" v-if="!showWorkedData && !showFolderData">
			<h3>내 폴더들</h3>
			<button class="btn folder create" @click="showCreateFolder = true">
				<p class="folder-text">폴더생성</p>
			</button>
			<button class="btn folder" :class="{ 'mine' : folder.owner === user_oid, 'share' : folder.owner !== user_oid }" v-for="(folder, idx) in folderList" :key="idx" @click="showFolderData = true; clicked_folder = folder">
				<div class="share-user-profile" v-for="(user, idx2) in folder.share" :key="idx2">{{ user.user_id }}</div>
				<p class="folder-text folder-title">{{ folder.folderName }}</p>
			</button>
		</div>
		<div class="recents-section" v-if="!showWorkedData && !showFolderData">
			<h3>최근 작업내역</h3>
			<div>
				<div class="recent-work" v-for="(recent, idx) in recentWorks" :key="idx" @click="showWorkedData=true; recent.user_oid = user_oid; clicked_image=recent;">
					<img class="recent-image" :src="serverUrl + recent.fileName" />
					<p class="recent-fileName">{{ recent.fileName }}</p>
					<p class="recent-fileName">/ {{ getFolderName(recent.folder) }}</p>
					<p class="recent-fileName">{{recent.workedAt.substring(0,10)+' '+recent.workedAt.substring(11,19)}}</p>
				</div>
			</div>
		</div>
		<div class="custom-modal" v-if="showCreateFolder">
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
		<WorkData v-if="showWorkedData" @cancelWorkData="cancelWorkData" :clicked_image="clicked_image"></WorkData>
		<FolderData v-if="showFolderData" @cancelFolderData="cancelFolderData" :clicked_folder="clicked_folder"></FolderData>
	</div>
</template>

<script>
import WorkData from '@/components/WorkData.vue'
import FolderData from '@/components/FolderData.vue'
	
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
			user_oid: '',
			inviteEmail: '',
			folderName: '',
			folderList: '',
			recentWorks: '',
			showCreateFolder: false,
			showWorkedData: false,
			showFolderData: false,
			clicked_image: '',
			clicked_folder: ''
		}
	},
	methods : {
		createFolder() {
			this.$http.post('/api/folders',{
				folderName: this.folderName,
				owner : this.user_oid
			}).then((response) => {
				alert(response.data.message);
				this.showCreateFolder = false;
				this.getFolders();
			}).catch((err) =>{
				console.log(err);
			})
		},
		getFolderName(data) {
			if (!data)
				return '';
			return data.folderName
		},
		getFolders() {
			this.$http.get(`/api/folders?user_oid=${this.user_oid}`)
				.then((response) => {
					this.folderList = response.data;
				}).catch((err) =>{
					console.log(err);
				})
			this.$http.get(`/api/folders/shared/?user_oid=${this.user_oid}`)
				.then((response) => {
					this.folderList = this.folderList.concat(response.data);
				}).catch((err) =>{
					console.log(err);
				})
		},
		cancelWorkData() {
			this.getRecentWork();
			this.showWorkedData = false;
		},
		cancelFolderData() {
			this.getRecentWork();
			this.showFolderData = false;
		},
		getRecentWork() {
			var userid = sessionStorage.getItem("userid");
			this.user_id = userid;
			var skip = 0;	// 뛰어넘기	(default 0)
			var limit = 5;	// 개수	(default 5)
			var sort = -1;	// -1 최신순부터, 1 예전순부터 (default -1)

			this.$http.get(`/api/works/${userid}/?skip=${skip}&limit=${limit}&sort=${sort}`)
				.then((response) => {
					this.recentWorks = response.data;
					// console.log(this.recentWorks);
					// console.log(this.recentWorks);
					if (this.recentWorks.length > 0) {
						// 작업물이 한개 이상이라도 있으면
					}
				})
				.catch((err) =>{
					this.recentWorks = err;
				})
		}
	},
	created(){
		this.user_oid = sessionStorage.getItem("user_oid");
		console.log('uid ', sessionStorage.getItem("userid"));
		this.getFolders();
		this.getRecentWork();
	},
	components: {
		WorkData,
		FolderData
	}
}
</script>
<style lang="scss">
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
			padding-left: 1.5rem;
			padding-right: 1.5rem;
			padding-top: 1.5rem;
			display: inline-flex;
			/* text-align: left; */
			/* align-content: flex-start; */
			/* vertical-align: top; */
			overflow: hidden;
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
				background-color: #b0abfb;
				border: 2px solid #b0abfb;
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
				// background-color: #7f7ffb1c !important;
				background-color: white !important;
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
	.custom-modal {
		position: absolute;
		left: 0px;
		top: 0px;
		width: 100%;
		height: 100vh;
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
	.share-user-profile {
		width: 1.5rem;
		height: 1.5rem;
		border-radius: 1rem;
		background-color: white;
		margin-right: .5rem;
		overflow: hidden;
		box-shadow: 2px 2px 3px 1px #00000030;
	}
</style>
