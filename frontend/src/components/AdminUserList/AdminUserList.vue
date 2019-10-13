<template>
  <div data-aos="fade-up" data-aos-once="true" data-aos-duration="1500" data-aos-delay="800">
    <v-row class="justify-center">
      <v-col cols="12" sm="8">
        <v-expansion-panels dark>
          <v-expansion-panel
            v-for="(item,i) in allProfiles.results"
            :key="i"
            style="background-color: black;"
          >
            <v-expansion-panel-header>{{ item.nickname }}</v-expansion-panel-header>
            <v-expansion-panel-content class="font-size">
              <p>Email: {{ item.user.email }}</p>
              <p>Age: {{ item.age }}</p>
              <p>Gender: {{ item.gender }}</p>
              <p>Occupation: {{ item.occupation }}</p>
              <p>Subscribe: {{ item.subscribe }}</p>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-pagination
          v-model="page"
          :length="pageNum"
          :total-visible="7"
          dark
        ></v-pagination>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";

export default {
  async created() {
    await this.getAllProfiles(1)
  },
  computed: {
    ...mapState("profiles", ["allProfiles"]),
    pageNum() {
      return Math.floor(this.allProfiles.count/40 + 1) 
    },
    page: {
      get() {
        return this.$store.state.profiles.page
      },
      async set(value) {
        this.setPage(value)
        await this.getAllProfiles(this.page)
      }
    }
  },
  methods: {
    ...mapMutations("profiles", ["setPage"]),
    ...mapActions("profiles", ["getAllProfiles"])
  },
}
</script>

<style scoped>
@media (max-width: 575px) {
  .font-size p {
    font-size: 11px !important;
  }
}
</style>