import { render } from "@testing-library/react";
import React, {useState, useEffect} from "react";
import * as HeroesServer from "./HeroesServer";

const Heroe = () => {
    // ESTADOS

    // HOOK useState
    const initialState = {
        id: 0,
        nombre: "",
        edad: 0,
        universo: 0
    };
    const [heroe, setHeroe] = useState({initialState});

    // FUNCION PARA OBTENER NUESTRO HEROE
    const getHeroe = async ()=>{
        try{
            const res = await HeroesServer.getHeroe();
            const data = await res.json();
            const {id, nombre, edad, universo} = data.heroe;
            setHeroe({id, nombre, edad, universo});
        } catch(error){
            console.log(error)

        }
    }
    const handleInputChange = (e) => {
        
        setHeroe({...heroe,[e.target.name]: e.target.value})

    }
    
    // EFECTO
    useEffect(()=>{},[]);

    // RENDER o HTML o RETURN
    
    render(
        <div>
            <div className = "col-md-3 mx-auto">
                <h2 className="mb-3 text-center">Heroe</h2>
                <form>
                    <div className="mb-3">
                        <label className="form-label">Nombre Heroe</label>
                        <input type="text" name= "nombre" id= "nombre" value = {heroe.nombre} onChange={handleInputChange}>
                        </input>
                        <label className="form-label">Edad</label>
                        <input type="number" name= "edad" id= "edad" value = {heroe.edad} onChange={handleInputChange}>
                        </input>
                    </div>
                </form>
            </div>
        </div>
    );
};
export default Heroe;