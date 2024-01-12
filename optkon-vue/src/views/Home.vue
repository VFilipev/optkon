<template>
  <v-container>
  <v-card>
    <v-data-iterator :items="productList" :items-per-page="20" :search="search">
      <template v-slot:header>
        <v-toolbar class="px-2">
          <v-text-field v-model="search" clearable density="comfortable" hide-details placeholder="Поиск"
            prepend-inner-icon="mdi-magnify" style="width: 100%;" variant="solo"></v-text-field>
        </v-toolbar>
      </template>

      <template v-slot:default="{ items }">
        <v-container class="pa-2" fluid>
          <v-row dense>
            <v-col v-for="item in items" :key="item.id" cols="12" lg="2">
              <v-card class="pb-3" border hover @click="toDetail(item.raw.id)">
                <v-img :src="item.raw.img" :height="150" cover></v-img>

                <v-list-item class="mb-2" :subtitle="item.raw.category.name">
                  <template v-slot:title>
                    <strong class="text-subtitle-2 mb-2">{{ item.raw.name }}</strong>
                  </template>
                </v-list-item>

                <div class="d-flex justify-space-between px-4">
                  <div class="d-flex align-center text-caption text-medium-emphasis me-1">
                    <v-icon icon="mdi mdi-weight" start></v-icon>

                    <div class="text-truncate">{{ item.raw.weight + ' кг' }}</div>
                  </div>

                  <v-btn v-if="isSelect(item)" color="select" border flat size="small" class="text-none" @click.stop="removeProduct(item)">
                    В корзине
                  </v-btn>
                  <v-btn v-else border flat size="small" class="text-none" @click.stop="addProduct(item)">
                    В корзину
                  </v-btn>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </template>

      <template v-slot:footer="{ page, pageCount, prevPage, nextPage }">
        <div class="d-flex align-center justify-center pa-4">
          <v-btn :disabled="page === 1" icon="mdi-arrow-left" density="comfortable" variant="tonal" rounded
            @click="prevPage"></v-btn>

          <div class="mx-2 text-caption">
            Страница {{ page }} из {{ pageCount }}
          </div>

          <v-btn :disabled="page >= pageCount" icon="mdi-arrow-right" density="comfortable" variant="tonal" rounded
            @click="nextPage"></v-btn>
        </div>
      </template>
    </v-data-iterator>
  </v-card>
</v-container>
</template>
<script>
import { Product } from '../api'
import { useCartStore } from "../store/app";
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
export default {

  name: 'home-page',
  components: {},
  setup() {
    const cartStore = useCartStore()
    const isSelect = (product) => {
      let findIndex = cartStore.cartItems.findIndex(x => x.product.id == product.raw.id)
      if (findIndex >= 0) { return true }
      else { return false }
    }
    const addProduct = (product) => {
      cartStore.cartItems.push({'count':1,'product':product.raw})
    }
    const removeProduct = (product) =>{
      let findIndex = cartStore.cartItems.findIndex(x => x.product.id == product.raw.id)
      cartStore.cartItems.splice(findIndex, 1)
    }
    let search = ref('')
    let productList = ref([])
    const getProduct = async () =>{
      productList.value = (await Product.getList({ 'available': true })).results
    }
    const router = useRouter()
    const toDetail = (productId) =>{
      router.push({'name': 'ProductDetail', params:{productId}})
    }
    onMounted(()=>{
      getProduct()
    })
    return {
      search,
      productList,
      addProduct,
      isSelect,
      removeProduct,
      toDetail
    }
  }
}
</script>
<style>
</style>