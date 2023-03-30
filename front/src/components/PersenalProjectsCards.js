import Project from './Project'
import axios from 'axios';

import { useEffect, useState } from 'react';


function PersenalProjectsCards(props){
	
	const [projectCards, setProjectCards] = useState([])

    useEffect(() => {
    		// console.log(props)
    		axios.get('http://localhost:8000/user_project/')
    		.then((response) => setProjectCards(response.data))
			});

	return (
		<>
		<h1>ProjectsCards</h1>
		<p>{projectCards.map((project, i) =>  {
			return <Project key={i} name={project.name} photo={project.photo} index={i}/>

		} )}</p>
		</>
	);
}

export default PersenalProjectsCards;
