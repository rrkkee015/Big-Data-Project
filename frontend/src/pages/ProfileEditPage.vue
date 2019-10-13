<template>
  <div style="width: 100%; padding-left:12px; padding-right:12px;">
    <EditProfile/>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";
import EditProfile from "../components/ProfileEdit/EditProfile"

export default {
  components: {
    EditProfile
  },
  async created() {
    this.toggleProfileSnackBar(false)
    await this.getSingleProfile(this.$route.params.nickname)
  },
  methods: {
    ...mapActions("profiles", ["getSingleProfile"]),
    ...mapMutations("entrance", ["toggleProfileSnackBar"]),
  },
}
</script>

<style scoped>

</style>