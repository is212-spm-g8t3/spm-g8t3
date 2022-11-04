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
		
		<div v-if="dataFilteredStatus.length == 0">
			<h5>No courses available.</h5>
		</div>

		<a-row type="flex" :gutter="[24,24]" align="stretch">
			<!-- Project Column -->
			<a-col :span="24" :md="6" v-for="(item, index) in dataFilteredStatus" :key="index">
				<!-- Project Card -->
				<a-card class="card-info" hoverable bodyStyle="height:200px;">
					<template #cover>
						<img
						alt="example"
						:src="courseImage[index]"
						style="border-radius: 10px 10px 0px 0px; height:200px;"
						/>
					</template>
					<div class="card-tag">{{item.Course_Category}}</div>
					<h5>{{item.Course_Name}}</h5>
					<p class="text">
						{{item.Course_Description}}
					</p>
					<template #actions>
						<h6 v-on:click="selectCourse(item.Course_ID)"
						block
						style='color: black'
						>
							{{ item.isInCart == true ? "Remove" : "Add" }}
						</h6>
					</template>

					<!-- <template #actions>
						<a-button type="link" style="width: 90%; margin: 0px; padding: 0px; height: 25px; color: black" size="large">Select</a-button>
					</template> -->
				</a-card>
				<!-- / Project Card -->
			</a-col>
			<!-- / Project Column -->
		</a-row>
		<div>
			<a-row type="flex" style="margin-bottom: 10px;">
				<a-col :span="24" :md="12" style="text-align: left;">
					<a-button type="dark" @click="backToSkill()" style="margin-top: 20px;">
						Back
					</a-button>
				</a-col>
				<a-col :span="24" :md="12" style="text-align: right;">
					<a-button v-if="this.$route.query.type == 'addToLJ'" @click="checkout()" type="dark" style="margin-top: 20px; margin-left: 20px;">
						Save
					</a-button>
					<a-button v-else type="dark" onclick="history.back()" style="margin-top: 20px;">
						Confirm
					</a-button>
				</a-col>
			</a-row>
			
			

		</div>


	</div>

</template>




<script>

	import axios from 'axios';

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
			selectCourse(courseId){
				for (let course of this.courseData){
					if (course.Course_ID == courseId){
						course.isInCart = true
					}
				}

				let skillId = this.$route.query.skillId

				//handle skills selection
				let selectedSkillsAndCourses = JSON.parse(localStorage.getItem('selectedSkillsAndCourses'));
				
				if (selectedSkillsAndCourses === null){
					selectedSkillsAndCourses = {}
				}

				if (!(skillId in selectedSkillsAndCourses)){
					// if selected skills is null then initialise selected skills array.
					
					let skillCourse = [courseId] //initialise course list
					selectedSkillsAndCourses[skillId] = skillCourse
				} else{

					//check if courseId is in list of courses
					if (!selectedSkillsAndCourses[skillId].includes(courseId)){

						selectedSkillsAndCourses[skillId].push(courseId) //add skill course object
					} else {
						const index = selectedSkillsAndCourses[skillId].indexOf(courseId);
						if (index > -1) { // only splice array when item is found
							selectedSkillsAndCourses[skillId].splice(index, 1); // 2nd parameter means remove one item only

							for (let course of this.courseData){
								if (course.Course_ID == courseId){
									course.isInCart = false
								}
							}
						}

						if (selectedSkillsAndCourses[skillId].length == 0) {
							delete selectedSkillsAndCourses[skillId]
						}
					}
				}

				localStorage.setItem('selectedSkillsAndCourses', JSON.stringify(selectedSkillsAndCourses));
				location.reload()
			},

			checkout(){
				//checkout skills and courses
				let sendData = confirm("You are about to save a learning journey. Proceed?");

				if (sendData == false){
					return
				}

				let skillId = this.$route.query.skillId
				let selectedSkillsAndCourses = JSON.parse(localStorage.getItem('selectedSkillsAndCourses'));
				let staffInfo = JSON.parse(localStorage.getItem('staffInfo'));
				let staffId = staffInfo['staffId'];
				
				//save learning journey courses
				for (let course of selectedSkillsAndCourses[skillId]){
					let coursePayload = { skill_id: skillId, 
						staff_id: staffId, 
						reg_id: 1, 
						course_id: course, 
						lj_id: this.$route.query.LJId
					};
					let coursePath = 'http://localhost:5000/learningJourney/addLearningJourneyCourse';
					axios.post(coursePath, coursePayload)
						.then((res) => {
							console.log("Learning Journey course Successfully saved")
						})
						.catch((error) => {
							console.error(error);
						});
				}

				alert("Learning Journey successfully created")
				localStorage.removeItem('selectedSkillsAndCourses');
				history.back()
			
				//save learning journey skills
				// for (let skill in selectedSkillsAndCourses){
				// 	console.log(skill)
				// 	let skillPayload = { skill_id: skill, staff_id: staffId, lj_id: 13 };
				// 	let skillPath = 'http://localhost:5000/learningJourney/createLearningJourneySkill';
				// 	axios.post(skillPath, skillPayload)
				// 		.then((res) => {
				// 			console.log("Learning Journey skill Successfully saved")
							
				// 		})
				// 		.catch((error) => {
				// 		// eslint-disable-next-line
				// 		console.error(error);
				// 		});
				// }
			},

			backToSkill() {
				localStorage.removeItem('selectedSkillsAndCourses');
				history.back()
			}
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