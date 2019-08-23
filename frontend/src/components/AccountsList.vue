<template>
  <v-simple-table>
    <thead>
      <tr>
        <th class="text-left">user</th>
        <th class="text-left">username</th>
        <th class="text-left">age</th>
        <th class="text-left">occupation</th>
        <th class="text-left">gender</th>
      </tr>
    </thead>
    <tbody>
      <AccountView
        :account="account"
        v-for = "account in accountList" :key="account.id"
      />
    </tbody>
  </v-simple-table>
</template>

<script>
import AccountView from './AccountView'

export default {
  components: {
    AccountView
  },
  props: {
    accountList: {
      type:Array,
      default: () => new Array()
    }
  },
  data() {
    return {
      dialog: false
    }
  },
  methods: {
    toggleDialog() {
      this.dialog = !this.dialog
    }
  }
}
</script>