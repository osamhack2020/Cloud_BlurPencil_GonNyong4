<template>
	<div class = "upload">
		<b-alert v-model="showDismissibleAlert" variant = "success"  dismissible>
			파일이 업로드 되었습니다!
		</b-alert>
		<div class = "wrap">
			<div class="helper"></div>
			<div class="drop display-inline align-center"
				v-bind:style = "{background : color}"
				@dragover.prevent  = "onOver"
				@dragleave.prevent = "onLeave"
				@drop="onDrop">
				<div class="helper"></div>
					<label v-if="!image" class="btns display-inline">
						이곳에 이미지를 드래그하거나 선택해주세요
						<input type="file" name="image" @change="onChange">
					</label>
				<div class="hidden display-inline align-center" v-else v-bind:class="{ 			'image': true }">
					<div class = "file-preview-wrapper">
						<img :src="image" alt="" class="img" />
						<div class="file-close-button" @click="removeFile" 								v-if="image">x</div>
					</div>
					<button class="btns" @click="uploadFile">전송</button>
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
		}
    }
 }
</script>

<style>
html, body {
  height: 100%;
}
.wrap {
	margin : 2% auto;
    position: relative;
}
.btns {
  background-color: #d3394c;
  border: 0;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-weight: bold;
  padding: 15px 35px;
  position: relative;
}

.btns:hover {
  background-color: #722040;
}

input[type="file"] {
  position: absolute;
  opacity: 0;
  z-index: -1;
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
</style>