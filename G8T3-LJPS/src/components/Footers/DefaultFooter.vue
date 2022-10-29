<template>

	<!-- Layout Footer -->
	<a-layout-footer>

		<!-- Footer Navigation Menu -->
		<a-menu mode="horizontal" style="margin-top: 150px">
			<a-menu-item>Company </a-menu-item>
			<a-menu-item>About Us</a-menu-item>
			<a-menu-item>Team </a-menu-item>
			<a-menu-item>Products</a-menu-item>
			<a-menu-item>Blog</a-menu-item>
			<a-menu-item>Pricing</a-menu-item>
		</a-menu>
		<!-- / Footer Navigation Menu -->

		
		
		<!-- Copyright Notice -->
		<p class="copyright">
			Copyright © 2022 G8T3
			by Group 8 Team 3
		</p>
		<!-- / Copyright Notice -->

	</a-layout-footer>
	<!-- / Layout Footer -->

</template>

<script>

	export default ({
		data() {
			return {
			}
		},
	})

</script>

<style lang="scss" scoped>

	.nav-link svg {
		margin-right: 5px;
		vertical-align: middle;
	}
	.nav-link span {
		vertical-align: middle;
	}
	.ant-menu-submenu-popup {
		width: 100%;
	}

</style>