<template>
  <v-row class="white--text">
    <v-row class="col-12" data-aos="fade-in" data-aos-once="true" data-aos-duration="1500" data-aos-delay="400">
      <v-col>
        <div class="neon" style="display: flex; align-items: center; justify-content: center;">
          <p>Se<span>t</span>ting for <span>U</span>SER Clu<span>ste</span>ring</p>
        </div>
      </v-col>
    </v-row>
    <UserClustering data-aos="fade-in" data-aos-once="true" data-aos-duration="1500" data-aos-delay="800"/>
    <v-row v-show="cur.isKMeans" class="center col-12">
      <Kmeans/>
    </v-row>
    <v-row v-show="cur.isHierarchical" class="center col-12">
      <Hierarchical/>
    </v-row>
    <v-row v-show="cur.isEM" class="center col-12">
      <EM/>
    </v-row>
  </v-row>
</template>

<script>
import { mapState } from 'vuex'
import UserClustering from '../components/AdminUserClustering/UserClustering'
import Kmeans from '../components/AdminUserClustering/Kmeans'
import Hierarchical from '../components/AdminUserClustering/Hierarchical'
import EM from '../components/AdminUserClustering/EM'

export default {
  computed: {
    ...mapState("userClustering", ["cur"])
  },
  components: {
    UserClustering,
    Kmeans,
    Hierarchical,
    EM
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/css?family=Vibur);

.center {
  display: flex;
  justify-content: center;
}
.neon {
  text-align: center;
  width: 50%;
  height: 250px;
  margin: auto;
  background: #112 url(//images.weserv.nl/?url=i.imgur.com/6QJjYMe.jpg) center;
  background-size: contain;
  border-radius: 50px;
  box-shadow: 0px 0px 20px 20px black inset;
}
.neon p{
  font: 400 55px "Vibur";
  color: #fee;
  text-shadow: 
    0 -40px 100px, 
    0 0 2px, 
    0 0 1em #ff4444, 
    0 0 0.5em #ff4444, 
    0 0 0.1em #ff4444, 
    0 10px 3px #000;
}
.neon p span{
  animation: blink linear infinite 2s;
}
.neon p span:nth-of-type(2){
  animation: blink linear infinite 4s;
}
.neon p span:nth-of-type(3){
  animation: blink linear infinite 3s;
}
@keyframes blink {
  78% {
    color: inherit;
    text-shadow: inherit;
  }
  79%{
     color: #333;
  }
  80% {
    
    text-shadow: none;
  }
  81% {
    color: inherit;
    text-shadow: inherit;
  }
  82% {
    color: #333;
    text-shadow: none;
  }
  83% {
    color: inherit;
    text-shadow: inherit;
  }
  92% {
    color: #333;
    text-shadow: none;
  }
  92.5% {
    color: inherit;
    text-shadow: inherit;
  }
}
</style>