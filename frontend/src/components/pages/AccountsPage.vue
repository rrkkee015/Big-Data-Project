<template>
  <v-flex shrink>
    <span class="display-3 grey--text">유저 페이지</span>
    {{ accountList }}
  </v-flex>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState("data",["accountList"])
  },
  methods: {
    ...mapActions("data", { setUser: 'searchAccounts'}),
    your_own_function() {},
  },
  mounted() {
    this.setUser()
  }
}
</script>
