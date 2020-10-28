<template>
	<div class = "upload">
		<div class="waiting" v-if="waiting">
			<div class="waiting-notice">
				<img src="../images/sync.svg" class="sync-image"/>
				처리중입니다.. 잠시만 기다려주세요.
			</div>
		</div>
		<b-alert v-model="showDismissibleAlert" variant = "success"  dismissible>
			파일이 업로드 되었습니다!
		</b-alert>
		<div class="progressbar">
			<button v-on:click="step=0" v-bind:class="{'now': step===0, 'active': step > 0}">업로드</button>
			<button v-on:click="step=1" v-bind:class="{'now': step===1, 'active': step > 1}">수정</button>
			<button v-on:click="step=2" v-bind:class="{'now': step===2, 'active': step > 2}">필터링</button>
			<button>다운로드</button>
		</div>
		<div class = "wrap" v-if="step === 0">
			<div class="helper"></div>
			<div class="drop display-inline align-center"
				v-bind:style = "{background : color}"
				@dragover.prevent  = "onOver"
				@dragleave.prevent = "onLeave"
				@drop="onDrop">
				<div class="helper"></div>
				<img v-if="!image" class="upload-image" src="../images/image-upload.svg"/>
				<label v-if="!image" class="btns ready-btn display-inline">
					이곳에 이미지를 드래그하거나 선택해주세요
					<input type="file" name="image" @change="onChange">
				</label>
				<div class="hidden display-inline align-center" v-else v-bind:class="{'image': true }">
					<div class = "file-preview-wrapper">
						<img :src="image" alt="" class="img" />
						<div class="file-close-button" @click="removeFile" v-if="image">x</div>
					</div>
					<button class="btns" @click="uploadFile">전송</button>
					<button class="btns" @click="nextFile">다음</button>
					
				</div>
			</div>

			<button class="move_btn" @click = "step=1" v-if="isGet && image">＞</button>			
			<button class="move_btn" @click = "nextFile" v-if="image && !isGet">＞</button>
		</div>
		
		<div class="container fix-section" v-else-if="step===1">
			<div class="wrap">
				<div class ="wrap_btn" style = "float:left;">
					<button class="move_btn" @click = "step=0" v-if="image">＜</button>
				</div>
				<div class="row" style="margin : 0 auto;">
					<div class="col-md-8">
						<div class="target-panel">
							<img class="target-image" :src="image" @load = "getSize(image)"/>
						</div>
					</div>
					<div class="col-md-4">
						<div class="setting-panel">
							<p class="setting-comment" v-on:click="openScorePanel = !openScorePanel">인식률 <span class="show-value">{{ selectedData.score }}</span></p>
							<div class="setting-detail" v-if="openScorePanel">
								<p class="setting-desc">로고로 인식할 추적 점수의 최소값</p>
								<b-form-group style="margin-top: 1rem;">
									<b-form-radio-group
										v-model="selectedData.score"
										:options="options"
										name="radio-inline"
									></b-form-radio-group>
								</b-form-group>
								<input v-model="selectedData.score" type="range" class="custom-range" min="0" max="1" step="0.1" id="scoreRange">
							</div>
							<hr/>
							<p class="setting-comment" v-on:click="openNMSPanel = !openNMSPanel">NMS <span class="show-value">{{ selectedData.nms }}</span></p>
							<div class="setting-detail" v-if="openNMSPanel">
								<p class="setting-desc">Non-Maximum Suppression에서 사용할 IoU(Intersection over Union)의 threshold 값</p>
								<b-form-group style="margin-top: 1rem;">
									<b-form-radio-group
										v-model="selectedData.nms"
										:options="options"
										name="radio-inline"
									></b-form-radio-group>
								</b-form-group>
								<input v-model="selectedData.nms" type="range" class="custom-range" min="0" max="1" step="0.1" id="nmsRange">
							</div>
						</div>
						<button class="btn btn-primary btn-re" v-on:click="nextFile" :disabled="compareSelectedData()">변경된 데이터로 이미지 새로고침</button>
						<!-- <div class="list-panel">
							<p class = "setting-comment">객체 정보</p>
							<button class="btn sample-btn" v-for="(pData, idx) in predictData" :key="idx" v-on:click="pData.check = !pData.check">
								<img class="check" v-bind:src="pData.check ? require('@/images/check.svg') : require('@/images/uncheck.svg')"/>
							</button>
						</div> -->
					</div>
				</div>
				<div class ="wrap_btn" style="float : right;">
					<button class="move_btn" @click = "filterFile" v-if="image">＞</button>
				</div>
			
				</div>
				<div class="row" style="margin-top:2rem;">
					<div class="col-md-12">
						<div class="lists-section">
							<div class="sample-div"
								v-for="(pData, idx) in predictData"
								:key="idx"
								v-on:click="pData.check = !pData.check"
								:class="{ 'unactive' : !pData.check }"
								:style="{ 'width': divSize(pData.pos[2], pData.pos[0]), 'height': divSize(pData.pos[3], pData.pos[1]) }">
								<img class="sample-image"
									:src="image"
									alt="Card image"
									:style="{ 'width' : setw, 'height' : seth, 'left': imagePos(pData.pos[0]), 'top': imagePos(pData.pos[1]) }">
								<img class="check" v-bind:src="pData.check ? require('@/images/check.svg') : require('@/images/uncheck.svg')"/>
							</div>
						</div>
					</div>
				</div>
		</div>
		<div class="container" v-if="step === 2">
			<div class="wrap">
				<img :src="receiveimage" class="filtered-image">
			</div>
		</div>
	</div>
