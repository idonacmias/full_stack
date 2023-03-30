import Project from './Project'

function ProjectsCards(props){
	const cards = [{name:'bob', photo:'/myPhoto.jpeg'}, {name:'bob2', photo:'/myPhoto.jpeg'}, {name:'bob3', photo:'/myPhoto.jpeg'}];

	return (
		<>
		<h1>ProjectsCards</h1>
		<p>{cards.map((project, i) =>  {
			return <Project key={i} name={project.name} photo={project.photo} index={i}/>

		} )}</p>
		</>
	);
}

export default ProjectsCards;
