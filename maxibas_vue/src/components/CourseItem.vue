<template>
    <div class="ed_mostrecomeded_course">
						<div class="ed_item_img">
							<img :src="course.get_image" alt="item1" class="img-responsive">
						</div>
						<div class="ed_item_description ed_most_recomended_data">
							<h4><a href="course_single.html"> {{ course.title }} </a></h4>
							<!--div class="row">
								<div class="ed_rating">
									<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
										<div class="row">
											<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
												<div class="ed_stardiv">
													<div class="star-rating"><span style="width:80%;"></span></div>
												</div>
											</div>
											<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
												<div class="row">
													<p>(5 review)</p>
												</div>
											</div>
										</div>
									</div>
									<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
										<div class="ed_views">
										<i class="fa fa-users"></i>
										<span>35 students</span>
										</div>
									</div>
								</div>
							</div-->
							<div class="course_detail">
								<div class="course_faculty">
									<img src="http://placehold.it/32X32" alt=""> <a href="#">Joanna Simpson</a>
								</div>
							</div>
							<p>{{ course.short_description }}</p>
							
                            <router-link class="ed_getinvolved" :to="{name: 'Course', params: {slug: course.slug}}">More <i class="fa fa-long-arrow-right"></i></router-link>
						</div>
					</div>
</template>

<script> 

export default ({
    props:['course']
})
</script>
