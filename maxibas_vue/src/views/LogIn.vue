<template>
  <div>

      <!--Breadcrumb start-->
<div class="ed_pagetitle">
<div class="ed_img_overlay"></div>
	<div class="container">
		<div class="row">
			<div class="col-lg-6 col-md-4 col-sm-6">
				<div class="page_title">
					<h2>Log in</h2>
				</div>
			</div>
			<div class="col-lg-6 col-md-8 col-sm-6">
				<ul class="breadcrumb">
					<li><router-link to="/">home</router-link></li>
					<li><i class="fa fa-angle-double-left" aria-hidden="true"></i></li>
					<li><router-link to="/log-in">Log in</router-link></li>
				</ul>
			</div>
		</div>
	</div>
</div>

    



    <!--section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <form v-on:submit.prevent="submitForm">
                        <div class="notification is-danger" v-if="errors.length">
                            <p
                                v-for="error in errors"
                                v-bind:key="error"
                            >
                                {{ error }}
                            </p>
                        </div>
                        <div class="field">
                            <label>Email</label>
                            <div class="control">
                                <input type="email" class="input" v-model="username">
                            </div>
                        </div>

                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password">
                            </div>
                        </div>

                        

                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">Log in</button>
                            </div>
                        </div>
                    </form>

                    <hr>

                    Or <router-link to="/sign-up">click here</router-link> to sign up!
                </div>
            </div>
        </div>
    </section-->


    <!--Breadcrumb end-->
<div class="ed_transprentbg ed_toppadder80 ed_bottompadder80">
	<div class="container">
		<div class="row">
			<div class="col-lg-8 col-md-8 col-sm-12 col-xs-12 col-lg-offset-2 col-md-offset-2">
				<div class="ed_teacher_div">
					<div class="ed_heading_top">
						<h3>login in</h3>
					</div>

                     <div class="is-danger" v-if="errors.length">
                            <p
                                v-for="error in errors"
                                v-bind:key="error"
                            >
                                {{ error }}
                            </p>
                        </div>
                    
					<form class="ed_contact_form ed_toppadder40" v-on:submit.prevent="submitForm">
						<div class="row">
							
							
							<div class="col-lg-12 col-md-12 col-sm-12">
								<div class="form-group">
									<label class="control-label">Username :</label>
									<input type="text" class="form-control" v-model="username">
								</div>
							</div>
							<div class="col-lg-12 col-md-12 col-sm-12">
								<div class="form-group">
									<label class="control-label">Password :</label>
									<input type="password" class="form-control" v-model="password">
								</div>
							</div>
							
							<div class="col-lg-12 col-md-12 col-sm-12">
								<button class="btn ed_btn ed_orange pull-right">login in</button>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>
<!--Footer Top section start-->











  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted(){
        document.title = 'Login | macibas'
    },
    methods: {
        submitForm() {
            console.log('submitForm')

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing!')
            }

            if (this.password === '') {
                this.errors.push('The password is missing!')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post('token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = "Token " + token

                        localStorage.setItem('token', token)

                        this.$router.push('/dashboard/my-account')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>