</template>

<script>
export default{
    data(){
		return {
			color : '#ffffff',
			image : '',
			sendFile : '',
			file1 : null,
			showDismissibleAlert: false,
			step: 0,
			waiting: false,
			isGet : false,
			predictData: [],
			selectedData: {
				score: 0,
				nms: 0.2,
			},
			baseSelectedData: {
				score: 0,
				nms: 0.2,
			},
			openScorePanel: false,
			openNMSPanel: false,
			options: [
				{ text: '낮음', value: 0.2 },
				{ text: '중간', value: 0.5 },
				{ text: '높음', value: 0.8 },
				{ text: '매우높음', value: 1 }
			],
			setw : '',
			seth : '',
			receiveimage : '',
		}
	},
	created(){
		this.image = '';
		this.sendfile = '';
	},
    methods: {
		onOver(){
			this.color = 'gray'
		},
		onLeave(){
			this.color = 'white'
		},
        onDrop(e){
			this.color = 'white'
			e.stopPropagation();
			e.preventDefault();
			this.isGet = false;
			var files = e.dataTransfer.files;
			this.createFile(files[0]);
        },
        onChange(e) {
			var files = e.target.files;
			this.createFile(files[0]);
        },
        createFile(file) {
			if (!file.type.match('image.*')){
				alert('이미지 파일을 선택해주세요');
				return;
			}
			// var img = new Image();
			var reader = new FileReader();
			var vm = this;

			reader.onload = function(e) {
				vm.image = e.target.result;
            }
            reader.readAsDataURL(file);
			this.sendFile = file;
			console.log(this.sendFile);
        },
        removeFile() {
            this.image = '';
			this.sendfile = '';
        },
		uploadFile(){
			if(this.sendFile == ''){
				alert('업로드할 이미지가 없습니다.');
				return false;
			}
			
			const formData = new FormData();
			const userid = sessionStorage.getItem('userid');
			formData.append('imgUploads',this.sendFile);
			formData.append('userid',userid);
			this.$http.post('/api/upload',formData,{
				headers : {
					'Content-Type' : 'multipart/form-data'
				}
			}).then((res) =>{
				console.log(res);
				this.image = '';
				this.sendfile = '';
				this.showDismissibleAlert = true;
			}).catch((err)=>{
				console.log(err);
			});
		},
		nextFile(){
			if(this.sendFile == ''){
				alert('업로드할 이미지가 없습니다.');
				return false;
			}
			this.predictData = [];
			this.waiting = true;
			
			const formData = new FormData();
			formData.append('file', this.sendFile);
			
			this.$http.post(`https://osam2020-4gb-uokiv.run.goorm.io/predict?visualize=none&score_threshold=${this.selectedData.score}&nms_iou_threshold=${this.selectedData.nms}`,formData,{
				headers : {
					'Content-Type' : 'multipart/form-data'
				}
			}).then((res) =>{
				res.data.boxes.forEach((e, idx) => {
					this.predictData.push(
						{
							pos: [ e[0], e[1], e[2], e[3] ],
							check: true,
							scored: res.data.scores[idx]
						}
					);
				});
				this.waiting = false;
				this.step = 1;
				this.isGet = true;
				this.baseSelectedData.score = this.selectedData.score;
				this.baseSelectedData.nms = this.selectedData.nms;
			}).catch((err)=>{
				console.log(err);
				this.waiting = false;
			});
		},
		filterFile(){
			if(this.sendFile == ''){
				alert('필터링할 이미지가 없습니다.');
				return false;
			}
			// TODO : [ [], []. [] ] 처럼 만들기
			// 지금 ; [ [], [], [], ]
			this.waiting = true;
			let passposes = [];
			for(var i = 0; i<this.predictData.length; i++){
				if(this.predictData[i].check){
					passposes.push('[' + this.predictData[i].pos.join(',') + ']');
				}
			}
			passposes = '[' + passposes.join(',') + ']';
			
			const formData = new FormData();
			formData.append('file', this.sendFile);
			formData.append('boxes', passposes);
			console.log(passposes);
			// '[' + [1, 2, 3].join(',') + ']'

			let self = this;
			fetch('https://osam2020-4gb-uokiv.run.goorm.io/blur', {
				method: 'POST',
				body: formData
			}).then(function(response) {
				console.log(response);
				return response.blob();
			}).then(function(blob) {
				console.log(blob);
				const objURL = URL.createObjectURL(blob);
				// image.src = objURL;
				console.log(objURL);
				self.receiveimage = objURL;
				
				self.waiting = false;
				self.step = 2;
			});
		},
		getSize(src){
			var img = new Image();
			img.src = src;
			this.setw = img.width;
			this.seth = img.height;
		},
		divSize(maxPos, minPos) {
			return (maxPos - minPos) + 'px';
		},
		imagePos(pos) {
			return '-' + pos + 'px';
		},
		compareSelectedData() {
			return this.selectedData.score == this.baseSelectedData.score && this.selectedData.nms == this.baseSelectedData.nms;
		}
    }
 }
