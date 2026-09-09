import React from 'react';
import { View, TouchableOpacity, Text, StyleSheet } from 'react-native';
import * as Haptics from 'expo-haptics';
import { announceForAccessibility } from '../accessibility/voiceOverAdapter';

const SPEEDS = [1.0, 1.25, 1.5, 2.0, 2.5, 3.0];

export const SpeedSelector = ({ currentSpeed, onSpeedChange }) => {
  const handlePress = (speed) => {
    Haptics.selectionAsync();
    announceForAccessibility(`Velocidad cambiada a ${speed} equis`);
    onSpeedChange(speed);
  };

  return (
    <View 
      style={styles.container} 
      accessible={true} 
      accessibilityLabel="Selector de velocidad de reproducción"
    >
      {SPEEDS.map((speed) => {
        const isSelected = currentSpeed === speed;
        return (
          <TouchableOpacity
            key={speed}
            style={[styles.button, isSelected && styles.selectedButton]}
            onPress={() => handlePress(speed)}
            accessible={true}
            accessibilityRole="button"
            accessibilityState={{ selected: isSelected }}
            accessibilityLabel={`Velocidad ${speed} equis`}
          >
            <Text style={[styles.text, isSelected && styles.selectedText]}>
              {speed}x
            </Text>
          </TouchableOpacity>
        );
      })}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flexDirection: 'row', justifyContent: 'space-around', marginVertical: 10 },
  button: { padding: 10, borderRadius: 8, backgroundColor: '#E2E8F0', minWidth: 48, alignItems: 'center' },
  selectedButton: { backgroundColor: '#2B6CB0' },
  text: { fontSize: 16, fontWeight: 'bold', color: '#2D3748' },
  selectedText: { color: '#FFFFFF' },
});