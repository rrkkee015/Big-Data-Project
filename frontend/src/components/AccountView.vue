<template>
  <tr @click="toggledialog()">
    <td class="text-left">{{ account.user }}</td>
    <td class="text-left">{{ account.username }}</td>
    <td class="text-left">{{ account.age }}</td>
    <td class="text-left">{{ account.occupation }}</td>
    <td class="text-left">{{ account.gender }}</td>
    <v-dialog v-model="dialog" max-width="1000" persistent>
      <AccountDetail
        :account="account"
        @turnOff="dialog=false"
      />
    </v-dialog>
  </tr>
</template>

<script>
import AccountDetail from './AccountDetail'

export default {
  components: {
    AccountDetail
  },
  props: {
    account: {
      type: Object,
      default: () => new Object
    }
  },
  data() {
    return {
      dialog: false
    }
  },
  methods: {
    toggledialog() {
      this.dialog = !this.dialog
    }
  }
}
</script>