<template>
  <div class="home">
<nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top" style="padding: 1rem;">
	<div class="container">
	<a class="navbar-brand" href="#"><img src="../images/logo.png" class="navbar-logo"/></a>
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
	<span class="navbar-toggler-icon"></span>
	</button>

	<div class="collapse navbar-collapse" id="navbarSupportedContent">
	<ul class="navbar-nav mr-auto">
	<li class="nav-item active">
		<a class="nav-link" href="#info">서비스 소개 <span class="sr-only">(current)</span></a>
	</li>
	<li class="nav-item active">
		<a class="nav-link" href="#feature">기능</a>
	</li>
	<li class="nav-item active">
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
			<p style="margin-bottom: .5rem;">접근하기 편리한 웹을 통해 이미지를 드래그 앤 드랍만 하면, 학습된 BLUR PENCIL이 이미지를 분석한 후 모자이크 할 객체를 인식하며, 인식된 객체 중 원하는 객체를 골라 모자이크 처리할 수 있습니다. 또한 모자이크 처리 된 이미지 내역들은 저장할 수 있으며, 다른 사용자들과 공유할 수 있습니다.</p>
			<a class="btn btn-primary" href="/demo	">무료로 사용하기</a>
		</div>
		<img src="../images/106.png" class="intro-head-img"/>
	</div>
	<div class="container section-feature" id="feature">
		<img src="../images/066.png" class="feature-head-img"/>
		<div class="feature-desc">
			<h1 class="feature-desc-point">BLUR PENCIL의 검열 기능</h1>
			<!-- <h5 class="feature-desc-point">빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해를 보완하세요!</h5> -->
			<p style="color :black;">빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해를 보완하세요!</p><p>모자이크 할 이미지를 올리고 클릭 3번이면 자동으로 이미지를 검열합니다.<br>강력한 보안을 필요로 하는 개인이나 집단, 저작권 보호를 중요시 하는 단체에게 BLUR PENCIL만의 기술을 통해 빠르고 편리하게 이미지를 자동 검열하여<br>업무 성능 향상을 도와줍니다.</p>
		</div>
	</div>
	<div class="color-box"></div>
	<div class="bg-point">
		<div class="container section-price" id="price">
			<div class="price-desc" style = "padding-top : 10vh">
				<h1>Price</h1>	
				<div class="row" style="justify-content: space-around;">
					<div class="col-md-4">
						<div class="card price-card">
							<div class="card-body">
								<div class="price">무료</div>
								<p style="margin-bottom : 0.5rem;">회원가입을 하지 않아도 사용가능합니다.</p>
								<div class="price-content" style = "display : inline-block">
									<div style= "text-align : left">
										<li>이미지 모자이크 처리</li>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-md-4">
						<div class="card price-card">
							<div class="card-body">
								<div class="price">로그인</div>
								<p style="margin-bottom : 0.5rem;">회원가입시 더 많은 기능이 제공됩니다.</p>
								<div class="price-content" style = "display : inline-block">
									<div style= "text-align : left">
										<li>이미지 모자이크 처리</li>
										<li>데이터 백업</li>
										<li>작업 내역 저장</li>
										<li>동료들과 작업 공유</li>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
	<login-page id="login" style="position: relative; padding-bottom: 9rem; padding-top : 7.5rem;"></login-page>
	<div class="footer container">
		<a href="/" class="footer-brand"><img src="../images/logo.png" class="footer-logo">BLUR PENCIL</a>
		<div class="footer-menu">
			<a href="#">서비스 소개</a>
			<a href="#feature">기능</a>
			<a href="#price">가격</a>
		</div>
		<a href="https://github.com/orgs/osamhack2020/teams/gonnyong4">GONYONG4</a>
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
<style lang="scss">
/* 반응형 나중에 */
	html {
		scroll-behavior: smooth;
	}
	body {
		background-color: white !important;
	}
	.navbar-logo {
		width: 1.5rem;
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
		padding-bottom: 4rem;
	}
	.footer {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
		height: 4.5rem;
		background-color: #FEFEFE;
	}
	.footer .footer-menu a {
		color: black;
		margin-left: 1rem;
		margin-right: 1rem;
	}
	.footer .footer-brand  {
		color: black;
		text-decoration: none;
	}
	.footer .footer-brand .footer-logo {
		height: 1.8rem;
		margin-right: .5rem;
	}
	.price-card {
		border-radius: 3rem !important;
		padding-top: 16px;
		padding-bottom: 16px;
		box-shadow: 0px 5px 15px 5px #0000004a;
		.price {
			font-size: 3rem;
		}
	}
</style>
