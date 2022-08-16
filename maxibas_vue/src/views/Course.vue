<template>
    <!--div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title"></h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Table of contents</h2>

                        <ul>
                            <li
                                v-for="lesson in lessons"
                                v-bind:key="lesson.id"
                            >
                                <a @click="activeLesson = lesson">{{ lesson.title }}</a>
                            </li>
                        </ul>
                    </div>

                    <div class="column is-10">
                        <template v-if="$store.state.user.isAuthenticated">
                            <template v-if="activeLesson">
                                <h2>{{ activeLesson.title }}</h2>
                                
                                {{ activeLesson.long_description }}
                            </template>

                            <template v-else>
                                {{ course.long_description }}
                            </template>
                        </template>

                        <template v-else>
                            <h2>Restricted access</h2>
                            
                            <p>You need to have an account to continue!</p>
                        </template>
                    </div>
                </div>
            </div>
        </section>
    </div-->
    <div>




        <!--Breadcrumb start-->
<div class="ed_pagetitle">
<div class="ed_img_overlay"></div>
	<div class="container">
		<div class="row">
			<div class="col-lg-6 col-md-4 col-sm-6">
				<div class="page_title">
					<h2>Course : {{ course.title }}</h2>
				</div>
			</div>
			<div class="col-lg-6 col-md-8 col-sm-6">
				<ul class="breadcrumb">
 
					
                    <li><router-link to="/">Home</router-link></li>
					<li><i class="fa fa-angle-double-left" aria-hidden="true"></i></li>
					<li><router-link to="/courses">all courses</router-link></li>
					<li><i class="fa fa-angle-double-left" aria-hidden="true"></i> </li>
					<li> {{ course.title }}</li>
				</ul>
			</div>
		</div>
	</div>
</div>
<!--Breadcrumb end-->
                








            <!--Single content start-->
<div class="ed_graysection ed_toppadder80 ed_bottompadder80">
  <div class="container">
    <div class="row">
		<div class="col-lg-9 col-md-9 col-sm-9 col-lg-push-3 col-md-push-3 col-sm-push-3">
			<div class="ed_course_single_item">
				<div class="ed_course_single_image">


                    <template v-if="$store.state.user.isAuthenticated">
                        <template v-if="activeLesson">
                            <template v-if="activeLesson.lesson_type === 'video'"> 
                                    
                                    <Video
                                        v-bind:youtube_id="activeLesson.youtube_id"

                                        />

                            </template>
                        </template>

                    </template>
					
					






				
				</div>
			<div class="ed_course_single_info"> 
                 <template v-if="$store.state.user.isAuthenticated">
                     
                            <template v-if="activeLesson">
                                <h2 class="ed_toppadder20">Lesson : {{ activeLesson.title }}</h2>
                                
                                {{ activeLesson.long_description }}

                                <span class="text-center " style="background:yellow" v-if="activity.status == 'started'" @click="markAsDone">Started (mark as done)</span>
                                <span class="text-center " style="background:red" v-else>Done</span>

                                <template v-if="activeLesson.lesson_type === 'quiz'">
                                    <Quiz 
                                    v-bind:quiz="quiz"/>
                                    

                                </template>


                                
                            </template>

                            <template v-else>
                                {{ course.long_description }}
                            </template>

                    <button type="button" class="btn ed_btn pull-left ed_orange">preview lesson</button>
                    <button type="button" class="btn ed_btn pull-right ed_orange">next lesson</button>
                  
                </template>

                <template v-else>
                    <div align="center">
                        <h2 class="center">Restricted access</h2>
                            
                        <p>You need to have an account to continue!</p>

                    </div>
                    
                </template>
				
				
				
			</div>
			</div>	
        <template v-if="$store.state.user.isAuthenticated">
            <template v-if="activeLesson">
                <template v-if="activeLesson.lesson_type === 'article'">

                    <div class="ed_time_executor ed_toppadder40">
                        
                        <!--Comments section start-->
                            <div class="ed_blog_comment_wrapper">
                                <h4>All Comments</h4> 
                                <CourseComment
                                
                                    v-for="comment in comments"
                                    v-bind:key="comment.id"
                                    v-bind:comment="comment"
                                 />
                                <!--Comments section end-->

                                <!--Comments Form start-->
                                <AddComment v-bind:course="course"
                                            v-bind:activeLesson="activeLesson"
                                            v-on:submitComment = "submitComment"

                                />
                        
                                    
                                <!--Comments Form end-->
                            </div>
                        

                    </div>
                    
                </template>
            </template>
        </template>
			<!--div class="ed_time_executor ed_toppadder40">
				<ul>
					<li><a href="course_lesson.html">lessons</a> <span>estimated time</span></li>
					<li><a href="course_lesson.html">languages</a> <span><i class="fa fa-check-circle-o"></i></span></li>
					<li><a href="course_lesson.html">writting work</a> <span>Currently active</span></li>
					<li><a href="course_lesson.html">Reading works</a> <span>Locked</span></li>
					<li><a href="course_lesson.html">spoken</a> <span>Locked</span></li>
					<li><a href="course_lesson.html">Beginners</a> <span>Locked</span></li>
				</ul>
			</div-->
			</div>
		
        <!--Sidebar Start-->
		<div class="col-lg-3 col-md-3 col-sm-3 col-lg-pull-9 col-md-pull-9 col-sm-pull-9">
		<div class="sidebar_wrapper_upper">
			<div class="sidebar_wrapper">
			
				<aside class="widget widget_progress_bar">
					<h4 class="widget-title">lessons status</h4>
					<div class="progress">
						<div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" style="width: 75%">
						<span class="sr-only">75% Complete</span>
						<p>75% Completed</p>
						</div>
					</div>
				</aside>
				
				<aside class="widget widget_categories">
					<h4 class="widget-title">Search lessons</h4>
					<ul>
						
                        <li
                            v-for="lesson in lessons"
                            v-bind:key="lesson.id">
                                <i class="fa fa-chevron-right"></i>
                                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a> 
                                            
                        </li>
					</ul>
				</aside>
				
				<aside class="widget widget_sharing">
					<h4 class="widget-title">share this lesson</h4>
					<ul>
						<li><a href="course_single.html"><i class="fa fa-facebook"></i> facebook</a></li>
						<li><a href="course_single.html"><i class="fa fa-linkedin"></i> linkedin</a></li>
						<li><a href="course_single.html"><i class="fa fa-twitter"></i> twitter</a></li>
						<li><a href="course_single.html"><i class="fa fa-google-plus"></i> google+</a></li>
					</ul>
				</aside>
				
			</div>
		</div>
		</div>
		<div class="col-lg-3 col-md-3 col-sm-3 col-lg-pull-9 col-md-pull-9 col-sm-pull-9">
			<div class="ed_sidebar_slider ed_bottompadder10">
				<h3>popular courses</h3>
				<div id="owl-demo3" class="owl-carousel owl-theme">
					<div class="item">
						<div class="ed_item_img">
							<img src="http://placehold.it/233X233" alt="item1" class="img-responsive">
						</div>
						<div class="ed_mostrecomeded_course_slider ed_most_recomended_data">
							<h4><a href="course_single.html">summer Camps</a></h4>
						</div>
					</div>
					<div class="item">
						<div class="ed_item_img">
						<img src="http://placehold.it/233X233" alt="item2" class="img-responsive">
						</div>
						<div class="ed_mostrecomeded_course_slider ed_most_recomended_data">
							<h4><a href="course_single.html">writting skills</a></h4>
						</div>
					</div>
					<div class="item">
						<div class="ed_item_img">
						<img src="http://placehold.it/233X233" alt="item3" class="img-responsive">
						</div>
						<div class="ed_mostrecomeded_course_slider ed_most_recomended_data">
							<h4><a href="course_single.html">learning Seminar</a></h4>
						</div>
					</div>
				</div>
			</div>
		</div>
    <!--Sidebar End-->

	</div>
  </div>  
  
