<template>
  <v-col cols="8">
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="ratentNum"
          label="Number of ratent, Ratent number"
          required
          :error-messages="ratentNumError"
          dark
          :items="ratentNumItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="learningRate"
          label="Number of learning rate, Rate"
          required
          :error-messages="learningRateError"
          dark
          :items="learningRateItems"
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="epocks"
          label="Number of epocks, Epocks"
          required
          :error-messages="epocksError"
          dark
          :items="epocksItems"
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
      ratentNumItems: [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
      learningRateItems: [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1],
      epocksItems: [100, 200, 300, 400, 500],
      ratentNum: "",
      learningRate: "",
      epocks: "",
    }
  },
  mixins: [validationMixin],
  validations: {
    ratentNum: { required },
    learningRate: { required },
    epocks: { required },
  },
  computed: {
    ratentNumError () {
      const errors = []
      if (!this.$v.ratentNum.$dirty) return errors
      !this.$v.ratentNum.required && errors.push('Ratent number is required')
      return errors
    },
    learningRateError () {
      const errors = []
      if (!this.$v.learningRate.$dirty) return errors
      !this.$v.learningRate.required && errors.push('learningRate is required')
      return errors
    },
    epocksError () {
      const errors = []
      if (!this.$v.epocks.$dirty) return errors
      !this.$v.epocks.required && errors.push('Epocks is required')
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