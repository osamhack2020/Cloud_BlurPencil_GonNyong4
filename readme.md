
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
 <img src="https://img.shields.io/github/commit-activity/y/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge"/>
 <img src="https://img.shields.io/github/last-commit/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge"/>
</p>

<p align="center">
 <img src="https://img.shields.io/github/license/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge"/>
 <a href="https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4">
 	<img src="https://img.shields.io/badge/LIVE-DEMO-%235f5fff?style=for-the-badge"/>
 </a>
</p>

<!-- 
//깃헙 레포 코드 용량
![](https://img.shields.io/github/languages/code-size/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge)
//깃헙 레포 닫힌 이슈 개수
![](https://img.shields.io/github/issues-closed/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge)
//깃헙 PR
![](https://img.shields.io/github/issues-pr/osamhack2020/Cloud_BlurPencil_GonNyong4?style=for-the-badge)
-->

## 팀소개 및 프로젝트 설명 동영상
<!-- 마땅히 넣어 볼게 없어서 당장 심심해 보여 넣습니담.. 넣어두 되려나 모르겠네여 -->
![프로젝트설명](./intro.png)

## 기능 설계
### 구조
![구조](./archi.png.png)

### 설계
![설계](https://user-images.githubusercontent.com/7239579/96877750-01658a80-14b5-11eb-9fe7-118d594dc8a7.png)


## 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)
- 권장 : 최신 버전의 크로미움 기반 브라우저

## 기술 스택 (Technique Used) (예시)
### Server(back-end)
 - Node.js
 - Express
 - MongoDB
 - Flask
 - PyTorch
 
### front-end
 -  Vue.js
 -  Bootstrap

## 설치 안내 (Installation Process)
```bash
$ git clone https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4.git
```

### Back-End
```bash
$ cd server/
$ npm install
```

### Front-End
```bash
$ cd client/
$ npm install
```

### Build / Test
```bash
$ (root) npm start
```

### 세팅 유의 사항
1. [vue.config.js](https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/blob/master/client/vue.config.js) 안에 '/api' `target` 주소를 서버주소(로컬 환경시 서버포트)로 변경
2. [main.js](https://github.com/osamhack2020/Cloud_BlurPencil_GonNyong4/blob/master/client/src/main.js) 안에 `serverUrl` 변수명을 서버주소(로컬 환경시 서버포트)로 변경

> 구름 IDE 환경으로 개발시 로컬 주소가 아닌 URL 주소를 직접 입력해 주어야함


## 팀 정보 (Team Information)
<!--
- 팀장: 김현재 (hyeonjae.dev@gmail.com) | [Github](https://github.com/hughesgoon)
- 팀원(Full stack): 강예찬 (kyechan99@gmail.com) | [Github](https://github.com/kyechan99) 
- 팀원(Front-End): 배성준 (clcc001@naver.com) | 
- 팀원(Pytorch, CV): 홍승표 (spkbk98@gmail.com) | [Github](https://github.com/seungpyo) 
-->

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

## 저작권 및 사용권 정보 (Copyleft / End User License)
MIT License

Copyright (c) 2020 GONNYONG4

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
