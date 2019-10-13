import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import firebase from 'firebase/app'
import router from './router'
import store from './store'
import AOS from 'aos'
import 'aos/dist/aos.css'

Vue.config.productionTip = false

const firebaseConfig = {
  apiKey: "AIzaSyCaPQtIgFwdWzWrijl7bFLQnwSChPHKfsk",
  authDomain: "heyandnerd.firebaseapp.com",
  databaseURL: "https://heyandnerd.firebaseio.com",
  projectId: "heyandnerd",
  storageBucket: "",
  messagingSenderId: "229073390656",
  appId: "1:229073390656:web:e91297afdefe314941e3a5",
  measurementId: "G-4Q7K8SKG5L"
};
firebase.initializeApp(firebaseConfig);

new Vue({
  async created() {
    AOS.init();
    if ('user' in localStorage) {
      await store.dispatch('auth/autoLogin')
      var nickname = await this.$store.state.auth.profile.nickname
      await store.dispatch('profiles/getSingleProfile', nickname)
      var ratingsLength = await this.$store.state.profiles.ratingsLength
      if (ratingsLength < 7) {
        router.push({name: 'rating'})
      }
    } else {
      router.push({name: 'landing'})
    }
  },
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
