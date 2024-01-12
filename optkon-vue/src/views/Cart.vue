<template>
    <v-container class="">
        <template v-if="cartStore.cartItems.length > 0">
            <div class="text-h5"> Корзина </div>
            <v-table fixed-header max-height="500px" :hover=true density="compact">
                <thead>
                    <tr>
                        <th class="text-center">
                            №
                        </th>
                        <th class="text-left">
                            Название
                        </th>
                        <th class="text-center">
                            Вес уп.
                        </th>
                        <th class="text-center">
                            Кол-во
                        </th>
                        <th class="text-left">
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in cartStore.cartItems" :key="item.id">
                        <td class="text-center">{{ index + 1 }}</td>
                        <td>{{ item.product.name }}</td>
                        <td class="text-center">{{ item.product.weight }}</td>
                        <td class="text-center">
                            <div class="d-flex align-center justify-center">
                                <v-btn size="x-small" variant="text" icon="mdi mdi-minus" @click="removeQuantity(item)" />

                                <div class="mx-2 justify-center">
                                    {{ item.count }}
                                </div>

                                <v-btn size="x-small" variant="text" icon="mdi mdi-plus" @click="addQuantity(item)" />
                            </div>
                        </td>
                        <td class="text-center">
                            <v-icon icon="mdi mdi-delete-outline" color="red-lighten-2" role="button"
                                @click="removeProduct(item)" />
                        </td>
                    </tr>
                </tbody>
            </v-table>
            <v-dialog transition="dialog-bottom-transition" width="1200">
                <template v-slot:activator="{ props }">
                    <v-btn class="mt-2" variant="outlined" color="primary" size="small" v-bind="props">
                        Оформить заказ
                    </v-btn>
                </template>
                <template v-slot:default="{ isActive }">
                    <v-card>
                        <v-toolbar color="primary" title="Оформление заказа" />
                        <v-card-text>
                            <template v-if="!isConfirmOrder">
                                <v-form @submit.prevent="submit">
                                    <v-text-field v-model="name.value.value" :counter="10"
                                        :error-messages="name.errorMessage.value" label="ФИО"></v-text-field>

                                    <v-text-field v-model="phone.value.value" :counter="7"
                                        :error-messages="phone.errorMessage.value" label="Телефон"></v-text-field>

                                    <v-text-field v-model="email.value.value" :error-messages="email.errorMessage.value"
                                        label="E-mail"></v-text-field>
                                    <div class="d-flex justify-space-between">
                                        <v-btn variant="text" type="submit" color="select">Подтвердить</v-btn>
                                        <v-btn variant="text" @click="isActive.value = false">Закрыть</v-btn>
                                    </div>
                                </v-form>
                            </template>
                            <template v-else>
                                <div class="text-h3 d-flex justify-center flex-column align-center">
                                    <v-icon icon="mdi mdi-check-circle" size="x-large" color="success"
                                        style="font-size: 75px;" />
                                    <div>
                                        Спасибо за заказ!
                                    </div>
                                    <v-btn @click="toHome" class="mt-2" variant="outlined"
                                        color="primary">
                                        На главную
                                    </v-btn>
                                </div>
                            </template>
                        </v-card-text>
                    </v-card>
                </template>
            </v-dialog>
        </template>
        <template v-else>
            <div class="text-h5">
                Корзина пуста
            </div>
            <v-btn class="mt-2" variant="outlined" color="primary" size="small" @click="$router.push({ name: 'Home' })">
                Вернуться к каталогу
            </v-btn>
        </template>
    </v-container>
</template>
<script>
import { useCartStore } from "../store/app";
import { ref } from "vue"
import { useField, useForm } from 'vee-validate'
import { Order } from "@/api"
import { useRouter } from "vue-router";
export default {
    name: 'cart-page',
    setup() {
        const isConfirmOrder = ref(false)
        const cartStore = useCartStore()
        const removeProduct = (product) => {
            let findIndex = cartStore.cartItems.findIndex(x => x.product.id == product.product.id)
            cartStore.cartItems.splice(findIndex, 1)
        }
        const removeQuantity = (item) => {
            if (item.count > 0) {
                item.count -= 1
            }
        }
        const addQuantity = (item) => {
            item.count += 1
        }
        const isActive = ref(false)
        let customer = ref({})
        const { handleSubmit, handleReset } = useForm({
            validationSchema: {
                name(value) {
                    if (value?.length >= 2) return true

                    return 'Имя должно содержать не менее 2 символов.'
                },
                phone(value) {
                    if (value?.length > 10 && /[0-9-]+/.test(value)) return true

                    return 'Номер телефона должен состоять как минимум из 11 цифр.'
                },
                email(value) {
                    if (/^[a-z.-]+@[a-z.-]+\.[a-z]+$/i.test(value)) return true

                    return 'Укажите действительный адрес электронной почты.'
                },
            },
        })
        const name = useField('name')
        const phone = useField('phone')
        const email = useField('email')
        const items = ref([
            'Item 1',
            'Item 2',
            'Item 3',
            'Item 4',
        ])
        let order = ref({})
        const saveOrder = async () => {
            order.value.name = name.value.value
            order.value.phone = phone.value.value
            order.value.email = email.value.value
            let tmp = []
            for (let item of cartStore.cartItems) {
                tmp.push({ 'count': item.count, 'product': item.product.id })
            }
            order.value.products_set = tmp
            isConfirmOrder.value = true
            await Order.save(order.value)
        }
        const submit = handleSubmit(values => {
            saveOrder()
        })
        const router = useRouter()
        const toHome = () =>{
            cartStore.cartItems = []
            router.push({ name: 'Home' })
        }
        return {
            cartStore,
            removeProduct,
            removeQuantity,
            addQuantity,
            isActive,
            customer,
            name,
            phone,
            email,
            items,
            submit,
            saveOrder,
            isConfirmOrder,
            toHome
        }
    }
}
</script>
<style>
table {
    border: 1px solid #e6e6e6;
}

table th {
    border-top: 1px solid #e6e6e6;
}

table th+th {
    border-left: 1px solid #e6e6e6;
}

table td+td {
    border-left: 1px solid #e6e6e6;
}
</style>