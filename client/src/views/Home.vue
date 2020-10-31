<template>
  <div class="home">
<nav class="navbar navbar-expand-lg navbar-light fixed-top" style="background-color: white; padding: 1rem;">
	<div class="container">
		<a class="navbar-brand navbar-logo" href="#"><img src="../images/logo.png"/></a>
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
	<div class="container-fluid" style="background-color: #f2f2f2;">
		<div class="container section-feature" id="feature">
			<img src="../images/066.png" class="feature-head-img"/>
			<div class="feature-desc">
				<h1 class="feature-desc-point">BLUR PENCIL의 검열 기능</h1>
				<!-- <h5 class="feature-desc-point">빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해를 보완하세요!</h5> -->
				<p>빠르고 편리한 자동 검열 기능을 통해 보안 취약점과 저작권 침해를 보완하세요!</p>
				<p>모자이크 할 이미지를 올리고 클릭 3번이면 자동으로 이미지를 검열합니다.<br>강력한 보안을 필요로 하는 개인이나 집단, 저작권 보호를 중요시 하는 단체에게 BLUR PENCIL만의 기술을 통해 빠르고 편리하게 이미지를 자동 검열하여<br>업무 성능 향상을 도와줍니다.</p>
				<div class="row feature-tech-row" style="margin-top: 32px; justify-content: space-around;">
					<div class="col-md-5 card">
						<div class="card-body">
							<h4>인식률</h4>
							<p>로고로 파악할 추적 점수의 최소값을 조절하여 검열 대상의 인식률을 조절합니다.</p>
						</div>
					</div>
					<div class="col-md-5 card">
						<div class="card-body">
							<h4>NMS</h4>
							<p>Non-Maximum Suppression에서 사용할 IoU(Intersection over Union)의 threshold 값</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- <div class="color-box"></div> -->
	<div class="bg-point">
		<div class="container section-price" id="price">
			<div class="price-desc">
				<h1>BLUR PENCIL은 무료입니다</h1>	
				<p style="color: white;">무료 회원가입을 통해 더 많은 기능을 사용해보세요!</p>
				<div class="row" style="justify-content: space-around; margin-top: 4rem;">
					<div class="col-md-4">
						<div class="card price-card">
							<div class="card-body">
								<div class="price">무료</div>
								<p style="margin-bottom : 0.5rem;">회원가입을 하지 않아도 사용가능합니다.</p>
								<hr/>
								<div class="price-content">
									<li><img class="check-icon" src="../images/icons/check-circle.svg"/>이미지 모자이크 처리</li>
									<hr/>
									<a class="btn btn-primary" href="/demo	">무료로 사용하기</a>
								</div>
							</div>
						</div>
					</div>
					<div class="col-md-4">
						<div class="card price-card">
							<div class="card-body">
								<div class="price">로그인</div>
								<p style="margin-bottom : 0.5rem;">회원가입시 더 많은 기능이 제공됩니다.</p>
								<hr/>
								<div class="price-content">
										<li><img class="check-icon" src="../images/icons/check-circle.svg"/>이미지 모자이크 처리</li>
										<hr/>
										<li><img class="check-icon" src="../images/icons/check-circle.svg"/>데이터 백업</li>
										<hr/>
										<li><img class="check-icon" src="../images/icons/check-circle.svg"/>작업 내역 저장</li>
										<hr/>
										<li><img class="check-icon" src="../images/icons/check-circle.svg"/>동료들과 작업 공유</li>
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
		<a href="https://github.com/orgs/osamhack2020/teams/gonnyong4">Copyright © 2020 GONYONG4</a>
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
	h1 {
		font-weight: bold !important;
	}
	.navbar-logo {
		width: 1.5rem;
		margin-left: 1rem;
		img {
			width: 1.5rem;
		}
	}
	.navbar-nav {
		@media (max-width: 992px) {
			flex-direction: row !important;
		}
	}
	.nav-item {
		.nav-link {
			@media (max-width: 992px) {
				padding: .5rem !important;
			}
		}
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
		position: relative;
		// @media (max-width: 1200px) {
		// 	padding-left: 0px !important;
		// }
		// @media (max-width: 576px) {
		// 	padding-left: 0px !important;
		// }
		.intro-desc {
			padding: 5rem 5rem 5rem 1rem;
			text-align: left;
			@media (max-width: 992px) {
				padding: 0px;
			}
		}
		.intro-head-img {
			height: 30rem;
			@media (max-width: 992px) {
				height: 20rem;
				position: absolute;
				opacity: .1;
				right: 0px;
			}
		}
	}
	.feature-title {
		text-align: left;
	}
	.section-feature {
		display: flex;
		padding-top: 5rem;
		padding-bottom: 5rem;
		/* padding-bottom: 0rem; */
		text-align: left;
		justify-content: space-between;
		align-items: center;
		position: relative;
		/* min-height: 50rem; */
		.feature-head-img {
			padding-left: 1rem;
			height: 15rem;
			z-index: 0;
			@media (max-width: 1200px) {
				position: absolute;
				left: 0px;
				opacity: .1;
				// height: 10vw;
			}
			@media (max-width: 768px) {
				display: none;
			}
		}
		.feature-desc {
			padding: 5rem 0rem 5rem 3rem;
			text-align: right;
			z-index: 1;
			@media (max-width: 768px) {
				padding: 0px;
			}
			// color: white;
		}
	}
	.feature-desc-point {
		color: black;
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
		padding-top: 5rem;
		padding-bottom: 5rem;
		.price-desc {
			h1 {
				color: white;
				font-weight: 700;
				@media (max-width: 768px) {
					font-size: 2.4rem !important;
				}
			}
		}
	}
	.footer {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
		height: 4.5rem;
		background-color: #FEFEFE;
		padding-top: 5rem;
		padding-bottom: 5rem;
		a {
			color: black;
			text-decoration: none;
			&:hover {
				color: black;
			text-decoration: none;
			}
		}
		@media (max-width: 768px) {
			display: table;
			// flex-flow: column;
		}
		.footer-menu {
			@media (max-width: 768px) {
				margin-top: 2rem;
				margin-bottom: 2rem;
			}
		}
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
		@media (max-width: 768px) {
			margin-bottom: 2rem;
		}
		.price {
			font-size: 3rem;
			padding-top: 1rem;
			padding-bottom: 2rem;
		}
		li {
			list-style-type: none;
		}
		hr {
			border-top: 1px solid rgba(95, 95, 255, 0.25) !important;
		}
		.check-icon {
			width: 1.2rem;
			margin-right: .5rem;
		}
	}
	.feature-tech-row {
		margin-top: 2rem;
		justify-content: space-around;
		.card-body {
			text-align: left;
			padding: 2rem 1rem;
			h4 {
				font-size: 1.2rem;
			}
		}
	}
</style>
