<template>
    <nav class="navbar navbar-expand-lg navbar-default">
        <div class="container-fluid px-0">
            <router-link to="/" class="navbar-brand">
                <img
                    alt="pixeltail-logo"
                    src="../assets/img/logo.svg">
            </router-link>

            <!-- button -->
            <button
                class="navbar-toggler collapsed shadow-none"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbar-default"
                aria-controls="navbar-default"
                aria-expanded="false"
                aria-label="toggle navigation"
            >
                <span class="icon-bar top-bar mt-0"></span>
                <span class="icon-bar middle-bar"></span>
                <span class="icon-bar bottom-bar"></span>
            </button>

            <!-- collapse -->
            <div class="collapse navbar-collapse" id="navbar-default">

                <!-- search input -->
                <form class="mt-3 mt-lg-0 mx-lg-5 mx-sm-0 d-flex align-items-center w-100">
                    <span class="position-absolute ps-3 search-icon">
                        <i class="fe fe-search"></i>
                    </span>
                    <input
                        type="search"
                        class="form-control ps-6 shadow-none"
                        placeholder="Search articles"
                    />
                </form>

                <div class="ms-auto mt-3 mt-lg-0">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <router-link
                                class="nav-link"
                                to="/" exact>
                                Home  
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link
                                class="nav-link"
                                to="/blog" exact>
                                Blog  
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link
                                class="nav-link"
                                to="/about" exact>
                                About
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'Navbar',
    }
</script>