</div>

<!--Single content end-->





    </div>
</template>

<script>
import axios from 'axios'
import CourseComment from '@/components/CourseComment.vue'
import AddComment from '@/components/AddComment.vue'
import Quiz from '@/components/Quiz.vue'
import Video from '@/components/Video.vue' 

export default {
    components:{
        CourseComment,
        AddComment,
        Quiz,
        Video,
    },
    data() {
        return {
            course: {},
            lessons: [],
            comments:[],
            activeLesson: null,
            errors:[],
            quiz:{},
            activity:{}
        }
    },
   async mounted() {
        console.log('mounted')

        const slug = this.$route.params.slug

        await axios
             .get(`courses/${slug}/`)
             .then(response => {
                console.log(response.data)

                this.course = response.data.course
                this.lessons = response.data.lessons
            })

        document.title = this.course.title + ' | maxibas'
    },
    methods:{ 
        submitComment(comment){
            this.comments.push(comment)

        },
        setActiveLesson(lesson){
            this.activeLesson = lesson

            if (lesson.lesson_type === 'quiz') {
                this.getQuiz()
                
            } else {
                this.getComments() 
            }

            this.trackStarted()
           
        },
        trackStarted() {
            axios
                .post(`activities/track_started/${this.$route.params.slug}/${this.activeLesson.slug}/`)
                .then(response => {
                    console.log(response.data)
                    this.activity = response.data
                })
        }, 
        markAsDone() {
            axios
                .post(`activities/mark_as_done/${this.$route.params.slug}/${this.activeLesson.slug}/`)
                .then(response => {
                    console.log(response.data)
                    this.activity = response.data
                })
        },
        getQuiz(){
            axios
                .get(`courses/${this.course.slug}/${this.activeLesson.slug}/get_quiz/`)
                .then(response=>{
                    console.log(response.data)
                    this.quiz = response.data
                })

        },
        getComments(){
            //console.log('List of comment')
            axios
                .get(`courses/${this.course.slug}/${this.activeLesson.slug}/get-comments/`)
                .then(response=>{
                    console.log(response.data)
                    this.comments = response.data
                })

        }
    }
}
</script>