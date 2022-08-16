<template>
<div>






<!--Breadcrumb start-->
<div class="ed_pagetitle">
<div class="ed_img_overlay"></div>
	<div class="container">
		<div class="row">
			<!--div class="col-lg-12 col-md-12 col-sm-12">
				<div class="page_title d-flex justify-content-center">
					
					<div>
						<h2>All Courses</h2>

					</div>
				</div>
			</div-->

			<div class="col-lg-5 col-md-5 col-sm-12 col-xs-5">
				
			</div>
			<div class="col-lg-7 col-md-7 col-sm-12 col-xs-7">
				<a href="/sign-up" class="btn ed_btn   ed_orange">Get Started</a>
			</div>

		</div>
	</div>
</div>
<!--Breadcrumb end-->
<!-- Section eleven start -->
<div class="ed_courses ed_toppadder80 ed_bottompadder80">
	<div class="container">
		<div class="row"
		>
		

			<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"
			
			v-for="course in courses"
			v-bind:key="course.id"
			>

			<!--Import course Item -->
			<CourseItem :course="course" />
				
			</div>
		
		</div>
    </div><!-- /.container -->
</div>
<!-- Section eleven end -->
 
 

<!--counter section start -->
<div class="ed_graysection ed_toppadder90 ed_bottompadder90">
	<div class="container">
		<div class="row">
			<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
				<div class="ed_heading_top ed_bottompadder50">
					<h3>Why Choose Us</h3>
				</div>
			</div>
			<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
				<div class="ed_counter_wrapper">
					<div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">
						<div class="ed_counter">
							<h2 class="timer" data-from="0" data-to="2600" data-speed="5000"></h2>
							<h4>Students Successive</h4>
							<p>Throughout these year we have done amazing work with 250 students..</p>
						</div>
					</div>
					<div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">
						<div class="ed_counter">
							<h2 class="timer" data-from="0" data-to="5900" data-speed="5000"></h2>
							<h4>Competitions won</h4>
							<p>Only competitions were the ones in the back of the magazines you find..</p>
						</div>
					</div>
					<div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">
						<div class="ed_counter">
							<h2 class="timer" data-from="0" data-to="8400" data-speed="5000"></h2>
							<h4>Classes visited</h4>
							<p>Can how you setup your classroom impact how students think...</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<!--counter section end -->
<!--client section start -->
<div class="ed_transprentbg ed_toppadder90 ed_bottompadder90">
	<div class="container">
		<div class="row">
			<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
				<div class="ed_heading_top ed_bottompadder80">
					<h3>our partners</h3>
				</div>
			</div>
			<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
				<div class="ed_clientslider">
					<div id="owl-demo5" class="owl-carousel owl-theme">
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div>
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div>
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div>
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div>
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div> 
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div>
						<div class="item">
							<a href="#">
								<img src="http://placehold.it/160X100" alt="Partner Img" />
							</a>
						</div>
					</div>
				</div>
			</div>
		</div>
    </div><!-- /.container -->
</div>
<!--client section end -->
</div>
   

</template>

<script>
 
import axios from 'axios'
import CourseItem from '@/components/CourseItem.vue'
export default {
  name: 'Home',
   data() {
        return {
            courses: []
        }
    },
	components:{
		CourseItem
	},
	
    mounted() {
        console.log('mounted')

		document.title = 'Wellcome | maxibas'

        axios
            .get('courses/get_frontpage_courses/')
            .then(response => {
                console.log(response.data)

                this.courses = response.data
            })
    } 
}
</script>
