<!-- 
	This is the dashboard page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" class="mb-12">
				<h3 style="margin-left: 12px">My Learning Journey</h3>
			</a-col>
		</a-row>
		<!-- Title -->


		<!-- Learning Journeys -->
		<a-row :gutter="24" type="flex" style="margin:0px">
			<a-col :span="24" :xl="6" class="mb-24" v-for="(learningJourney, index) in learningJourneys" :key="index">
				<CardInfo 
					:id="learningJourney.id"
					:staffId="learningJourney.staffId"
					:roleName="learningJourney.name"
					:roleDescription="learningJourney.description"
					:imageURl="learningJourney.imageURL"
				></CardInfo>
			</a-col>
		</a-row>

		<!-- Learning Journeys -->

		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" class="mb-12">
				<h3 style="margin-left: 12px">Statistics</h3>
			</a-col>
		</a-row>
		<!-- Title -->

		<!-- Charts -->
		<a-row :gutter="24" type="flex" align="stretch" style="margin:0px">
			<a-col :span="24" :lg="10" class="mb-24">

				<!-- Active Users Card -->
				<CardBarChart></CardBarChart>
				<!-- Active Users Card -->

			</a-col>
			<a-col :span="24" :lg="14" class="mb-24">
				
				<!-- Sales Overview Card -->
				<CardLineChart></CardLineChart>
				<!-- / Sales Overview Card -->

			</a-col>
		</a-row>
		<!-- / Charts -->
	</div>
</template>

<script>

	// Learning Journey.
	import CardInfo from '../components/Cards/CardInfo' ;
	// Bar chart for "Active Users" card.
	import CardBarChart from '../components/Cards/CardBarChart' ;
	// Line chart for "Sales Overview" card.
	import CardLineChart from '../components/Cards/CardLineChart' ;
	import axios from 'axios';

	const stats = [
		{
			title: 'Front-End Engineer',
			description: 'Front-end engineers path will teach you not only the necessary languages and technologies, but how to think like a front-end engineer, too.',
			imageURl: 'images/front-end-engineer.jpeg'
		},
		{
			title: 'Back-End Engineer',
			description: 'Back-End Engineers path, you will start with programming servers and client-side interfaces, then level up to designing databases.',
			imageURl: 'images/back-end-engineering.jpg'
		},
		{
			title: 'Data Scientist',
			description: 'Analytics is all about using data to answer questions, and you will learn how to analyze data, build dashboards, and deliver impactful reports.',
			imageURl: 'images/data-scientist.jpg'
		},
				{
			title: 'Data Scientist',
			description: 'Analytics is all about using data to answer questions, and you will learn how to analyze data, build dashboards, and deliver impactful reports.',
			imageURl: 'images/data-scientist.jpg'
		},
	];

	export default ({
		components: {
			CardBarChart,
			CardLineChart,
			CardInfo,
		},
		data() {
			return {
				// Counter Widgets Stats
				stats,
				learningJourneys: []
			}
		},
		methods: {
			getStaffLearningJourneys() {

                // TODO: Change Staff ID to dynamic
				let staffInfo = JSON.parse(localStorage.getItem('staffInfo'));

				const learningJourneyURL = 'http://localhost:5000/learningJourney/viewStaffLearningJourneys/' + staffInfo['staffId']
				axios.get(learningJourneyURL)
					.then((res) => {
						// console.log(res);
						for (let learningJourney of res.data.data.learning_journeys) {

							this.learningJourneys.push({
								staffId: learningJourney.Staff_ID,
								id: learningJourney.LJ_ID,
								name: learningJourney.Job_Role_Name,
								description: learningJourney.Job_Role_Description,
								department: learningJourney.Department,
								imageURL: 'images/front-end-engineer.jpeg',
							})
						}
					})
					.catch((error) => {
						console.error(res.message);
					});
			},
		},
		created() {
			this.getStaffLearningJourneys();
		}
	})

</script>

<style lang="scss">

</style>