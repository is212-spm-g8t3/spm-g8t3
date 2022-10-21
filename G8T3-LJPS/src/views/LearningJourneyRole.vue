<!-- 
	This is the dashboard page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>
        <!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" class="mb-12">
				<h3 style="margin-left: 12px">{{role.name}}</h3>
			</a-col>

            <!-- Left info -->
            <a-col :span="9" class="mb-12">
                <a-card  style="margin-left: 15px;">
                    <h5>
                        Description
                    </h5>

                    <!-- Description -->
                    <p style="font-size: 14px; color: rgba(0, 0, 0, 0.85); margin-bottom: 16px; font-weight: 500">
                        {{role.description}}
                    </p>
                    <!-- Description -->

                    <!-- Skill -->
                    <h5>
                        Skills
                    </h5>
                    <a-card hoverable v-for="(skill, index) in skillsData" :key="index" @click="viewCourse(skill)" :style="selectedSkill == skill ? 'background-color: #ebf9ff; border: 1px #dedede solid;margin-bottom: 15px;' : 'margin-bottom: 15px;'">
                        <h6>{{skill.Skill_Name}}
                            <a-tag color="blue" style="margin-left: 5px">In-progress</a-tag>
                        </h6>
                        
                        <p>{{skill.Skill_Description}}</p>

                    </a-card>
                </a-card>
            </a-col>
            <!-- Left Info -->

            <!-- Right Info -->
            <a-col :span="15" class="mb-12">
                <a-card  style="margin-right: 15px;">
                    <h5>
                        Courses
                    </h5>

                    <a-card hoverable v-for="(course, index) in courseData" :key="index" style="margin-bottom: 15px;">
                        <!-- <template #extra>
                            <a href="#">More</a>
                        </template> -->
                        <h6>{{course.Course_Name}}
                            <a-tag color="blue" style="margin-left: 5px">
                                In-progress
                            </a-tag>
                            <a-tag>{{course.Course_Type}}</a-tag>
                        </h6>
                        <p>{{course.Course_Description}}</p>
                        
                        
                    
                        <template #actions>
                            <a-icon type="check" theme="outlined" />
                            <a-icon type="delete" theme="outlined" />
                        </template>
                    </a-card>
                </a-card>
            </a-col>
            <!-- Right Info -->
		</a-row>
		<!-- Title -->
        <template>
            
        </template>
	</div>
</template>

<script>

	import axios from 'axios';

	export default ({
		components: {
		},
		data() {
			return {
				// Role Data
				role: {},

                // Skill Data
                skillsData: [],
                selectedSkill: {},

                // Course Data
                courseData: [],
			}
		},
		methods: {
            getLearningJourneyRole() {
				const learningJourneyURL = 'http://localhost:5000/learningJourney/getLearningJourneyRole/' + this.$route.query.LJId
				axios.get(learningJourneyURL)
					.then((res) => {
                        let response = res.data.data.Role[0]
                        this.role = {
                            name: response.Job_Role_Name,
                            department: response.Department,
                            description: response.Job_Role_Description,
                        }
					})
					.catch((error) => {
						console.error(error);
					});
			},

            getLearningJourneySkills() {
                const learningJourneyURL = 'http://localhost:5000/learningJourney/getLearningJourneySkills/' + this.$route.query.LJId
				axios.get(learningJourneyURL)
					.then((res) => {
                        for (let skill of res.data.data.Skills) {
                            this.skillsData.push(skill);
                        }


                        // First time load, display first skill courses
                        this.selectedSkill = this.skillsData[0];
                        this.viewCourse(this.selectedSkill);
					})
					.catch((error) => {
						console.error(error);
					});
            },

            viewCourse(skill) {
                this.selectedSkill = skill;
                this.courseData = [];
                const learningJourneyURL = 'http://localhost:5000/getCoursesBySkill/' + this.selectedSkill.Skill_ID;
                axios.get(learningJourneyURL)
                    .then((res) => {
                        for (let course of res.data.data.courses) {
                            this.courseData.push(course);
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                        });
            },
		},
		created() {
            this.getLearningJourneyRole();
            this.getLearningJourneySkills();
            // this.viewCourse(this.selectedSkill);
		}
	})

</script>

<style lang="scss">

</style>