
function Project(props){
	return (
		<>

		<h1>Project card {props.index}</h1>
		<a href	='https://google.com'>
			<h1>{props.name}</h1>
        	<img src={process.env.PUBLIC_URL + props.photo} alt="My Photo" />
		</a>
		<br/>		

		</>
	);
}

export default Project;
