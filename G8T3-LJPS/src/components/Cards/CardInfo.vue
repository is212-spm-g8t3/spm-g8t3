<template>
	<a-card hoverable class="card-info" @click="selectRole" style="height: 370px">
		<template #cover>
			<img alt="example" :src="imageURl" style="height:200px; border-bottom: 1px solid #ededed; border-radius: 10px 10px 0px 0px"/>
		</template>
		<a-row type="flex">
			<a-col class="col-content" :span="24" :xl="12">
				<div class="card-content">
					<h6>Role</h6>
					<h5>{{roleName}}</h5>
					<p class="text">{{roleDescription}}</p>
				</div>
			</a-col>
		</a-row>
	</a-card>
</template>

<script>

	export default ({
		props: {
			id: {
				type: Number,
				default: "",
			},
			staffId: {
				type: Number,
				default: "",
			},
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
		methods: {
			selectRole() {
				this.$router.push({
					// name: 'Learning-Journey-Role',
					// params: {
					// 	staffId: this.staffId,
					// 	roleId: this.roleId,
					// 	roleName: this.roleName,
					// 	roleDescription: this.roleDescription,
					// 	imageURl: this.imageURl
					// }
					path: '/learning-journey-role', 
					query: { 
						LJId: this.id,
					}
				});
			}
		}
	})

</script>

<style scoped>
.text {
   overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 3; /* number of lines to show */
           line-clamp: 3; 
   -webkit-box-orient: vertical;
}
</style>