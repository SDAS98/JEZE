import AsyncStorage from '@react-native-async-storage/async-storage';
import { apiClient } from './api';
import { announceForAccessibility } from '../accessibility/voiceOverAdapter';

const TOKEN_KEY = '@jeze_jwt_token';

export const loginUser = async (email, password) => {
  try {
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);

    const response = await apiClient.post('/auth/login', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });

    const { access_token } = response.data;
    await AsyncStorage.setItem(TOKEN_KEY, access_token);
    
    // Configurar header por defecto en Axios
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
    announceForAccessibility("Sesión iniciada con éxito");
    return true;
  } catch (error) {
    announceForAccessibility("Error al iniciar sesión. Verifique sus credenciales.");
    throw error;
  }
};

export const logoutUser = async () => {
  await AsyncStorage.removeItem(TOKEN_KEY);
  delete apiClient.defaults.headers.common['Authorization'];
  announceForAccessibility("Sesión cerrada");
};

export const loadStoredToken = async () => {
  const token = await AsyncStorage.getItem(TOKEN_KEY);
  if (token) {
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    return token;
  }
  return null;
};