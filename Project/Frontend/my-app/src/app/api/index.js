import axios from "axios";

export const get = async (endpoint, params) => {
  try {
    const response = await axios.get(endpoint, { params });
    return response.data;
  } catch (error) {
    throw error; // Rechazar la promesa con el error
  }
};

export const post = async (endpoint, data) => {
  try {
    const response = await axios.post(endpoint, data);
    return response;
  } catch (error) {
    throw error; // Re-lanza el error para manejarlo en el componente
  }
};
