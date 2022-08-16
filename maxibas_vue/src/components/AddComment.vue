<template>
    <div class="ed_blog_message_wrapper">
                                        <h4>All Comments</h4>
                                        <div class="ed_blog_messages ed_toppadder30">
                                            <div class="row">

                                                <h5 class="text-center is-danger"
                                                    v-for="error in errors"
                                                    v-bind:key="error"
                                                >
                                                    {{ error }}
                                                </h5>
                                            


                                
                                        <form v-on:submit.prevent="submitComment()">
                                            
                                            
                                            <div class="form-group">
                                                <div class="col-lg-12">
                                                    <textarea class="form-control" rows="5" placeholder="Your Message" v-model="comment.content"></textarea>
                                                </div>
                                            </div>
                                            <div class="form-group">
                                                <div class="col-lg-12">
                                                    <button  class="btn ed_btn ed_orange">Submit</button>
                                                </div>
                                            </div>
                                        </form>

                            
                            

                                            </div>
                                        </div>
                                    </div>
    
</template>
<script>
import axios from 'axios'
export default {

        props:[
            'course','activeLesson',
        ],
        data(){
            return {
                comment:{
                    name:'',
                    email:'',
                    content:''
                },
                errors:[]
            }
        },
        methods:{
            
            submitComment(){  
                this.errors=[]
               
                
                if(this.comment.content === ''){
                    this.errors.push('The content must be filled out')
                }
                
                if(!this.errors.length){
                    
                    axios
                        .post(`courses/${this.$route.params.slug}/${this.activeLesson.slug}/`,this.comment )
                        .then(response => {
                            this.comment.name = ''
                            this.comment.email = ''
                            this.comment.content = ''
                        
                            this.$emit('submitComment',response.data)

                            
                        })
                        .catch(error =>{
                            console.log(error)
                            
                        })
                }
                
            },
        }
    }
</script>
