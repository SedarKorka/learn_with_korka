<template>

    <div class="ed_video_section">
        <div class="embed-responsive embed-responsive-16by9">
            <div class="ed_video">
               <img src="http://placehold.it/806X405" class="img-responsive" alt="1" />
                <div class="ed_img_overlay">
                <a href="#"><i class="fa fa-play-circle" aria-hidden="true"></i></a>
            </div>
            </div>
               <iframe 
                    id="educo_video" 
                    class="embed-responsive-item" 
                    :src="'https://www.youtube.com/embed/' + youtube_id" 
                    allowfullscreen>
                </iframe>
            </div>
        </div>
    
</template>
<script> 

export default{
    props: ['youtube_id']
}
</script>
