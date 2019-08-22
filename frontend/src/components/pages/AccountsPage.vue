<template>
  <v-flex shrink>
    <span class="display-3 grey--text">유저 페이지</span>
  </v-flex>
</template>

<script>
import { mapActions } from "vuex";

export default {
  mounted() {
    mapActions("data", [""])
  }
}
</script>
