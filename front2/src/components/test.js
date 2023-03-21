import { useEffect, useState } from 'react';
import axios from 'axios';


function Test() {
    const SERVER_URL = "http://localhost:8000/test"
    const [fname, setfname] = useState("")
    const [email, setemail] = useState("")
    const [students, setstudents] = useState([])


    useEffect(() => {
        console.log("call the server")
        show()
    }, [])


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




    return (
        <div className="Test">


            Number of students:{students.length}<hr></hr>
            {students.map((stud, ind) => <div key={ind}>
                Fname: {stud.fname} {", "}
                Email:{stud.email}
                <button onClick={() => data_delete( stud.id )}>Delete</button>
                <button onClick={() => upd( stud.id )}>Update</button>
            </div>)}
            <hr></hr>
            Email:<input onChange={(e) => setemail(e.target.value)} />
            Name:<input onChange={(e) => setfname(e.target.value)} />
            <button onClick={() => add2Server()}>Add</button>
        </div>
    );
}


export default Test;
