<template>
  <v-card>
    <v-layout>
      <v-img class="movie_img" :src="getImgUrl('Toy_story.jpg')"></v-img>
      <v-flex>
        <v-card-title class="headline">{{ title }}</v-card-title>
        
        <v-card-text>
          동해물과 백두산이 마르고 닳도록 하느님이 보우하사 길이보전하세 무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세
        </v-card-text>
        <v-card-text>
          <v-layout justify-center>
            <v-icon color="black">mdi-eye</v-icon>
            <div class="grey--text ml-4">{{ viewCnt }}</div>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow=1"></div>

          <v-btn
            color="green darken-1"
            text
            @click="callParents"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ""
    },
    viewCnt: {
      type: Number,
      default: 0
    }
  },
  methods: {
    getImgUrl(img) {
      return require('@/assets/' + img)
    },
    callParents() {
      this.$emit('turnOff')
    }
  }
}
</script>

<style scoped>
  .movie_img {
    width: 50%;
  }
</style>