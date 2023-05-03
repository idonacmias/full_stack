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








