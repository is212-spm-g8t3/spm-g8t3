<template>	
	<!-- Projects Table Card -->
	<div>
		<a-row type="flex" style="margin-bottom: 10px;">
			<a-col :span="24" :md="12" style="text-align: left;">
				<h3>Courses</h3>
			</a-col>
			<a-col :span="24" :md="12" style="text-align: right;">
				<a-input-search
					v-model:value="search"
					placeholder="Search for Course"
					style="width: 250px; margin-bottom: 0px"
				/>
			</a-col>
		</a-row>

		<a-row type="flex" :gutter="[24,24]" align="stretch">
			<!-- Project Column -->
			<a-col :span="24" :md="6" v-for="(item, index) in dataFilteredStatus" :key="index">
				<!-- Project Card -->
				<a-card class="card-info" hoverable @click="selectCourse" bodyStyle="height:200px;">
					<template #cover>
						<img
						alt="example"
						:src="courseImages[index]"
						style="border-radius: 10px 10px 0px 0px; height:200px;"
						/>
					</template>
					<div class="card-tag">{{item.Course_Category}}</div>
					<h5>{{item.Course_Name}}</h5>
					<p class="text">
						{{item.Course_Description}}
					</p>
					<!-- <template #actions>
						<a-button type="link" style="width: 90%; margin: 0px; padding: 0px; height: 25px; color: black" size="large">Select</a-button>
					</template> -->
				</a-card>
				<!-- / Project Card -->
			</a-col>
			<!-- / Project Column -->
		</a-row>
	</div>
	<!-- / Projects Table Card -->
</template>

<script>

	export default ({
		props: {
			// data: {
			// 	type: Array,
			// 	default: () => [],
			// },
			courseData: {
				type: Array,
				default: () => [],
			},
			courseImage: {
				type: Array,
				default: () => [],
			},
		},
		data() {
			return {
				search: '',
				courseImages: ["/images/back-end-engineering.jpg", "/images/ux-ui.png", "/images/data-scientist.jpg", "/images/front-end-engineer.jpeg"]
			}
		},

		methods: {
			selectCourse(){
				console.log("Hello!")
				let text;
  				if (confirm("Confirm course selection?") == true) {
					text = "Selection confirmed!";
					alert(text)
				} else {
					text = "You canceled!";
					alert(text)
  				}
			},
		},
		computed: {
			dataFilteredStatus: function() {
				if (this.search != '') {
					return this.courseData.filter(eachCourse => 
						eachCourse.Course_Name.toLowerCase().includes(this.search.toLowerCase()) || 
						eachCourse.Course_Description.toLowerCase().includes(this.search.toLowerCase()) || 
						eachCourse.Course_Category.toLowerCase().includes(this.search.toLowerCase()));
				}
				return this.courseData
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