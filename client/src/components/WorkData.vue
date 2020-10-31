<template>
	<div class="container data-section">
		<button class="btn before-btn" @click="cancelWorkData();">
			<div class="before-btn-circle">
				<p>＜</p>
			</div>
			{{ beforeComponent }}</button>
		<h3 style="text-align:left;">{{clicked_image.fileName}}</h3>
		<div class="row">
			<div class="col-lg-8">
				<div class="data-image">
					<img class="worked-image" v-bind:src="serverUrl + clicked_image.fileName"/>
				</div>
			</div>
			<div class="col-lg-4">
				<select class="form-control form-control-lg folder-select" v-model="workFolder" @change="folderChange($event)" v-show="user_oid == clicked_image.user_oid">
					<option v-for="(folder, idx) in folderList"
							:key="idx"
							:value="folder._id"
							:selected="workFolder == folder._id">{{ folder.folderName }}</option>
				</select>
				<div class="data-setting">
					<p class="setting-comment">인식률 <span class="show-value">{{ clicked_image.score }}</span></p>
					<p class="setting-desc">로고로 인식할 추적 점수의 최소값</p>
					<hr/>
					<p class="setting-comment">NMS <span class="show-value">{{ clicked_image.nms }}</span></p>
					<p class="setting-desc">Non-Maximum Suppression에서 사용할 IoU(Intersection over Union)의 threshold 값</p>
					<hr/>
					<p class="setting-comment">작업일</p>
					<p class="setting-desc">{{ clicked_image.workedAt }}</p>
				</div>
			</div>
		</div>
		<div v-show="user_oid == clicked_image.user_oid">
			<button class="btn" v-on:click="downloadWork(clicked_image.fileName)" style="float:right; background-color:white;">
				<img src = "../images/import.svg" class="btn_image"/>
				다운로드
			</button>
			<button class="btn" v-on:click="removeWork(clicked_image._id, clicked_image.fileName)" style="float:right; background-color:white; margin-right:1rem;">
				<img src = "../images/trash-alt.svg" class="btn_image">
				삭제
			</button>
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
		clicked_image: {
		},
		beforeComponent: {
			type: String,
			default: '뒤로가기'
		}
    },
	data () {
		return {
			user_oid: '',
			folderList: [],
			workFolder: this.clicked_image.folder ? this.clicked_image.folder._id : ''
		}
	},
	created(){
		this.user_oid = sessionStorage.getItem("user_oid");
		this.getFolderList();
	},
	methods : {	
		cancelWorkData : function() {
			this.$emit('cancelWorkData');
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
			.then((response) => {	// eslint-disable-line no-unused-vars
				location.reload();
			})
			.catch((err) =>{
				this.workData = err;
			})
		},
        folderChange(event) {
			this.$http.patch('/api/works/folder', {
				work_oid: this.clicked_image._id,
				folder_oid: event.target.value
			})
			.then((response) => {	// eslint-disable-line no-unused-vars
				this.getFolderList();
			})
			.catch((err) =>{
				this.workData = err;
			})
        },
		getFolderList() {
			// 폴더들 가져옴
			this.$http.get(`/api/folders?user_oid=${this.user_oid}`)
				.then((response) => {
					this.folderList.push({ folderName: '(폴더 없음)', _id: '' })
					this.folderList = this.folderList.concat(response.data);
				}).catch((err) =>{
					console.log(err);
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
.folder-select {
	border: none !important;
	margin-bottom: 1rem;
}
</style>

