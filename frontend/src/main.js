import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router/router'

import '@/assets/css/theme.min.css';
import '@/assets/fonts/feather/feather.css';
import '@/assets/fonts/mdi/font/css/materialdesignicons.min.css';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

import 'jquery/src/jquery.js'
import 'popper.js/dist/popper.min.js'
import 'bootstrap/dist/js/bootstrap.min.js'


createApp(App).use(router).mount('#app')
