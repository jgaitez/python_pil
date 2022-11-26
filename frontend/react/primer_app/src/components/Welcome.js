// DEPENDENCIAS
import React from "react";

// LOGICA
function formatName(user){
    return user.firstName + " " + user.lastName;
}

const user = {
    firstName: "Harper",
    lastName: "Perez"
};

const element = (
    
    <h1>
    Hello, {formatName(user)}!
    </h1>

)

// RENDER
 function Welcome(){

    return (
        <div>
            Hola, desde Welcome {element}
            Como estás {user.firstName}?
        </div>
    )

}

// SALIDA
export default Welcome