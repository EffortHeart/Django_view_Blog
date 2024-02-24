<template>
	<PageHomeHeader/>
	<PageHomeContent/>
</template>


<script>
	import PageHomeHeader from '@/components/PageHomeHeader.vue';
	import PageHomeContent from '@/components/PageHomeContent.vue'
	
	export default {
		components: {
			PageHomeHeader,
			PageHomeContent,
		}
	}
</script>