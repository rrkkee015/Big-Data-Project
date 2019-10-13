<template>
  <v-row class="center white--text col-12">
    <v-col cols="8">
      <v-select
        v-model="clustering"
        :items="clusterings"
        background-color="black"
        item-color="black"
        dark
        label="Select User Cluster Algorithm"
        @change="setState(clustering)"
      ></v-select>  
    </v-col>
  </v-row>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data() {
    return {
      clusterings: ['KNN', 'MF'],
      clustering: ""
    }
  },
  methods: {
    ...mapMutations("movieRecommendation", ["setState"])
  }
}
</script>

<style scoped>
  .center {
    display: flex;
    justify-content: center;
  }
</style>