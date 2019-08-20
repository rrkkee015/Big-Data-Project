<template>
  <v-form ref="form">
    <v-text-field v-model="title" label="장르 제목" />
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    genre: ""
  }),
  methods: {
    onSubmit: function() {
      const params = {
        genre: this.genre,
      };
      
      this.submit(params);
    }
  }
};
</script>