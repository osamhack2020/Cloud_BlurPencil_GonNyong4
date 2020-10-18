<template>
  <div class="home">
<nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
	<div class="container">
	<a class="navbar-brand" href="#"><img src="../images/logo(125x125).png" class="navbar-logo"/></a>
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
	<span class="navbar-toggler-icon"></span>
	</button>

	<div class="collapse navbar-collapse" id="navbarSupportedContent">
	<ul class="navbar-nav mr-auto">
	<li class="nav-item active">
		<a class="nav-link" href="#info">서비스 소개 <span class="sr-only">(current)</span></a>
	</li>
	<li class="nav-item">
		<a class="nav-link" href="#feature">기능</a>
	</li>
	<li class="nav-item">
		<a class="nav-link" href="#price">가격</a>
	</li>
	</ul>
	<a href="#login" class="btn btn-outline-primary my-2 my-sm-0 rounded-pill">로그인</a>
	</div>
	</div>
</nav>
	<div class="container section-intro" id="info">
		<div class="intro-desc">
			<h1>BLUR PENCIL</h1>
			<h5>BLUR PENCIL 은 가장 강력한 모자이크 처리 서비스입니다.</h5>
			<p>어쩌구 저쩌구 블라 블라 아무말이나 계속 채워 넣다 보면 뭔가는 있어보이겠지 싶어서 일단은 계속 적고 있는데 이게 정말 효과적일지는 모르겠고 더 이상 쓸말이 없으니 여기까지 쓸까 하다가도 아직 부족하다 생각도 들고 에라 모르겠다.</p>
		</div>
		<img src="../images/106.png" class="intro-head-img"/>
	</div>
	<div class="container section-feature" id="feature">
		<div class="feature-desc">
			<h1>Feature</h1>
			<p>대충 모자이크 해주는 사진</p>
		</div>
	</div>
	<div class="container section-price" id="price">
		<div class="price-desc">
			<h1>Price</h1>
			<p>대충 가격 정책 나열</p>
		</div>
	</div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
	<div >
		<login-page id="login"></login-page>
	</div>
  </div>
</template>

<script>
import LoginPage from '@/components/Login.vue'

export default {
  name: 'Home',
  components: {
    LoginPage
  }
}
</script>
<style>
/* 반응형 나중에 */
.navbar-logo {
	width: 3rem;
}
.section-intro {
	display: flex;
	padding-top: 10rem;
	padding-bottom: 10rem;
	margin-top: 74px;
	background-color: white;
	justify-content: space-between;
}
.section-intro .intro-desc {
	padding: 5rem 5rem 5rem 1rem;
	text-align: left;
}
.section-intro .intro-head-img {
	height: 30rem;
}
</style>
