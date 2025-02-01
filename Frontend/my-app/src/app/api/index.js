import axios from "axios";

export const get = async (endpoint, params) => {
  try {
    const response = await axios.get(endpoint, { params });
    return response.data;
  } catch (error) {
    throw error; // Rechazar la promesa con el error
  }
};
