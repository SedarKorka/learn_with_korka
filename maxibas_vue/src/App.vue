<template>
<div>
 <Nav/>

  <router-view/>

  <Footer/>
</div>
</template>
<script>
import axios from 'axios'
import Footer from '@/components/Footer'
import Nav from '@/components/Nav'

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  },
  beforeCreated(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.user.token

    if (token) {
      axios.defaults.headers.common['Autorization'] = "Token "+token
    }else{

       axios.defaults.headers.common['Autorization'] = ""
    }
  }
}
</script>

<style lang="scss">

</style>
