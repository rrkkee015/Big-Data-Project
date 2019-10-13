<template>
  <v-container class="white--text">
    <v-row>
      <v-col cols="12">
        <div data-aos="fade-in" data-aos-once="true" data-aos-duration="1500" data-aos-delay="400" class="neon center">
          <p>U<span>S</span>ERS</p>
        </div>
      </v-col>
    </v-row>
    <AdminUserList/>
  </v-container>
</template>

<script>
import AdminUserList from "../components/AdminUserList/AdminUserList"

export default {
  components: {
    AdminUserList
  }
}
</script>

<style scoped>
@media (max-width: 575px) {
  .neon p {
    font: 400 35px "Vibur" !important;
  }
  .neon {
    height: 150px !important;
  }
}
.center {
  display: flex;
  align-items: center;
  justify-content: center;
}
.neon {
  text-align: center;
  width: 65%;
  height: 250px;
  margin: auto;
  background: #112 url(//images.weserv.nl/?url=i.imgur.com/6QJjYMe.jpg) center;
  background-size: contain;
  border-radius: 50px;
  box-shadow: 0px 0px 20px 20px black inset;
}
@import url(//fonts.googleapis.com/css?family=Vibur);
.neon p {
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