import { AccessibilityInfo, Platform } from 'react-native';

export const announceForAccessibility = (message) => {
  if (Platform.OS === 'ios' || Platform.OS === 'android') {
    AccessibilityInfo.announceForAccessibility(message);
  }
};