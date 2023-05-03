import { useEffect, useState } from 'react';
import axios from 'axios';


function Test() {
    const SERVER_URL = "https://woodworksite.onrender.com/test"
    const [fname, setfname] = useState("")
    const [email, setemail] = useState("")
    const [students, setstudents] = useState([])
    const [fnameUpToDate, setFnameUpToDate] = useState("")


    const add2Server = () => {
        const student = { fname: fname, email: email };
        axios.post(SERVER_URL, student)
        show()
    }


    const show = () => {
        axios.get(SERVER_URL).then(response => setstudents(response.data));
    }
    const data_delete = (id) => {
        axios.delete(`${SERVER_URL}/${id}`)
        show()
    }
    const upd = (id) => {
        const student = { fname: fname, email: email };
        console.log(id)
        axios.put(`${SERVER_URL}/${id}`, student)
      .then((response) => { console.log(response.data); });
      show()
    }



    const getMyDict = () => {
        console.log('getMyDict')
        axios.get('https://woodworksite.onrender.com/test/')
        .then((response) => console.log(response.data));
    }

    const postMyDict = () => {
        console.log('postMyDict')
        axios.post('https://woodworksite.onrender.com/test/', {name: 'bob'})
        .then((response) => console.log(response.data));

    }

    const handleSubmit = (e) => {
        console.log('handleSubmit')
        console.log('fname', fname)
        axios.post('https://woodworksite.onrender.com/test/', {name: fname})
        .then((response) => setFnameUpToDate(response.data.name))
        e.preventDefault()


    }

    return (
       <div>
            <button onClick={() => getMyDict()}>getMyDict</button>
            <button onClick={() => postMyDict()}>postMyDict</button>

             <form onSubmit={handleSubmit}>
                 Name:<input onChange={(e) => setfname(e.target.value)} />
                <button type="submit">Submit</button>

             </form>
            <h1>{fnameUpToDate}</h1>
       </div>

    );
}


export default Test;
