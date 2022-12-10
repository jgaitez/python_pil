// CONEXION A API
const API_URL = "http://localhost:8000/user/user";

export const getHeroe = async () => {
        return await fetch(API_URL);
}

export const traerHeroe = [
    {
    id: 1,
    nombre: "Batman",
    edad: 45,
    universo: 2
    }
];

export const updateHeroe = async () => {
    return await fetch(API_URL);
}

export const listHeroe = async () => {
    return await fetch(API_URL);
}

export const deleteHeroe = async () => {
    return await fetch(API_URL);
}

export const createHeroe = async () => {
    return await fetch(API_URL);
}