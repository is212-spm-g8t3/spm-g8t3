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
				<a-col :span="24" :md="6" v-for="index in correctCourseList" :key="index">

					<!-- Project Card -->
					<a-card class="card-project">
						<img
						slot="cover"
						alt="example"
						src="/images/ux-ui.png"
						/>
						<div class="card-tag">{{index.Course_Category}} {{index.Course_ID}} </div>
						<h5>{{index.Course_Name}}</h5>
						<p>
							{{index.Course_Description}}
						</p>
					</a-card>
					<!-- / Project Card -->

				</a-col>
				<!-- / Project Column -->
				
			</a-row>

		</template>



	</a-card>
	<!-- / Projects Table Card -->

</template>

<script>
	import axios from 'axios';


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
				correctCourseList: [],
				allCourse:[],
				skill: "Core",
				// Active button for the "Projects" table's card header radio button group.
				projectHeaderBtns: 'all',
			}
		},

		methods:{
			getCourses(){
				const course_url = "http://localhost:5000/courses"
				axios.get(course_url)
					.then((res) => {
						// console.log(res.data.data.courseCatalog)

						this.allCourse = res.data.data.courseCatalog
						
						for(let i=0; i < this.allCourse.length; i++){
							var course = this.allCourse[i]
							if(this.skill==course.Course_Category && course.Course_Status == "Active"){
								this.correctCourseList.push(this.allCourse[i])
							}
						}
						console.log(this.correctCourseList)
						

					})
					.catch((error) => {
						console.error(error);
					});
			},
			handleOk(e) {
			console.log(e);
			this.visible = false;
			},
		},
		created(){
			this.getCourses();
		}

	})

</script>