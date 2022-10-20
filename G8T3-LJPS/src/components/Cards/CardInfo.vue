<template>
	<a-card hoverable class="card-info">
		<template #cover>
			<img alt="example" :src="imageURl" style="height:200px; border-bottom: 1px solid #ededed; border-radius: 10px 10px 0px 0px"/>
		</template>
		<a-row type="flex">
			<a-col class="col-content" :span="24" :xl="12">
				<div class="card-content">
					<h6>Role</h6>
					<h5>{{roleName}}</h5>
					<p>{{roleDescription}}</p>
				</div>
			</a-col>
		</a-row>
	</a-card>
</template>

<script>

	export default ({
		props: {
			roleName: {
				type: String,
				default: "",
			},
			roleDescription: {
				type: String,
				default: "",
			},
			imageURl: {
				type: String,
				default: "",
			}
		},
		data() {
			return {
			}
		},
	})

</script>

