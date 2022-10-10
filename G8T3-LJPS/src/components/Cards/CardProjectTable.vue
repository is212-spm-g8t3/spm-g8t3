<template>
				
	<!-- Projects Table Card -->
	<a-card :bordered="false" class="header-solid h-full">
		<template #title>
			<a-row type="flex" align="middle">
				<a-col :span="24" :md="12">
					<a-button type="light">
						View All Roles
					</a-button>	
				</a-col>
				<a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
					<a-radio-group v-model="projectHeaderBtns" size="small">
						<a-radio-button value="all">Popular</a-radio-button>
						<a-radio-button value="online">Trending</a-radio-button>
						<a-radio-button value="stores">New</a-radio-button>
					</a-radio-group>
				</a-col>
			</a-row>
		</template>

		<template>
			<a-row type="flex" :gutter="[24,24]" align="stretch" style="padding-left: 7px; padding-right: 7px">

				<!-- Project Column -->
				<a-col :span="24" :md="6" v-for="index in 7" :key="index">

					<!-- Project Card -->
					<a-card class="card-project">
						<img
						slot="cover"
						alt="example"
						src="/images/ux-ui.png"
						/>
						<div class="card-tag">Technology</div>
						<h5>UX/UI Designer</h5>
						<p>
							Get a hands-on introduction to the wireframing and prototyping processes using Figma, creating actual deliverables expected of designers using industry-standard tools.
						</p>
					</a-card>
					<!-- / Project Card -->

				</a-col>
				<!-- / Project Column -->

				<!-- Project Column -->
				<a-col :span="24" :md="6">

					<!-- Project Card -->
					<a-card class="card-project">
						<img
						slot="cover"
						alt="example"
						src="/images/home-decor-2.jpeg"
						/>
						<div class="card-tag">Project #2</div>
						<h5>Scandinavian</h5>
						<p>
							Music is something that every person has his or her own specific opinion about.
						</p>
					</a-card>
					<!-- Project Card -->

				</a-col>
				<!-- / Project Column -->
				
			</a-row>

		</template>

	</a-card>
	<!-- / Projects Table Card -->

</template>

<script>

	export default ({
		props: {
			data: {
				type: Array,
				default: () => [],
			},
			columns: {
				type: Array,
				default: () => [],
			},
		},
		data() {
			return {

				// Active button for the "Projects" table's card header radio button group.
				projectHeaderBtns: 'all',
			}
		},
	})

</script>