<template>
  <div class="main">
	<div>
		<div class="recent-worked" v-if="!showWorkedData">
			<h2 class="recent-title">최근 작업내역</h2>
			<div class="menu-box"> 
				<button class="btn" v-on:click="clickDown" :disabled="checkedList==''">
					<img src = "../images/import.svg" class="btn_image"/>
					다운로드
				</button>
				<button class="btn" v-on:click="clickDel"  :disabled="checkedList==''">
					<img src = "../images/trash-alt.svg" class="btn_image">
					삭제
				</button>
			</div>
			<b-card-group deck>
				<div v-for="(list,idx) in lists" :key="idx" class = "wrap_cards">
					<b-card
						class = "showing_image"
						v-if="list"
					>
						<b-card-text>
							<input type="checkbox" v-bind:id="'check'+idx" v-bind:value="list" v-model="checkedList">
							{{list.fileName}}
						</b-card-text>
						<b-card no-body
							:img-src = "serverUrl + list.fileName" 
							@click="click_image(list)"
							style = "cursor : pointer; margin: 0px;"
							img-alt="Image"
							img-width = "auto"
							img-height = "250rem"
							img-top>
						</b-card>
						<b-card-text>
						</b-card-text>
							<template #footer>
								<small class="text-muted">Last updated at <br>{{list.workedAt}}</small>
							</template>
					</b-card>
				</div>
			</b-card-group>
			<div class = "wrap_pagination">
				<div class ="load_page">
					<b-pagination
						:total-rows="totalRows" 
						v-model="currentPage"
						:per-page="perPage"
					/>
				</div>
			</div>
		</div>
		<div class="container data-section" v-else-if="showWorkedData">
			<button class="btn before-btn" v-on:click="showWorkedData = false;">
				<div class="before-btn-circle">
					<p>＜</p>
				</div>
				최근 작업내역</button>
			<h3 style="text-align:left;">{{clicked_image.fileName}}</h3>
			<div class="row">
				<div class="col-md-8">
					<div class="data-image">
						<img class="worked-image" v-if="workData[0]" v-bind:src="serverUrl + clicked_image.fileName"/>
					</div>
				</div>
				<div class="col-md-4">
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
			<button class="btn" v-on:click="downloadWork(clicked_image.fileName)" style="float:right; background-color:white;">
				<img src = "../images/import.svg" class="btn_image"/>
				다운로드
			</button>
			<button class="btn" v-on:click="removeWork(clicked_image._id, clicked_image.fileName)" style="float:right; background-color:white; margin-right:1rem;">
				<img src = "../images/trash-alt.svg" class="btn_image">
				삭제
			</button>
		</div>
		<!-- <b-modal id="bv-modal-example" hide-footer size = "xl">
			<template #modal-title>
				{{clicked_image.fileName}}
			</template>
			<div style = "text-align : center; height : 500px;">
				<img class="worked-image" v-if="workData[0]" v-bind:src="serverUrl + clicked_image.fileName"/>
			</div>
			<button v-on:click="downloadWork(clicked_image.fileName)" class="btn btn-primary float-right">다운로드</button>
			<button v-on:click="removeWork(clicked_image._id, clicked_image.fileName)" class="btn btn-danger float-right">삭제</button>
		</b-modal> -->
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
			workData : '',
			finduser : this.$route.params.userid,
			perPage: 5,
			currentPage: 1,
			clicked_image : '',
			user_id : '',
			checkedList : [],
			showWorkedData: false
		}
	},
	methods : {
		click_image (src){
			this.clicked_image = src;
			// this.$bvModal.show('bv-modal-example');
			this.showWorkedData = true;
		},
		removeWork(work_oid, fileName) {
			this.$http.post(`/api/works/delete/${this.user_id}`, {
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
		clickDel(){
			const f = this.checkedList;
			var isok = confirm("정말"+f.length+"개의 파일을 삭제하시겠습니까?");
			if(isok){
				for(var i =0;i<f.length;i++){
					this.removeWork(f[i]._id,f[i].fileName);
				}
				alert("파일이 삭제되었습니다.");
				this.checkedList = [];
			}
		},
		clickDown(){
			const f= this.checkedList;
			var isok = confirm("정말"+f.length+"개의 파일을 다운로드하시겠습니까?");
			if(isok){
				for(var i =0;i<f.length;i++){
					this.downloadWork(f[i].fileName);
				}
				this.checkedList = [];
			}
		}
	},
	created () {
		var userid = sessionStorage.getItem("userid");
		this.user_id = userid;
		var skip = 0;	// 뛰어넘기	(default 0)
		var limit = 100;	// 개수	(default 5)
		var sort = -1;	// -1 최신순부터, 1 예전순부터 (default -1)
		
		this.$http.get(`/api/works/${userid}/?skip=${skip}&limit=${limit}&sort=${sort}`)
			.then((response) => {
				this.workData = response.data;
				if (this.workData.length > 0) {
					// 작업물이 한개 이상이라도 있으면
					this.rows = this.workData.length;
				}
			})
			.catch((err) =>{
				this.workData = err;
			})
	},
	computed: {
    lists () {
      const items = this.workData;
      // Return just page of items needed
      return items.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      )
    },
    totalRows () {
      return this.workData.length;
    }
  }
}
</script>
<style lang="scss">
	.main {
		padding: 5rem;
		background-color :  #f1f5f6 !important;
		position: relative;
	}
	.worked-image {
		// height: 500px;
		width: auto;
		max-width: 100%;
		display : inline-block;
		// margin : 0 auto;
	}
	.wrap_pagination{
		text-align : center;
		margin-top : 1rem;
	}
	.load_page span{
		bottom : 0;
		font-size : 1rem;
	}
	.load_page{
		margin : 0 auto;
		display : inline-block;
	}
	.recent-worked {
		text-align: left;
	}
	.recent-worked .recent-title {
		font-weight: 700;
	}
	.recent-worked .worked-list {
		padding: 1rem;
		align-items: center;
	}
	.menu-box {
		background-color: #f1f5f6 !important;
		width : 60vw;
		height : 35px;
		margin-bottom : 3rem;
		margin-top : 2rem;
		border-radius : 20px;
		.btn {
			background-color: white !important;
			& + .btn {
				margin-left: 1rem;
			}
		}
	}
	.showing_image{
		height : 30rem;
		max-width : 15rem;
		
	}
	.wrap_cards{
		margin-top : 5px;	
	}
	.card-title {
		font-size: 1rem;
	}
	.btn_image {
		width : 1rem;
		cursor : pointer;
		margin-right : .5rem;
	}
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
</style>
