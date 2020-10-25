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
				<div class="hidden display-inline align-center" v-else v-bind:class="{ 			'image': true }">
					<div class = "file-preview-wrapper">
						<img :src="image" alt="" class="img" />
						<div class="file-close-button" @click="removeFile" 								v-if="image">x</div>
					</div>
					<button class="btns" @click="uploadFile">전송</button>
					<button class="btns" @click="nextFile">다음</button>
				</div>
			</div>
		</div>
		
		<div class="container fix-section" v-else-if="step===1">
			<div class="row">
				<div class="col-md-8">
					<div class="target-panel">
						<img class="target-image" :src="image"/>
						인식률 : <a href="#">높음</a> <a href="#">중간</a> <a href="#">낮음</a> (이런식으로 선택 가능하게?)
					</div>
				</div>
				<div class="col-md-4">
					<div class ="score-panel">
						<p class = "setting-comment">인식률</p>
						<b-form-group>
							<b-form-radio-group
								v-model="selected"
								:options="options"
								name="radio-inline"
							></b-form-radio-group>
						</b-form-group>
					</div>
					<div class="setting-panel">
						<p class = "setting-comment">객체 정보</p>
						<button class="btn sample-btn" v-for="(pData, idx) in predictData" :key="idx" v-on:click="pData.check = !pData.check">
							<!-- <img class="sample-image" src="https://i.pinimg.com/originals/17/0d/f9/170df908bff9619457df64f5d4072a54.jpg"/> -->
							<!-- <div class="sample-div">
								<img class="sample-image2" :src="image"/>
							</div> -->
							<!-- <img class="sample-image" :style="{ 'position': 'absolute',  'clip': clipRect(pData.pos) }"  :src="image"/> -->
							<img class="check" v-bind:src="pData.check ? require('@/images/check.svg') : require('@/images/uncheck.svg')"/>
						</button>
					</div>
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
								src="https://i.ytimg.com/vi/7k7Ki7JlKf4/maxresdefault.jpg"
								alt="Card image"
								:style="{ 'left': imagePos(pData.pos[0]), 'top': imagePos(pData.pos[1]) }">
							<img class="check" v-bind:src="pData.check ? require('@/images/check.svg') : require('@/images/uncheck.svg')"/>
						</div>
					</div>
				</div>
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
			predictData: [],
			selected: '',
			options: [
				{ text: '낮음', value: 'low' },
				{ text: '중간', value: 'mid' },
				{ text: '높음', value: 'high' }
			]
		}
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
			this.waiting = true;
			const formData = new FormData();
			formData.append('file', this.sendFile);
			this.$http.post('https://osam2020-4gb-uokiv.run.goorm.io/predict?visualize=none&score_threshold=0.5',formData,{
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
			}).catch((err)=>{
				console.log(err);
				this.waiting = false;
			});
		},
		clipRect(pData) {
			return `rect(${pData[0]}, ${pData[1]}, ${pData[2]}, ${pData[3]})`;
		},
		divSize(maxPos, minPos) {
			return (maxPos - minPos) + 'px';
		},
		imagePos(pos) {
			return '-' + pos + 'px';
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
}
.progressbar button:after {
 content: '';
 position: absolute;
 width: 100%;
 height: 2px;
 margin-top: 3px;
 background-color: #a5a5a5;
 top: 15px;
 left: -50%;
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
	.score-panel{
		padding : 1rem;
		background-color : white;
		border-radius : .25rem;
		margin-bottom : 2rem;
		span{
			all : unset;
		}
		.setting-comment{
			font-weight : bold;
		}
	}
	.setting-panel {
		padding: 1rem;
		background-color: white;	
		border-radius: .25rem;
		.setting-comment{
			font-weight : bold;
		}
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
	.lists-section {
		padding: 1rem;
		background-color: white;
		border-radius: .25rem;
	}
		.sample-div {
			border: 1px solid red;
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
				width: 1280px;
				height: 720px;
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
	
@keyframes rotation {
	from {
		transform: rotate(359deg);
	}
	to {
		transform: rotate(0deg);
	}
}
</style>