<template>
  <v-data-table
    :headers="headers"
    :items="this.$store.state.data.accountList"
    :items-per-page="10"
    class="elevation-1"
    show-expand
  >
    <template v-slot:expanded-item="{ headers }">
      <td :colspan="headers.length">Peek-a-boo!</td>
    </template>
  </v-data-table>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      headers: [
        { text: 'user', value: 'user' },
        { text: 'username', value: 'username' },
        { text: 'age', value: 'age' },
        { text: 'occupation', value: 'occupation' },
        { text: 'gender', value: 'gender' },
      ]
    }
  },
  computed: {
    ...mapState("data",["accountList"])
  },
  mounted() {
    this.setUser()
  },
  methods: {
    ...mapActions("data", { setUser: 'searchAccounts'}),
  }
}
</script>