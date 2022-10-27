<template>
	<div>
		<!-- Title -->
		<!-- <a-row :gutter="24" style="margin-bottom: 15px;">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Courses</h3>
			</a-col>			
			<a-col :span="24" :md="12" style="text-align: right; padding-right: 25px;">
				<a-input-search
					v-model:value="search"
					placeholder="Search for Course"
					style="width: 250px; margin-bottom: 0px"
				/>
			</a-col>
		</a-row> -->
		<!-- / Title -->

		<!-- Table & Timeline -->
		<a-row :gutter="24" type="flex" align="stretch" style="margin:0px;">
			<!-- Table -->
			<a-col :span="24" :lg="24" class="mb-24">
				<!-- Projects Table Card -->
				<CardProjectTable
					:courseData="courses"
					:courseImage="courseSkill"
				></CardProjectTable>
				<!-- / Projects Table Card -->
			</a-col>
			<!-- / Table -->
			<!-- / Timeline -->
		</a-row>
		<!-- / Table & Timeline -->
	</div>
</template>

<script>
	import axios from 'axios';

	// "Projects" table component.
	import CardProjectTable from '../components/Cards/CardProjectTable' ;

	export default ({
		components: {
			CardProjectTable,
		},
		data() {
			return {
				courses: [],
				courseSkill:[],
				skill: "",
				// Active button for the "Projects" table's card header radio button group.
				projectHeaderBtns: 'all',
			}
		},
		methods: {

			getCourses() {
				// Update the skillId later on when merge
				// @app.route("/getCoursesBySkill/<skillID>", methods=['GET']) this.$route.query.roleId
				const course_url = "http://localhost:5000/getCoursesBySkill/" + this.$route.query.skillId
				axios.get(course_url)
					.then((res) => {
						
						if (res.data.code == 200) {
							this.courses = res.data.data.courseCatalog;
							for(let x = 0;x<this.courses.length;x++){
								this.courseSkill.push(res.data.data.courseCatalog[x].Course_Category)
							}
							
							console.log(this.courseSkill)
						}
					})
					.catch((error) => {
						console.error(error);
					});
			},
		},
		created() {
			this.getCourses();
		},
	})

</script>

<style lang="scss">
</style>