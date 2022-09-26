<template>

	<a-card :bordered="false" class="card-info">
		<a-row type="flex">
			<a-col class="col-content" :span="24" :xl="12">
				<div class="card-content">
					<h6>Role</h6>
					<h5>{{title}}</h5>
					<p>{{description}}</p>
				</div>
			</a-col>
			<a-col class="col-img" :span="24" :xl="12">
				<div class="card-img-bg" style="width: 447px">
					<img style="object-fit: cover;" :src="imageURl" alt="">
				</div>
			</a-col>
		</a-row>
	</a-card>

</template>

<script>

	export default ({
		props: {
			title: {
				type: String,
				default: "",
			},
			description: {
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