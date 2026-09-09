import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import * as Haptics from 'expo-haptics';
import { announceForAccessibility } from '../../../../client/src/accessibility/voiceOverAdapter';

export const AudioRecorder = ({ onRecordingComplete }) => {
  const [recording, setRecording] = useState(null);
  const [isRecording, setIsRecording] = useState(false);

  async function startRecording() {
    try {
      await Audio.requestPermissionsAsync();
      await Audio.setAudioModeAsync({
        allowsRecordingIOS: true,
        playsInSilentModeIOS: true,
      });

      // Vibración háptica de confirmación
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      announceForAccessibility("Grabación iniciada. Presiona de nuevo para detener.");

      const { recording } = await Audio.Recording.createAsync(
        Audio.RecordingOptionsPresets.HIGH_QUALITY
      );
      setRecording(recording);
      setIsRecording(true);
    } catch (err) {
      announceForAccessibility("Error al iniciar la grabación");
    }
  }

  async function stopRecording() {
    setIsRecording(false);
    await recording.stopAndUnloadAsync();
    const uri = recording.getURI();
    
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
    announceForAccessibility("Grabación finalizada. Subiendo nota de voz.");

    if (onRecordingComplete) {
      onRecordingComplete(uri);
    }
  }

  return (
    <View style={styles.container}>
      <TouchableOpacity
        accessible={true}
        accessibilityLabel={isRecording ? "Detener grabación de audio" : "Grabar nueva nota de voz"}
        accessibilityHint="Doble toque para activar o detener el micrófono"
        accessibilityRole="button"
        style={[styles.button, isRecording && styles.recordingButton]}
        onPress={isRecording ? stopRecording : startRecording}
      >
        <Text style={styles.buttonText}>
          {isRecording ? "■ Detener Grabación" : "🎙️ Grabar Nota de Voz"}
        </Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { padding: 20, alignItems: 'center' },
  button: {
    minWidth: 200,
    minHeight: 60, // Cumple requerimiento A11y > 48dp
    backgroundColor: '#1A365D',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 30,
  },
  recordingButton: { backgroundColor: '#C53030' },
  buttonText: { color: '#FFFFFF', fontSize: 18, fontWeight: 'bold' }
});