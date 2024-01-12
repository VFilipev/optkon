<template>
  <v-app-bar flat>
    <v-app-bar-title>
      <v-container>
        <div class="d-flex justify-space-between">
          <div>
            <v-icon icon="mdi mdi-cupcake" />
            ОптКонд

          </div>
          <template v-if="cartStore.cartItems">
            <v-badge :content="cartStore.cartItems.length" inline>
              <v-icon icon="mdi mdi-cart" role="button" @click="toCart" />
            </v-badge>
          </template>
        </div>
      </v-container>
    </v-app-bar-title>
  </v-app-bar>
</template>

<script>

import { useCartStore } from "../store/app";
import { useRouter } from "vue-router"

export default {
  name: 'app-bar',
  setup() {
    const cartStore = useCartStore()
    const router = useRouter()
    const toCart = () => {
      router.push({ name: 'Cart' })

    }
    return {
      cartStore,
      toCart
    }
  }
}

// const cartStore = useCartStore()

</script>

<style>
.v-toolbar__content>.v-toolbar-title {
  margin-inline-end: 16px;
}
</style>