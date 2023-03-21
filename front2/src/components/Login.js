import React, { useState } from 'react';

import axios from 'axios'; //{isCancel, AxiosError}

import serverBaseUrl from '../setting'



function Login() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [rank, setRank] = useState('student')

  const testLog = (event) => {
    console.log('Name:');
	
	};
  const handleSubmit = (event) => {
    console.log('Name:', name, 'Password:', password);
    axios({
			baseURL: serverBaseUrl + '/' + 'test' + '/',
			// baseURL: serverBXaseUrl + '/' + 'student' + '/',
			method: 'GET',
			body: JSON.stringify({name : name, password : password}),
			// headers: {"X-CSRFToken": csrfToken},

 	// 		// headers: {
    // 		// 		"Access-Control-Allow-Origin": "*",
    // 		// 		"Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
	// 		// 		}

    	})
  	// // axios.request({
	// 	baseURL: serverBaseUrl + '/' + 'test/',
	// 	methode: 'GET',
	// 	})
  };

  const handleChackbox = event => {
    console.log(event)
    if (event.target.checked) {
      console.log('✅ Checkbox is checked');
    } else {
      console.log('⛔️ Checkbox is NOT checked');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
      </label>
      <br/>
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br/>
      teacher<input type="checkbox" onChange={() => handleChackbox()} />
      <br/>
      <button type="submit">Submit</button>
    </form>
  );
}

export default Login












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
