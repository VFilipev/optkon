<template>
    <div class="bg-gray">
        <v-container>
            <div class="text-h4 mb-3">
                {{ obj.name }}
            </div>
            <v-card>
                <v-card-item>
                    <v-row>
                        <v-col cols="12" lg="4">
                            <v-img cover :src="obj.img" />
                            <div class="d-flex flex-wrap" style="width: 100%;">
                                <div class="card">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                                <div class="card2">
                                    <div class="card-body"></div>
                                </div>
                            </div>
                        </v-col>
                        <v-col cols="12" lg="8" class="d-flex flex-column justify-space-between">
                            <div>
                                <v-row>
                                    <v-col cols="4" lg="3" >
                                        <div class="text-subtitle-1 font-weight-bold">Категория:</div>
                                    </v-col>
                                    <v-col cols="8" lg="9">
                                        <div>{{ obj.category?.name }}</div>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="4" lg="3">
                                        <div class="text-subtitle-1 font-weight-bold">Вес в упаковке:</div>
                                    </v-col>
                                    <v-col cols="8" lg="9">
                                        <div>{{ obj.weight + ' кг' }}</div>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="4" lg="3">
                                        <div class="text-subtitle-1 font-weight-bold">Описание:</div>
                                    </v-col>
                                    <v-col cols="8" lg="9">
                                        <div>{{ obj.description }}</div>
                                    </v-col>
                                </v-row>
                            </div>
                            <div>
                                <v-card-actions>
                                    <v-btn v-if="isSelect()" color="select" border flat class="text-none"
                                        @click="removeProduct(item)">
                                        В корзине
                                    </v-btn>
                                    <v-btn v-else border flat class="text-none" @click="addProduct">
                                        В корзину
                                    </v-btn>
                                </v-card-actions>
                            </div>                            
                        </v-col>
                    </v-row>
                </v-card-item>
            </v-card>
        </v-container>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { Product } from '@/api';
import { useCartStore } from '@/store/app';
export default {
    name: 'product-detail',
    setup() {
        const cartStore = useCartStore()
        const route = useRoute()
        const objId = route.params.productId
        let obj = ref({})
        const getProduct = async () => {
            obj.value = (await Product.getById(objId))
        }
        const addProduct = () => {
            cartStore.cartItems.push({ 'count': 1, 'product': obj.value })
        }
        const isSelect = () => {
            let findIndex = cartStore.cartItems.findIndex(x => x.product.id == obj.value.id)
            if (findIndex >= 0) { return true }
            else { return false }
        }
        const removeProduct = () => {
            let findIndex = cartStore.cartItems.findIndex(x => x.product.id == obj.value.id)
            cartStore.cartItems.splice(findIndex, 1)
        }
        onMounted(() => {
            getProduct()
        })
        return {
            obj,
            addProduct,
            isSelect,
            removeProduct
        }
    }
}
</script>
<style scoped>
.bg-gray {
    min-height: 100%;
    background-color: rgb(246, 246, 246);
}

.card {
    width: 33%;
    padding: 5px;
    height: 110px;
}

.card-body {
    background-color: darkgray;
    width: 100%;
    height: 100%;
    background-image: url(/camera-custom.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
}

.card2 {
    width: 24.7%;
    padding: 5px;
    height: 90px;
}
</style>