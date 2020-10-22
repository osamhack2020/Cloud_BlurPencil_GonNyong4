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
			<p style="margin-bottom: .5rem;">어쩌구 저쩌구 블라 블라 아무말이나 계속 채워 넣다 보면 뭔가는 있어보이겠지 싶어서 일단은 계속 적고 있는데 이게 정말 효과적일지는 모르겠고 더 이상 쓸말이 없으니 여기까지 쓸까 하다가도 아직 부족하다 생각도 들고 에라 모르겠다.</p>
			<a class="btn btn-primary" href="#login">무료로 사용하기</a>
		</div>
		<img src="../images/106.png" class="intro-head-img"/>
	</div>
	<div class="container section-feature" id="feature">
		<img src="../images/066.png" class="feature-head-img"/>
		<div class="feature-desc">
			<h1 class="feature-desc-point">BLUR PENCIL의 검열 기능</h1>
			<!-- <h5 class="feature-desc-point">빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해를 보완하세요!</h5> -->
			<p>빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해를 보완하세요! 대충 이런말 쓰면 될 것같긴한데 막상 넣을 내용은 아직 없네요 한번 생각해봐주세요 어쩌구 저쩌구 블라 블라 아무말이나 넣어서 내용 있어보이게 만들기 어쩌구 저쩌구 블라 블라 아무말이나 넣어서 내용 있어보이게 만들기</p>
		</div>
	</div>
	<div class="color-box"></div>
	<div class="bg-point">
		<div class="container section-price" id="price">
			<div class="price-desc">
				<h1>Price</h1>	
				<div class="row" style="justify-content: space-around;">
					<div class="col-md-4">
						<div class="card">
							<div class="card-body">
								<div class="price">Free</div>
								<div class="price-content">
									<p>회원가입을 안해도 사용 가능함.</p>
									<p>대충 이런 내용 생각했지만 일단은 플랜은 제외</p>
								</div>
							</div>
						</div>
					</div>
					<div class="col-md-4">
						<div class="card">
							<div class="card-body">
								<div class="price">로그인</div>
								<div class="price-content">
									<p>회원가입을 하면 더 많은 기능이 제공됨.</p>
									<p>대충 이런 내용 생각했지만 일단은 플랜은 제외</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="footer container">
		<a href="/" class="footer-brand"><img src="../images/title.png" class="footer-logo"></a>
		<div class="footer-menu">
			<a href="#">서비스 소개</a>
			<a href="#">기능</a>
			<a href="#">가격</a>
		</div>
		<a href="#">GONYONG4</a>
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
	html {
		scroll-behavior: smooth;
	}
	.navbar-logo {
		width: 3rem;
	}
	.container p{
		margin-bottom : 0;
	}
	.content{
		border-bottom: 1px solid #353C46;
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
	.feature-title {
		text-align: left;
	}
	.section-feature {
		display: flex;
		padding-top: 10rem;
		/* padding-bottom: 0rem; */
		text-align: left;
		justify-content: space-between;
		align-items: center;
		/* min-height: 50rem; */
	}
	.feature-desc-point {
		color: black;
	}
	.section-feature .feature-head-img {
		padding-left: 1rem;
		height: 15rem;
	}
	.section-feature .feature-desc {
		padding: 5rem 0rem 5rem 3rem;
		text-align: right;
		color: white;
	}
	.color-box {
		z-index: -1;
		position: relative;
		margin-top: -11.25rem;
		width: 100%;
		height: 30rem;
		background-color: #5f5fff;
	}
	.bg-point {
		background-color: #5f5fff;
	}
	.section-price {
		/* color: white; */
		padding-bottom: 10rem;
	}
	.footer {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
		height: 10rem;
		background-color: #FEFEFE;
	}
	.footer .footer-menu a {
		color: black;
		margin-left: 1rem;
		margin-right: 1rem;
	}
	.footer .footer-brand .footer-logo {
		height: 3rem;
	}
</style>
