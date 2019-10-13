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
          v-model="linkage"
          label="Type of linkage, Linkage"
          required
          :error-messages="linkageError"
          dark
          :items="linkageItems"
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
      kItems: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      linkageItems: ['Ward', 'Complete', 'Average', 'Single'],
      k: "",
      linkage: ""
    }
  },
  mixins: [validationMixin],
  validations: {
    k: { required },
    linkage: { required },
  },
  computed: {
    kError () {
      const errors = []
      if (!this.$v.k.$dirty) return errors
      !this.$v.k.required && errors.push('K is required')
      return errors
    },
    linkageError () {
      const errors = []
      if (!this.$v.linkage.$dirty) return errors
      !this.$v.linkage.required && errors.push('Linkage is required')
      return errors
    },
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