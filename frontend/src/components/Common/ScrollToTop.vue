<template>
  <v-layout v-scroll="onScroll">
    <v-scroll-y-reverse-transition>
      <v-btn 
				v-show="offsetTop!=0" 
				@click="scrollToTop"  
				icon
				fixed 
				bottom 
				right
        class="white--text bg-transparent"
			>
        <v-icon>mdi-chevron-up</v-icon>
      </v-btn>
    </v-scroll-y-reverse-transition>
  </v-layout>
</template>

<script>
export default {
  data (){
    return{
      offsetTop: 0,
    }
  },
  methods: {
    scrollToTop() {
      window.scroll({ top: 0, left: 0, behavior: 'smooth' })
    },
    onScroll(e){
      this.offsetTop = window.pageYOffset || document.documentElement.scrollTop
    },
  }
}
</script>

<style scoped>
.bg-transparent {
  background-color: rgba(0, 0, 0, 0) !important;
}

.bg-transparent:hover {
  background-color: black !important;
}
.bg-transparent:before {
  background-color: black !important;
}
.bg-transparent:after {
  background-color: black !important;
}
</style>