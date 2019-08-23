<template>
  <v-card>
    <v-layout>
      <v-flex>
        <v-card-title class="headline">
          {{ account.username }}
          <v-spacer></v-spacer>
          <v-card-actions class="card_action justify-end">
            <v-icon color="black" @click="callParents()">mdi-close</v-icon>
          </v-card-actions> 
        </v-card-title>
        <hr>
        <v-card-text fluid v-for="movie in account.ratings" :key="movie.id">
          {{ movie.movie }}
        </v-card-text>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  props: {
    account: {
      type: Object,
      deafult: () => new Object
    }
  },
  methods: {
    callParents() {
      this.$emit('turnOff')
    }
  }
}
</script>