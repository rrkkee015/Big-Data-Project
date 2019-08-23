<template>
  <v-form ref="form">
    <v-select
      v-model="genre"
      :items="items"
      label="장르"
      @change="onSubmit"
    />
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
    title: "",
    genre: "",
    items: ['Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 
    'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 
    'Horror', 'Musical', 'Mystry', 'Romance', 'Sci-Fi', 
    'Thriller', 'War', 'Western']
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