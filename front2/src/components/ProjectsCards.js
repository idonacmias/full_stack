import Project from './Project'

function ProjectsCards(props){
	return (
		<>
		<p>ProjectsCards</p>
		<p>{props.cards.map((project, i) =>  {
			return <Project key={i} name={project.name} photo={project.photo} index={i}/>

		} )}</p>
		</>
	);
}

export default ProjectsCards;
