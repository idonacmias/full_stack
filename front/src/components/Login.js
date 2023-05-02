import React, { useState } from 'react';

import axios from 'axios'; //{isCancel, AxiosError}

import serverBaseUrl from '../setting'



function Login() {

  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
		console.log('handleSubmit')
        e.preventDefault()
        axios.post('https://woodworksite.onrender.com/token/', {username: name, password : password})
        .then((response) => localStorage.setItem('access',response.data.access)) 
        .catch(() => localStorage.setItem('access', ''))
        } 


  const handelResponse = (response) =>{ 
        
        console.log('localStorage:', localStorage.getItem('access'))

      }
	return (
		<form onSubmit={handleSubmit}>
			Name:
			<input type="text" value={name} onChange={(event) => setName(event.target.value)} />
       <br/>
         Password:
         <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
       <br/>

			<button type="submit">Submit</button>
 		</form>

 		);
}


export default Login










//   const [name, setName] = useState('');
//   const [password, setPassword] = useState('');
//   const [rank, setRank] = useState('student')

//   const handleSubmit = (event) => {
//     console.log('Name:', name, 'Password:', password);
//     axios.post(serverBaseUrl + '/' + 'student' + '/',
// 			// baseURL: serverBXaseUrl + '/' + 'student' + '/',
// 			// method: 'POST',
// 			// JSON.stringify({name : name, password : password}),
// 			// headers: {"X-CSRFToken": csrfToken},

//  	// 		// headers: {
//     // 		// 		"Access-Control-Allow-Origin": "*",
//     // 		// 		"Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
// 	// 		// 		}

//     	{name:name, password:password})
//   	// // axios.request({
// 	// 	baseURL: serverBaseUrl + '/' + 'test/',
// 	// 	methode: 'GET',
// 	// 	})
//   };

//   const handleChackbox = event => {
//     console.log(event)
//     if (event.target.checked) {
//       console.log('✅ Checkbox is checked');
//     } else {
//       console.log('⛔️ Checkbox is NOT checked');
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <label>
//         Name:
//         <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
//       </label>
//       <br/>
//       <label>
//         Password:
//         <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
//       </label>
//       <br/>
//       teacher<input type="checkbox" onChange={() => handleChackbox()} />
//       <br/>
//       <button type="submit">Submit</button>
//     </form>
//   );
// }













// function Login(props){

// 	return (
// 		<form onSabmit={this}>

//   			<label>
// 			Name:
// 			    <input type="text" name="name" />
//   			</label>

// 			<label>
// 			Password:
// 			    <input type="text" name="password" />
//   			</label>
			
// 			<input type="submit" value="Submit" />
		
// 		</form>
// 	);
// }

// export default Login;
