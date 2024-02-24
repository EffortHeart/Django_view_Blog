import { createRouter, createWebHistory } from 'vue-router'


const routes = [
	{
		path: '/',
		name: 'Home',
		component: () => import('../views/Home.vue')
	},
	{
		path: '/blog',
		name: 'Blog',
		component: () => import('../views/Blog.vue')
	},
	{
		path: '/blog/article/:slug/',
		name: 'PostDetail',
		component: () => import('../views/PostDetail.vue')
	},
	{
		path: '/about',
		name: 'About',
		component: () => import('../views/About.vue')
	},
	{
		path: "/:catchAll(.*)*",
		name: "404",
		component: () => import('../views/PageNotFound.vue')
	},
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

export default router
