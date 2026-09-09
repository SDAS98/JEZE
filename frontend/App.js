import React, { useState, useEffect } from 'react';
import { SafeAreaView, FlatList, StyleSheet, Text, View, ActivityIndicator } from 'react-native';
import { AudioRecorder } from './src/components/AudioRecorder';
import { AudioCard } from './src/components/AudioCard';
import { uploadAudioPost, fetchAudioFeed } from './src/services/api';
import { loadStoredToken } from './src/services/auth';
import { announceForAccessibility } from './src/accessibility/voiceOverAdapter';

export default function App() {
  const [loading, setLoading] = useState(true);
  const [feed, setFeed] = useState([]);

  useEffect(() => {
    async function init() {
      await loadStoredToken();
      await loadFeed();
      setLoading(false);
    }
    init();
  }, []);

  const loadFeed = async () => {
    try {
      const data = await fetchAudioFeed();
      setFeed(data);
    } catch (error) {
      console.log("Servidor no disponible o modo offline");
    }
  };

  const handleRecordingComplete = async (fileUri) => {
    try {
      announceForAccessibility("Subiendo nota de voz...");
      await uploadAudioPost(fileUri, 5.0);
      announceForAccessibility("Nota de voz enviada correctamente.");
      await loadFeed();
    } catch (error) {
      announceForAccessibility("Error al enviar la nota de voz.");
    }
  };

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#1A365D" />
        <Text accessibilityLiveRegion="polite">Cargando JEZE...</Text>
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.headerTitle} accessibilityRole="header">
        JEZE - Red Social Accesible
      </Text>
      
      <AudioRecorder onRecordingComplete={handleRecordingComplete} />

      <FlatList
        data={feed}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => <AudioCard audioItem={item} />}
        contentContainerStyle={styles.listContainer}
        ListEmptyComponent={
          <Text style={styles.emptyText} accessibilityRole="text">
            No hay publicaciones de audio aún. ¡Sé el primero en grabar una!
          </Text>
        }
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F7FAFC', paddingTop: 40 },
  center: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  headerTitle: { fontSize: 24, fontWeight: 'bold', textAlign: 'center', marginVertical: 10, color: '#1A365D' },
  listContainer: { paddingHorizontal: 16, paddingBottom: 20 },
  emptyText: { textAlign: 'center', color: '#718096', marginTop: 40, fontSize: 16 }
});