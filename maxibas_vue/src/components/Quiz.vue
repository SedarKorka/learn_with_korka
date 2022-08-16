<template>
<div>
<h5 class="ed_toppadder20 text-center">{{ quiz.question }}</h5>
    <div class="control ">
        <label class="radio text-center">
            <input type="radio" :value="quiz.op1" v-model="selectedAnswer">{{ quiz.op1 }}

        </label>
        <br/>
        <label class="radio text-center">
            <input type="radio" :value="quiz.op2" v-model="selectedAnswer">{{ quiz.op2 }}

        </label>
        <br/>
        <label class="radio text-center">
            <input type="radio" :value="quiz.op3" v-model="selectedAnswer">{{ quiz.op3 }}

        </label>
        <br/>
        <br/>

        <div className="">
            <button type="button" class="btn ed_btn pull-center ed_orange" @click="submitQuiz">Submit</button>

        </div>

        <template v-if="quizResult == 'correct'">
                <div className="notification is-success mt-4">
                    Correct :-D

                </div>

        </template>

        <template v-if="quizResult == 'incorrect'">
                <div className="notification is-danger mt-4">
                    wrong answer :-( Please try again !)

                </div>

        </template>


    </div>

</div>

    
</template>
<script>

export default{
        props: ['quiz'],
        data(){
            return {
                selectedAnswer:'',
                quizResult:null
            }
        },
        methods:{
            submitQuiz(){
                this.quizResult = null
                if (this.selectedAnswer) {
                    if (this.selectedAnswer  === this.quiz.answer) {
                        this.quizResult = 'correct'
                    }else{
                        this.quizResult = 'incorrect'
                    }
                }else{
                    alert("Select answer first")
                }
            },
        }
    }
</script>
