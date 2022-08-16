<template>
   
 <!--Header start-->
<header id="ed_header_wrapper">
	<div class="ed_header_top">
		<div class="container">
			<div class="row">
				<div class="col-lg-6 col-md-6 col-sm-6">
					<div class="ed_contact_details">
						<ul>
							<li><i class="fa fa-phone" aria-hidden="true"></i> +33 07 52 84 52 10</li>
							<li><a href="#"><i class="fa fa-envelope-o" aria-hidden="true"></i> codewithkorka@codewithkorka.com</a></li>
						</ul>
					</div>
				</div>
				
				<div class="col-lg-6 col-md-6 col-sm-6">
					<div class="ed_social_icons">
						<ul>
							<li><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
							<li><a href="#"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li>
							<li><a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
							<li><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
							<li><a href="#"><i class="fa fa-whatsapp" aria-hidden="true"></i></a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="ed_header_bottom">
		<div class="container">
			<div class="row">
				<div class="col-lg-3 col-md-3 col-sm-3">
 

					<div class="educo_logo">
                         <router-link to="/"><img src="assets/imges/header/Logo.png" alt="logo" /></router-link
                         > 
                    </div>
				</div>
				<div class="col-lg-9 col-md-9 col-sm-9">
					<div class="edoco_menu_toggle navbar-toggle" data-toggle="collapse" data-target="#ed_menu">Menu <i class="fa fa-bars"></i></div>
					<div class="edoco_menu">
						<ul class="collapse navbar-collapse" id="ed_menu">
							<li><router-link to="/">Home</router-link></li>
							<li><router-link to="/about">About</router-link></li>
							
							<li><router-link to="/courses">courses</router-link></li>
							<li><router-link to="/blog">Blog</router-link></li>
							
							<li><router-link to="/contact-us" >Contact </router-link></li>


                        <template v-if="$store.state.user.isAuthenticated">
                            <li><router-link to="/dashboard/my-account">My account</router-link></li>
                        </template>

                        <template v-else>
                            <li><router-link to="/sign-up" class=" is-primary"><strong>Sign up</strong></router-link></li>
                            <li><router-link to="/log-in" class=" is-light">Log in</router-link></li>
                        </template>


						</ul>
					</div>
				</div>
			</div>
		</div>
    </div>
</header>
</template>