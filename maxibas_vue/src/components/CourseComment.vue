<template>
<div>
    <div class="ed_blog_comment ed_toppadder30">
        <div class="ed_comment_image">
             <img src="http://placehold.it/70X70" alt="" /> 
        </div>
            
        <div class="ed_comment_text">
                <h5>{{ comment.name }} <span>{{ comment.created_at }} <a href="" class="comment_reply">Reply</a></span></h5>
                    <p>{{ comment.content }} </p>
              </div>
        </div>
                                    <!-- class="ed_blog_sub_comment ed_toppadder30" style="display:none">
                                            <div class="ed_comment_image"> <img src="http://placehold.it/70X70" alt="" /> </div>
                                            <div class="ed_comment_text">
                                                <h5>Tina Bonucci <span>january 31, 2017 <a href="" class="comment_reply">Reply</a></span></h5>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vehicula mauris ac facilisis congue. Fusce sem enim, rhoncus volutpat condimentum ac, placerat semper ligula. Suspendisse in viverra justo, eu placerat urna. Vestibulum blandit diam suscipit nibh mattis ullamcorper. Nullam a condimentum nulla, ut facilisis enim. </p>
                                            </div>
                                        </div-->

      </div>
                                    
</template>
<script> 

export default    {
        props : ['comment']
    } 
</script>
