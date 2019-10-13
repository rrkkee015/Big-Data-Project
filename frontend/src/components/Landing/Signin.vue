<template>
  <v-card color="rgba(0, 0, 0, 0.6)" class="pa-5 signInSize">
    <v-card-title style="padding-top:8px; color:white;">Sign In</v-card-title>
    <v-card-text>
      <v-text-field label="Email*" required
      v-model="email"
      :error-messages="emailErrors"
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
      autocomplete="off"
      >
      </v-text-field>
      <v-text-field label="Password*" type="password" required
      v-model="password"
      :error-messages="passwordErrors"
      @input="$v.password.$touch()"
      @blur="$v.password.$touch()"
      @keyup.enter="signIn"
      >
      </v-text-field>
    </v-card-text>
    <v-card-actions>
      <!-- <v-btn style="color:white" outlined block @click="changeLocation('main')">Sign In</v-btn> -->
      <v-btn style="color:white" outlined block @click="signIn">Sign In</v-btn>
    </v-card-actions>
    <v-flex class="mx-2 my-3">
      <v-btn style="color:white" :ripple="{ class: 'blue--text' }" text block><i class="fab fa-facebook-f"></i>&nbsp; Login with Facebook</v-btn>
      <v-btn style="color:white" :ripple="{ class: 'red--text' }" text block><i class="fab fa-google"></i>&nbsp; Login with Google</v-btn>
    </v-flex>
    <hr />
    <v-card-text style="color:white" class="text-center">
      <span>Are you newbie? <v-btn style="color:white" text @click="callParent()">Sign up now</v-btn></span>
    </v-card-text>
  </v-card>
</template>
<script>
import router from '../../router'
import { validationMixin } from 'vuelidate'
import { required, email, minLength } from 'vuelidate/lib/validators'
import { mapState, mapActions } from 'vuex'

export default {
  props: {
    toggle: {
      type: Boolean,
      default: true,
    },
    validCheckSnackbar: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return  {
      email: '',
      password: '',
    }
  },
  mixins: [validationMixin],
  validations: {
    email: {
      required,
      email,
    },
    password: {
      required,
      minLength: minLength(4)
    },
  },
  computed: {
    ...mapState('auth',['signInError']),
    emailErrors() {
      const errors = []
        if (!this.$v.email.$dirty) {
          return errors
        };
        !this.$v.email.required && errors.push('Must be valid e-mail')
        !this.$v.email.email && errors.push('E-mail is required')
        return errors
    },
    passwordErrors() {
      const errors = []
      if (!this.$v.password.$dirty) {
        return errors
      };
      !this.$v.password.required && errors.push('Must be valid password')
      !this.$v.password.minLength && errors.push('Password must be at least 4 characters long')
      return errors
    },
  },
  methods: {
    ...mapActions('profiles', ['getSingleProfile']),
    ...mapActions('auth', ['userLogin']),
    callParent() {
      this.$emit('turnToggle')
    },
    callParentForValid() {
      this.$emit('turnValidCheckSnackbar')
    },
    callParentForErr() {
      this.$emit('turnErrSnackbar')
    },
    clear() {
      this.$v.$reset()
      this.password = ''
    },
    async signIn() {
      this.$v.$touch()
      if (this.$v.$invalid) {
        this.callParentForValid()
        } else {
          await this.userLogin({
            username: this.email,
            password: this.password
          })
        if (this.signInError !== null) {
          this.callParentForErr()
        }
        var nickname = await this.$store.state.auth.profile.nickname
        await this.getSingleProfile(nickname)
        var ratingsLength = await this.$store.state.profiles.ratingsLength
        console.log(ratingsLength)
        if (ratingsLength < 7) {
          router.push({name: 'rating'})
        } else { router.push({name: 'home'}) }
        this.clear()
      }
    },
  },
}
</script>

<style scoped>
>>> .theme--light.v-input:not(.v-input--is-disabled) input, .theme--light.v-input:not(.v-input--is-disabled) textarea {
  color: white;
}
>>> .theme--light.v-label {
  color: white;
}
>>> .theme--light.v-text-field > .v-input__control > .v-input__slot:before {
  border-color : rgba(255, 255, 255, 0.5);
}
>>> .v-text-field.v-input--has-state > .v-input__control > .v-input__slot:before {
  border-color : currentColor;
}
>>> .theme--light.v-text-field:not(.v-input--has-state) > .v-input__control > .v-input__slot:hover:before {
  border-color: white;
}

.signInSize {
  width: 500px;
}

@media (max-width: 575px) {
  .signInSize {
    width: 350px;
  }
}
</style>