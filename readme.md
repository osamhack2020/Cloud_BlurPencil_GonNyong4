
<p align="center">
  <img src="./client/src/images/logo.png" width="125"/>
</p>
<br/>
<p align="center">
  자동 검열 모자이크 서비스, <strong>BLUR PENCIL</strong>
  <br/>  
 빠르고 편리한 자동 검열 기능을 통해 취약한 보안을 강화하고 저작권 침해를 예방합니다.
</p>

<p align="center">
 <img src="https://img.shields.io/github/repo-size/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge"/>
 <img src="https://img.shields.io/github/license/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge"/>
 <a href="http://20.194.22.218:8080/">
 	<img src="https://img.shields.io/badge/LIVE-DEMO-%235f5fff?style=for-the-badge"/>
 </a>
</p>

## 📖 프로젝트 소개

![프로젝트 설명 이미지](./intro.png)
<br>
<p><strong>Blur Pencil</strong>은 Blur와 Pencil을 합친 단어로, 모자이크 처리 하고 싶은 이미지를 Pencil(연필)과 같은 우리에게 익숙한 도구로 간단하고 쉽게 Blur처리 하기 위해 고안한 아이디어 입니다. 접근하기 편리한 웹을 통해 이미지를 드래그 앤 드랍만 하면, 학습된 Blur Pencil이 이미지를 분석한 뒤, 모자이크 할 객체를 인식하며, 인식된 객체 중 원하는 객체를 골라 모자이크 처리를 할 수 있습니다. 또한 모자이크 처리 된 이미지 내역들을 저장할 수 있으며, 다른 사용자와 공유할 수 있도록 도와줍니다.</p>

<table>
	<tr>
		<td>
			<a href="https://www.youtube.com/watch?v=Dpo0IvrmeTA&feature=youtu.be"><img src="images/goyoutube.png"></a>
		</td>
		<td>
			<a href="https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/blob/master/PPT/Blur%20Pencil%20%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pptx"><img src="images/goppt.png"></a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<b>소개 영상</b>
		</td>
		<td align="center">
			<b>발표 자료</b>
		</td>
	</tr>
</table>