</script>

<style lang="scss">
html, body {
  height: 100%;
}
.wrap {
	margin: 2% auto;
    position: relative;
}
.upload {
	background-color: #f1f5f6 !important;
	padding-bottom: 5rem;
}
.upload-image {
	width: 5rem;
	position: absolute;
    top: 40%;
    left: 50%;
	opacity: .5;
    transform: translate(-50%, -40%);
}
.btns {
  background-color: #5f5fff;
  border: 0;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-weight: bold;
  padding: 15px 35px;
  position: relative;
  border-radius: .25rem;
}
	.move_btn{
		border-radius : 50%;
		background-color: #5f5fff;
		color : #fff;
		font-weight: bold;
		padding: 10px;
		border : 0;
		cursor: pointer;
		margin-left : 3px;
		display : inline-block;
	}
.btns.ready-btn {
	margin-top: 8rem;
}
.btns:hover {
  background-color: #212b6b;
}

input[type="file"] {
  position: absolute;
  opacity: 0;
  z-index: -1;
  left: 0px;
}

.align-center {
  text-align: center;
}

.helper {
  height: 300px;
  display: inline-block;
  vertical-align: middle;
  width: 0;
}

.hidden {
  display: none !important;
}

.hidden.image {
  display: inline-block !important;
}

.display-inline {
  display: inline-block;
  vertical-align: middle;
}

.img {
	position: relative;
	width: 190px;
	height: auto;
    z-index: 10;
}

.drop {
	position: relative;
  background-color: #f2f2f2;
  border: 4px dashed #ccc;
  background-color: #f6f6f6;
  border-radius: 15px;
  height: 100%;
  max-height: 400px;
  max-width: 500px;
  width: 100%;
}
.file-close-button {
    position: absolute;
    /* align-items: center; */
    line-height: 18px;
    z-index: 99;
    font-size: 18px;
    right: 5px;
    top: 10px;
    color: #fff;
    font-weight: bold;
    background-color: #666666;
    width: 20px;
    height: 20px;
    text-align: center;
    cursor: pointer;
}
.file-preview-wrapper {
    padding: 10px;
    position: relative;
}
.file-preview-wrapper img {
	width: auto;
	max-width: 100%;
	max-height: 220px;
}
.progressbar {
 counter-reset: step;
	margin-top: 5%;
	margin-bottom: 3rem;
	min-height: 74px;
}
.progressbar button {
 list-style-type: none;
 float: left;
 width: 25%;
 position: relative;
 text-align: center;
 font-weight: 400;
 color: #a5a5a5;
 background-color: transparent;
 border: 0px;
 cursor: pointer;
	z-index: 4;
}
.progressbar button:focus {
 outline: none;
}
.progressbar button:before {
 content: counter(step);
 counter-increment: step;
 counter-increment: step;
 width: 40px;
 height: 40px;
 line-height: 40px;
 border: 1px solid #ddd;
 display: block;
 font-size: 22px;
 font-weight: 600;
 text-align: center;
 color: #a5a5a5;
 margin: 0 auto 10px auto;
 border-radius: 50%;
 background-color: white;
	// z-index: 1;
}
.progressbar button:after {
 content: '';
 position: absolute;
 width: 50%;
 height: 2px;
 margin-top: 3px;
 background-color: #c3c3c3;
 top: 15px;
 left: -25%;
 z-index: -1;
}
.progressbar button:first-child:after {
 content: none;
}
.progressbar button.now {
 font-weight: 700;
}
.progressbar button.now:before {
 /* color: white; */
 color: white !important;
 background-color: #5f5fff;
}
.progressbar button.active, .progressbar button.now {
 color: #5f5fff;
}
.progressbar button.active::before, .progressbar button.now::before {
 color: #5f5fff;
 border-color: #5f5fff;
}
.progressbar button.active + :after {
 background-color: #5f5fff;
}

