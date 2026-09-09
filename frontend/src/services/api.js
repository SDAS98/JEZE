import axios from 'axios';
import { Platform } from 'react-native';

// En emulador Android se usa 10.0.2.2; en iOS o dispositivo físico usar la IP local de tu PC
const BASE_URL = Platform.OS === 'android' 
  ? 'http://10.0.2.2:8000/api/v1' 
  : 'http://localhost:8000/api/v1';

export const apiClient = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const uploadAudioPost = async (fileUri, durationSeconds) => {
  const formData = new FormData();
  
  formData.append('file', {
    uri: fileUri,
    type: 'audio/m4a',
    name: 'voice_note.m4a',
  });
  formData.append('duration_seconds', durationSeconds.toString());
  formData.append('format', 'opus');

  const response = await apiClient.post('/audio/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const fetchAudioFeed = async () => {
  const response = await apiClient.get('/audio/feed');
  return response.data;
};