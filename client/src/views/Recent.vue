<template>
  <div class="recent">
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
		<WorkData v-else-if="showWorkedData" @cancelWorkData="cancelWorkData" :clicked_image="clicked_image" :beforeComponent="'최근 작업내역'"></WorkData>
	</div>
  </div>
</template>

<script>
import WorkData from '@/components/WorkData.vue'
	
export default {
	name: 'Recent',
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
			showWorkedData: false,
			inviteEmail: ''
		}
	},
	methods : {
		inviteFolder() {
			console.log('invite');
		},
		click_image (src){
			src.user_oid = sessionStorage.getItem("user_oid");
			this.clicked_image = src;
			// this.$bvModal.show('bv-modal-example');
			this.showWorkedData = true;
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
		cancelWorkData() {
			this.showWorkedData = false;
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
	components: {
		WorkData
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
	.recent {
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
		width: 1rem;
		margin-right: .5rem;
	}
</style>
