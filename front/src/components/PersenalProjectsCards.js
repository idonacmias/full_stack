import Project from './Project'
import axios from 'axios';

import { useEffect, useState } from 'react';


function PersenalProjectsCards(props){
	
	const [projectCards, setProjectCards] = useState([])
	const config = {headers:{Authorization:`Bearer ${localStorage.getItem('access')}`}}

    useEffect(() => {
			console.log('card:', projectCards)

    		// console.log(props)
    		axios.get('http://localhost:8000/project/10', config)
    		.then((response) => setProjectCards(response.data))
			});

	return (
		<>
		<h1>ProjectsCards</h1>
		<p>{projectCards.map((project, i) =>  {
			return <Project key={i} name={project.name} photo={project.image} index={i}/>

		} )}</p>
		</>
	);
}

export default PersenalProjectsCards;
