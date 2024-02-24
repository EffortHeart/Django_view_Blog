<template>
    <div class="pb-8">
        <div class="container">
            <div class="row">
                <article v-for="post in Articles" v-bind:key="post.uuid" class="col-xl-4 col-lg-4 col-md-6 col-12">
                    <div class="card mb-4 shadow-lg">
                        <router-link
                            :to="{ name: 'PostDetail', params: { uuid: post.uuid, name: post.name, subtitle: post.subtitle, body: post.body, image: post.image, published: post.published, slug: post.slug } }"
                            class="card-img-top"
                        >
                            <img
                                src="{{ post.image }}"
                                class="card-img-top rounded-top-md"
                                alt="{{ post.name }}"
                            >
                        </router-link>

                        <div class="card-body">
                            <router-link
                                :to="{ name: 'PostDetail', params: { uuid: post.uuid, name: post.name, subtitle: post.subtitle, body: post.body, image: post.image, published: post.published, slug: post.slug } }"
                                class="fs-5 fw-semi-bold d-block mb-3 text-danger"
                            >{{ post.category }}</router-link>
                            <h3>
                                <router-link
                                    :to="{ name: 'PostDetail', params: { uuid: post.uuid, name: post.name, subtitle: post.subtitle, body: post.body, image: post.image, published: post.published, slug: post.slug } }"
                                    class="text-inherit"
                                >
                                    {{ post.name }}
                                </router-link>
                            </h3>

                            <p>{{ post.subtitle }}</p>

                            <div class="row align-items-center g-0 mt-4">
                                <div class="col lh-1">
                                    <p class="fs-6 mb-0">
                                        {{ post.published }}
                                    </p>
                                </div>

                                <div class="col-auto">
                                    <p class="fs-6 mb-0">8 Min Read</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </div>
</template>

<script>
    import { getApi } from "../axios"
    export default {
        name: 'PageHomeContent',
        data () {
            return {
                Articles: []
            }
        },
        created () {
            getApi.get('/api/v1/~/post/', )
                .then(response => {
                    console.log('Post API has recieved data')
                    this.Articles = response.data
                }).catch(err => {
                    console.log(err)
                });
        }
    }
</script>