.fix-section {
	text-align: left;
	.target-panel {
		padding: 1rem;
		background-color: white;
		border-radius: .25rem;
		.target-image {
			width: auto;
			max-width: 100%;
			max-height: 50vh;
		}
	}
	.setting-panel{
		padding : 1rem;
		background-color : white;
		border-radius : .25rem;
		// margin-bottom : 2rem;
		span{
			all : unset;
		}
	}
	.list-panel {
		padding: 1rem;
		background-color: white;	
		border-radius: .25rem;
		.sample-image {
			width: 3rem;
		}
		.sample-btn {
			display: flex;
			justify-content: space-between;
			width: 100%;
			align-items: center;
			padding: 0px;
			&.sample-btn {
				margin-bottom: .5rem;
			}
			.check {
				width: 3rem;
			}
		}
	}
}
.filtered-image {
	max-width : 100%;
}
.setting-comment {
	font-weight : bold;
	padding-top: 1rem;
	padding-bottom: 1rem;
	cursor: pointer;
	transition: background .5s;
	&:hover {
		background-color : #ebebff;
	}
}
.setting-desc {
	font-size: .8rem;
}
.setting-detail {
	// padding-bottom: 1rem;
}
.lists-section {
	padding: 1rem;
	background-color: white;
	border-radius: .25rem;
	// 	어떻게 이쁠게 못쓸까 해서 일단 넣어봄 flex.. 정말 안이쁘다.
    display: flex;
    flex-wrap: wrap;
    flex: 1 1 auto;
    align-items: center;
    align-content: space-around;
    justify-content: space-around;
}
.sample-div {
	// border: 1px solid red;
	display: inline-block;
	width: 110px;
	height: 85px;
	overflow: hidden;
	position: relative;
	box-shadow: 0px 0px 10px 0px #929292;
	cursor: pointer;
	.sample-image {
		position: absolute;
		left: -70px;
		top: -31px;
		z-index: 2;
	}
	.sample-bg {
		width: 2rem;
		height: 2rem;
		background-color: tomato;
		z-index: 1;
		position: absolute;
		border-top-left-radius: 1rem;
		right: 0px;
		bottom: 0px;
	}
	.check {
		position: absolute;
	}
	&.unactive {
		opacity: .5;
	}
}
	
.waiting {
	position: fixed;
	top: 0px;
	width: 85%;
	height: 100%;
	z-index: 100;
	background: rgba(0, 0, 0, .7);
	.sync-image {
		width: 1rem;
		animation: rotation 2s infinite linear;
		margin-right: .5rem;
	}
	.waiting-notice {
		position: absolute;
		bottom: 10rem;
		left: 50%;
		transform: translate(-50%, 0px);
		color: white;
		background: #5f5fff;
		padding: 1rem 2.5rem 1rem 2rem;
		border-radius: .5rem;
	}
}
.btn-re {
	padding-top: .75rem !important;
	padding-bottom: .75rem !important;
	width: 100% !important;
	border-radius: 0px 0px .25rem .25rem !important;
	margin-bottom: 2rem;
}
.show-value {
	font-weight: 500 !important;
	margin-left: .5rem !important;
}
@keyframes rotation {
	from {
		transform: rotate(359deg);
	}
	to {
		transform: rotate(0deg);
	}
}
</style>