## 📄 기능 설계 및 가이드
### Figma Proto-typing
> 이미지 클릭 시 이동
[![Figma](images/Figma.png)](https://www.figma.com/file/ZokPcCmd6r5E2HvDRCOfDb/OSAM-HACK-2020-Blur-Pencil?node-id=0%3A1)

### 구조
![구조](images/archi.png)

### 설계
![설계](images/archi2.png)

### API 가이드(유저 관련)
[📝 가이드 문서](https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/wiki/API-Guide)

### API 가이드(로고 인식 관련)
[📝 가이드 문서](https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/wiki/API-Guide-(Logo-Detection))


## ⚙ 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)
- 권장 : 최신 버전의 크로미움 기반 브라우저

## 🔧 기술 스택 (Technique Used)
### Server(back-end)
 - Node.js
 - Express
 - MongoDB
 - Flask
 - PyTorch
 
### front-end
 -  Vue.js
 -  Bootstrap

## ⛏ 설치 안내 (Installation Process)
> MongoDB 및 node.js 설치는 되어 있다는 가정하에 진행합니다.

```bash
$ git clone https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4.git
```

### Back-End
```bash
$ cd server/
$ npm install
```

### Build / Test
```bash
$ (root) npm start
```

### 세팅시 유의 사항
1. [vue.config.js](https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/blob/master/client/vue.config.js) 안에 '/api' `target` 주소를 서버주소(로컬 환경시 서버포트)로 변경
2. [main.js](https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/blob/master/client/src/main.js) 안에 `serverUrl` 변수명을 서버주소(로컬 환경시 서버포트)로 변경

> 구름 IDE 환경으로 개발시 로컬 주소가 아닌 URL 주소를 직접 입력해 주어야함

## 👨‍💻 팀 정보 (Team Information)
<table>
  <tr>
    <td align="center">
     <a href="https://github.com/hughesgoon">
      <img src="https://avatars.githubusercontent.com/u/45625362?v=3" width="100px;" alt=""/>
      <br />
      <sub>
       <b>김현재</b>
      </sub>
     </a>
     <br />
      <sub>
       <b>팀장</b>
      </sub>
     <p>hyeonjae.dev@gmail.com</p>
   </td>
    <td align="center">
     <a href="https://github.com/kyechan99">
      <img src="https://avatars.githubusercontent.com/u/14146566?v=3" width="100px;" alt=""/>
      <br />
      <sub>
       <b>강예찬</b>
      </sub>
     </a>
     <br />
      <sub>
       <b>팀원(Full Stack)</b>
      </sub>
     <p>kyechan99@gmail.com</p>
   </td>
    <td align="center">
     <a href="https://github.com/kyechan99">
      <img src="https://avatars.githubusercontent.com/u/15906101?v=3" width="100px;" alt=""/>
      <br />
      <sub>
       <b>배성준</b>
      </sub>
     </a>
     <br />
      <sub>
       <b>팀원(Front-End)</b>
      </sub>
     <p>clcc001@naver.com</p>
   </td>
    <td align="center">
     <a href="https://github.com/seungpyo">
      <img src="https://avatars.githubusercontent.com/u/7239579?v=3" width="100px;" alt=""/>
      <br />
      <sub>
       <b>홍승표</b>
      </sub>
     </a>
     <br />
      <sub>
       <b>팀원(Pytorch, CV)</b>
      </sub>
     <p>spkbk98@gmail.com</p>
   </td>
  </tr>
 </table>
 <br><br>

## Blur Pencil 사용법
### STEP 1
<p>사진을 Drag and Drop해서 올린다.</p>
<img src ="images/1.png" width = "1024">

### STEP 2

<p>인식된 객체 중 모자이크 할 객체를 선택한다.</p>
<img src ="images/2.png" width = "1024">

### STEP 3

<p>모자이크 처리 된 이미지를 확인 후 다운로드 한다.</p>
<img src ="images/3.png" width = "1024">

### 로그인 없이 무료로 사용 가능
<img src ="images/strength1.png" width = "1024">
<br>

### 폴더 기능
<p>작업한 이미지들을 폴더 별로 나누어 저장할 수 있으며 다른 유저와 공유도 할 수 있습니다.</p>

<strong>메인 페이지</strong>
<img src ="images/prev_dash.png" width = "1024">
<br>
<strong>폴더 저장</strong>
<img src ="images/strength_folder.png" width = "1024">
<br>
<strong>폴더 공유</strong>
<img src ="images/strength_share.png" width = "1024">
<br>
<strong>파일 관리</strong>
<img src ="images/strength_multi.png" width = "1024">
<br><br>

## 💻 DEMO
> 더 많은 테스트 케이스를 `demo` 폴더에서 확인하실 수 있습니다.
<p align="center">
<p align="left">

### Demo Image 1

</p>
<img src = "./example1.png" width = "1024">
<p align="left">

### Demo Image 2

</p>
<img src = "./example2.png" width = "1024">
<p align="left">

### Demo Image 3

</p>
<img src = "./example3.png" width = "1024">
<p align="left">

### Functions
![](demo/mypage.png)
![](demo/foldername.png)
![](demo/goonin.png)
![](demo/sharefolder.png)

## Blur Pencil 기대 효과
- 빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해 등을 보완할 수 있다.
- 강력한 보안을 필요로 하는 개인이나 집단, 저작권 보호를 중요시하는 단체에게 Blur Pencil의 기술을 통해 업무 성능 향상을 도와준다.
- 인식률(score)과 NMS(Non-Maximum Suppression)을 조절하여 검열 대상의 인식률을 조절 할 수 있다.

## 저작권 및 사용권 정보 (Copyleft / End User License)
MIT License

Copyright (c) 2020 GONNYONG4

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
