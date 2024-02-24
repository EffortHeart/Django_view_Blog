<template>
    <div class="py-4 py-lg-8 pb-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-8 col-lg-8 col-md-12 col-12">
                    <div class="text-center mb-4">
                        <a href="#" class="fs-5 fw-semi-bold d-block mb-4 text-primary">
                            Course
                        </a>

                        <h1 class="display-3 fw-bold mb-4">
                            {{ $route.params.name }}
                        </h1>
                    </div>

                    <div class="d-flex justify-content-between align-items-center mb-5">
                        <div class="d-flex align-items-center">
                            <div class="ms-2 lh-1">
                                {{ $route.params.published }}
                            </div>
                        </div>
                        <div>
                            <span class="ms-2 text-muted">Partager</span>
                            <a href="#" class="ms-2 text-muted"><i class="fab fa-facebook"></i></a>
                            <a href="#" class="ms-2 text-muted"><i class="fab fa-twitter"></i></a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row justify-content-center">
                <div class="col-xl-10 col-lg-10 col-md-12 col-12 mb-6">
                    <img src="../assets/img/blog/blogpost-2.jpg" alt="{{ $route.params.name }}" class="img-fluid rounded-3">
                </div>
                
                <article class="col-xl-8 col-lg-8 col-md-12 col-12 mb-2">
                    <p class="lead text-dark">
                        {{ $route.params.subtitle }}
                    </p>

                    {{ $route.params.body }}
                </article>
            </div>
        </div>
    </div>
</template>