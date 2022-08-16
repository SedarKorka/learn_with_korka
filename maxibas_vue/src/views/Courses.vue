<template>
<div>
    <!--Breadcrumb start-->
<div class="ed_pagetitle">
<div class="ed_img_overlay"></div>
	<div class="container">
		<div class="row">
			<div class="col-lg-6 col-md-4 col-sm-6">
				<div class="page_title">
					<h2>Courses</h2>
				</div>
			</div>
			<div class="col-lg-6 col-md-8 col-sm-6">
				<ul class="breadcrumb">
					<li><a href="index.html">home</a></li>
					<li><i class="fa fa-angle-double-left" aria-hidden="true"></i></li>
					<li><a href="course_sidebar_r.html">Courses right sidebar</a></li>
				</ul>
			</div>
		</div>
	</div>
</div>
<!--Breadcrumb end-->
<!-- Section eleven start -->
<div class="ed_courses ed_toppadder80 ed_bottompadder80">
	<div class="container">
		<div class="row">
		<div class="col-lg-9 col-md-9 col-sm-9 col-lg-push-3 col-md-push-3 col-sm-push-3">
			<div class="row">
				<div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"
                        v-for="course in courses"
                        v-bind:key="course.id"
                >
				
					


					<!--Import course Item -->
					<CourseItem :course="course" />
				</div>
				<div class="col-lg-12">
					<div class="ed_blog_bottom_pagination">
						<nav>
							<ul class="pagination">
								<li><a href="#">1</a></li>
								<li><a href="#">2</a></li>
								<li><a href="#">3</a></li>
								<li class="active"><a href="#">Next <span class="sr-only">(current)</span></a></li>
							</ul>
						</nav>
					</div>
				</div>
			</div>
		</div>
	<!--Sidebar Start-->
		<div class="col-lg-3 col-md-3 col-sm-3 col-lg-pull-9 col-md-pull-9 col-sm-pull-9">
			<div class="sidebar_wrapper_upper">
				<div class="sidebar_wrapper">
					<aside class="widget widget_search">
						<div class="input-group">
							<input type="text" class="form-control" placeholder="Search...">
							<span class="input-group-btn">
								<button class="btn btn-default" type="button"><i class="fa fa-search"></i></button>
							</span>
						</div>
					</aside>
					<aside class="widget widget_categories">
						<h4 class="widget-title">course Categories</h4>
						<ul>

							<li 
								v-bind:class="{ 'is-active': !activeCategory }"
								@click="setActiveCategory(null)"
							>
							<a><i class="fa fa-chevron-right"></i> All Courses</a>
							
							</li>

							<li
								v-for="category in categories"
								v-bind:key="category.id"
								
								@click="setActiveCategory(category)"
							>
							<a><i class="fa fa-chevron-right"></i> {{ category.title }}</a>
							
							</li>
						</ul>
					</aside>
					<aside class="widget widget_categories">
						<h4 class="widget-title">course type</h4>
						<ul>
							<li><a href="#"><i class="fa fa-chevron-right"></i> basic</a></li>
							<li><a href="#"><i class="fa fa-chevron-right"></i> starts</a></li>
							<li><a href="#"><i class="fa fa-chevron-right"></i> advance</a></li>
						</ul>
					</aside>
					<aside class="widget widget_categories">
						<h4 class="widget-title">course certification</h4>
						<ul>
							<li><a href="#"><i class="fa fa-chevron-right"></i> Summer camps</a></li>
							<li><a href="#"><i class="fa fa-chevron-right"></i> complete course</a></li>
							<li><a href="#"><i class="fa fa-chevron-right"></i> Monthly learn</a></li>
						</ul>
					</aside>
					<aside class="widget widget_tag_cloud">
						<h4 class="widget-title">Search by Tags</h4>
							<a href="#" class="ed_btn ed_orange">Play school</a>
							<a href="#" class="ed_btn ed_orange">skill</a>
							<a href="#" class="ed_btn ed_orange">tests</a>
							<a href="#" class="ed_btn ed_orange">exams</a>
							<a href="#" class="ed_btn ed_orange">elementary school</a>
							<a href="#" class="ed_btn ed_orange">Study</a>
							<a href="#" class="ed_btn ed_orange">edution</a>
					</aside>
				</div>
			</div>
		</div>
<!--Sidebar End-->
		</div>
    </div><!-- /.container -->
</div>
<!-- Section eleven end -->
</div>
</template>

<script>
import axios from 'axios'
import CourseItem from '@/components/CourseItem.vue'

export default {
    data() {
        return {
            courses: [],
			categories: [],
			activeCategory: null
        }
    },
	components:{
		CourseItem
	},
   async mounted() {
        console.log('mounted')

		await axios
			.get('courses/get_categories/')
			.then(response=>{
				console.log(response.data)
				this.categories = response.data
			})
   
		this.getCourses() 

		document.title = 'Courses | macibas'
    },
	methods:{
		setActiveCategory(category){
			console.log(category)
			this.activeCategory = category

			this.getCourses()
			
		},

		getCourses(){
			let url = 'courses/'

			if (this.activeCategory) {
				url += '?category_id=' + this.activeCategory.id
			}
			axios
				.get(url)
				.then(response => {
					console.log(response.data)

					this.courses = response.data
				})

		}
	}
}
</script>