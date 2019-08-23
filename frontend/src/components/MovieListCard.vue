<template>
  <div>
    <v-hover v-slot:default="{ hover }">
      <v-card :elevation="hover ? 8 : 2" @click="toggleDialog()">
        <v-layout align-center py-4 pl-4>
          <v-flex text-center>
            <v-container grid-list-lg pa-0>
              <v-layout column>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title class="headline">
                      {{ title }}
                    </v-list-item-title>
                    <v-list-item-subtitle>{{ genresStr }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-card-text>
                  <v-layout justify-center>
                    <v-rating
                      :value="rating"
                      color="indigo"
                      background-color="indigo"
                      half-increments
                      dense
                      readonly
                    />
                    <div class="grey--text ml-4">{{ rating.toFixed(1) }}</div>
                  </v-layout>
                </v-card-text>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
    </v-hover>
    <v-dialog
      v-model="dialog"
      max-width="1000"
      persistent
    >
      <MovieDetail 
        :title="title"
        :viewCnt="viewCnt"
        :genresStr="genresStr"
        :rating="rating"
        @turnOff="dialog=false"
      />
    </v-dialog>
  </div>
</template>

<script>
import MovieDetail from './MovieDetail'

export default {
  components: {
    MovieDetail
  },
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      dialog: false
    }
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    },
  },
  methods: {
    toggleDialog() {
      this.dialog = !this.dialog
    },
    getImgUrl(img) {
      return require('@/assets/' + img)
    }
  }
};
</script>