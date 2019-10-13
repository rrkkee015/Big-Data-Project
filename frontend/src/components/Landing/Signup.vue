<template>
  <v-card color="rgb(0, 0, 0)" class="pa-5 signup_width" style="align-items: center; display: flex; right:0%; height:100%">
    <v-row style="display:flex; justify-content: center;">
      <v-col cols="12" md="6" lg="12">
        <v-card-title style="padding-top:8px; color:white;"><span>Sign Up</span></v-card-title>
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
          >
          </v-text-field>
          <v-text-field label="Confirm password*" type="password" required
          v-model="checkPassword"
          :error-messages="checkPasswordErrors"
          @input="$v.checkPassword.$touch()"
          @blur="$v.checkPassword.$touch()"
          @keyup.enter="signUp"
          >
          </v-text-field>
        </v-card-text>
        
        <v-card-actions style="margin-bottom: 26px;">
          <v-row style="display: flex; justify-content: center;">
            <v-col>
              <v-btn style="color:white; border: 0px !important" outlined block @click="signUp">Sign Up</v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
        <v-flex class="mx-2 my-3">
          <v-btn style="color:white" :ripple="{ class: 'blue--text' }" text block><i class="fab fa-facebook-f"></i>&nbsp; Signup with Facebook</v-btn>
          <v-btn style="color:white" :ripple="{ class: 'red--text' }" text block><i class="fab fa-google"></i>&nbsp; Signup with Google</v-btn>
        </v-flex>
        <hr/>

        <v-card-text class="text-center" style="color:white">
          <span>Already have an account? <v-btn style="color:white" @click="callParent_toggle()" text>Sign in</v-btn></span>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, sameAs } from 'vuelidate/lib/validators'
import { mapState, mapMutations } from 'vuex'

export default {
  props: {
    toggle: {
      type: Boolean,
      default: false,
    },
    signUpSnackbar: {
      type: Boolean,
      default: false,
    },
    existSnackbar: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
      show: false,
      email: '',
      password: '',
      checkPassword: '',
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
    checkPassword: {
      required,
      sameAs: sameAs('password')
    },
  },
  computed: {
    ...mapState("auth", ["signUpError"]),
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
    checkPasswordErrors() {
      const errors = []
      if (!this.$v.checkPassword.$dirty) {
        return errors
      };
      !this.$v.checkPassword.required && errors.push('Enter your password once more')
      !this.$v.checkPassword.sameAs && errors.push('Password does not match')
      return errors
    },
  },
  methods: {
    ...mapMutations("auth", ["initError"]),
    callParent() {
      this.$emit('turnToggle')
      this.$emit('turnsignUpSnackbar')
    },
    callParent_toggle() {
      this.$emit('turnToggle')
    },
    async signUp() {
      this.$v.$touch()
      if (this.$v.$invalid) {
        console.log('Validation Error!!')
        }
      else {
        await this.$store.dispatch('auth/userRegister', {
          username: this.email,
          password: this.password,
        })
        if (this.signUpError !== null) {
          this.$emit('turnexistSnackbar')
          this.initError()
        }
        else {
          this.$emit('turnToggle')
          this.callParent()
        }
      }
    },
  },
}
</script>

<style scoped>
@media (max-width: 1264px) {
  .signup_width {
    width: 100%
  }
}
>>> .theme--light.v-input:not(.v-input--is-disabled) input, .theme--light.v-input:not(.v-input--is-disabled) textarea {
  color: white;
}
>>> .theme--light.v-text-field > .v-input__control > .v-input__slot:before {
  border-color : rgba(255, 255, 255, 0.5);
}
>>> .v-text-field.v-input--has-state > .v-input__control > .v-input__slot:before {
  border-color : currentColor;
}
>>> .theme--light.v-label {
  color: white;
}
>>> .theme--light.v-icon {
  color: white;
}
>>> .theme--light.v-select .v-select__selections {
  color: white;
}
>>> .theme--light.v-text-field:not(.v-input--has-state) > .v-input__control > .v-input__slot:hover:before {
  border-color: white;
}
</style>