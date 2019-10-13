<template>
  <v-col cols="8">
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="k"
          label="Number of Clusters, K"
          required
          :error-messages="kError"
          dark
          :items="kItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="base"
          label="Type of Base, Base"
          required
          :error-messages="baseError"
          dark
          :items="baseItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="similarity_function"
          label="Type of Similarity function, Similarity"
          required
          :error-messages="similarity_functionError"
          dark
          :items="similarity_functionItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="center" cols="12">
        <v-btn @click="startClustering" text color="white">Run</v-btn>
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      kItems: [100, 200, 300, 400, 500],
      baseItems: ['item', 'user', 'CF'],
      similarity_functionItems: ['Cosine', 'Pearson'],
      k: "",
      base: "",
      similarity_function: "",
    }
  },
  mixins: [validationMixin],
  validations: {
    k: { required },
    base: { required },
    similarity_function: { required },
  },
  computed: {
    kError () {
      const errors = []
      if (!this.$v.k.$dirty) return errors
      !this.$v.k.required && errors.push('K is required')
      return errors
    },
    baseError () {
      const errors = []
      if (!this.$v.base.$dirty) return errors
      !this.$v.base.required && errors.push('Base is required')
      return errors
    },
    similarity_functionError () {
      const errors = []
      if (!this.$v.similarity_function.$dirty) return errors
      !this.$v.similarity_function.required && errors.push('Similarity function is required')
      return errors
    }
  },
  methods: {
    startClustering() {
      this.$v.$touch()
      if (this.$v.$invalid) {
        console.log('---')
      } else {
        console.log('asdhfjkhsakjdhjk')
      }
    }
  },
}
</script>

<style scoped>
.center {
  justify-content: center;
  display: flex;
}
</style>