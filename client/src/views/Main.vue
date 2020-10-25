<template>
  <div class="main">
	<div>
		<div class="recent-worked">
			<h2 class="recent-title">Recently work</h2>
			<b-card-group deck>
				<div v-for="(list	,idx) in lists" :key="idx" class = "wrap_cards">
					<b-card
						class = "showing_image"
						v-if="list"
						:title="list.fileName"
					>
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
							<!-- <img src = "../images/trash-alt.svg" v-on:click = "removeWork(list._id, list.fileName)" class = "btn_image">
							<img src = "../images/import.svg" v-on:click="downloadWork(list.fileName)" class = "btn_image"> -->
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
		<b-modal id="bv-modal-example" hide-footer size = "xl">
			<template #modal-title>
				{{clicked_image.fileName}}
			</template>
			<div style = "text-align : center; height : 500px;">
				<img class="worked-image" v-if="workData[0]" v-bind:src="serverUrl + clicked_image.fileName"/>
			</div>
			<button v-on:click="downloadWork(clicked_image.fileName)" class="btn btn-primary float-right">다운로드</button>
			<button v-on:click="removeWork(clicked_image._id, clicked_image.fileName)" class="btn btn-danger float-right">삭제</button>
		</b-modal>
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
		}
	},
	methods : {
		click_image (src){
			this.clicked_image = src;
			this.$bvModal.show('bv-modal-example');
		},
		removeWork(work_oid, fileName) {
			var isok = confirm("정말 파일을 삭제하시겠습니까?");
			if(isok){
				this.$http.post(`/api/works/delete/${this.user_id}`, {
						work_oid: work_oid,
						fileName: fileName
					})
					.then((response) => {
						console.log(response.data);
						alert('파일이 삭제되었습니다.');
						location.reload();
					})
					.catch((err) =>{
						this.workData = err;
					})
			}
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
<style>
	.main {
		padding: 5rem;
	}
	.worked-image {
		height: 500px;
		display : inline-block;
		margin : 0 auto;
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
		width : 2vw;
		float : right;
		padding-top : 3vw;
		cursor : pointer;
	}
</style>
