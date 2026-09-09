import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import { announceForAccessibility } from '../../../../client/src/accessibility/voiceOverAdapter';

export const AudioCard = ({ audioItem }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [sound, setSound] = useState(null);
  const [rate, setRate] = useState(1.0);

  async function togglePlay() {
    if (sound) {
      if (isPlaying) {
        await sound.pauseAsync();
        setIsPlaying(false);
        announceForAccessibility("Audio pausado");
      } else {
        await sound.playAsync();
        setIsPlaying(true);
        announceForAccessibility(`Reproduciendo audio a velocidad ${rate}x`);
      }
    } else {
      const { sound: newSound } = await Audio.Sound.createAsync(
        { uri: audioItem.file_url },
        { shouldPlay: true, rate: rate }
      );
      setSound(newSound);
      setIsPlaying(true);
      announceForAccessibility(`Reproduciendo audio de ${audioItem.duration_seconds} segundos`);
    }
  }

  return (
    <View 
      style={styles.card}
      accessible={true}
      accessibilityLabel={`Nota de voz. Duración ${audioItem.duration_seconds} segundos. Transcripción: ${audioItem.transcript || "Procesándose"}`}
    >
      <Text style={styles.transcriptText}>
        {audioItem.transcript ? `📝 ${audioItem.transcript}` : "⏳ Transcribiendo audio..."}
      </Text>

      <TouchableOpacity
        accessible={true}
        accessibilityLabel={isPlaying ? "Pausar nota de voz" : "Reproducir nota de voz"}
        accessibilityRole="button"
        style={styles.playButton}
        onPress={togglePlay}
      >
        <Text style={styles.playText}>{isPlaying ? "⏸️ Pausar" : "▶️ Reproducir"}</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  card: { padding: 16, marginVertical: 8, backgroundColor: '#EDF2F7', borderRadius: 12 },
  transcriptText: { fontSize: 16, color: '#2D3748', marginBottom: 10 },
  playButton: { minHeight: 48, backgroundColor: '#2B6CB0', justifyContent: 'center', alignItems: 'center', borderRadius: 8 },
  playText: { color: '#FFF', fontSize: 16, fontWeight: '600' }
});