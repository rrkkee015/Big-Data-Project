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
          v-model="maxIter"
          label="Number of Iterations, Max iteration"
          required
          :error-messages="maxIterError"
          dark
          :items="maxIterItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="nInit"
          label="Number of Initialization, N init"
          required
          :error-messages="nInitError"
          dark
          :items="nInitItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="con"
          label="Type of Convariance, Convariance Type"
          required
          :error-messages="conError"
          dark
          :items="conItems"
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
      maxIterItems: [100, 200, 300, 400, 500],
      nInitItems: [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      conItems: ['Pull', 'Tied', 'Diag', 'Pherical'],
      k: "",
      maxIter: "",
      nInit: "",
      con: ""
    }
  },
  mixins: [validationMixin],
  validations: {
    k: { required },
    maxIter: { required },
    nInit: { required },
    con: { required }
  },
  computed: {
    kError () {
      const errors = []
      if (!this.$v.k.$dirty) return errors
      !this.$v.k.required && errors.push('K is required')
      return errors
    },
    maxIterError () {
      const errors = []
      if (!this.$v.maxIter.$dirty) return errors
      !this.$v.maxIter.required && errors.push('Max iteration is required')
      return errors
    },
    nInitError () {
      const errors = []
      if (!this.$v.nInit.$dirty) return errors
      !this.$v.nInit.required && errors.push('N init is required')
      return errors
    },
    conError () {
      const errors = []
      if (!this.$v.con.$dirty) return errors
      !this.$v.con.required && errors.push('Convariance type is required')
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