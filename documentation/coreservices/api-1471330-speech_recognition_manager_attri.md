# Speech Recognition Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Speech Recognition Manager.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltSpeechRecognitionAttr](./api-1471330-speech_recognition_manager_attri/gestaltspeechrecognitionattr.md)
  The selector which you pass to the `Gestalt` function to determine the Speech Recognition Manager attributes.
- [gestaltDesktopSpeechRecognition](./api-1471330-speech_recognition_manager_attri/gestaltdesktopspeechrecognition.md)
  If this bit is set, the Speech Recognition Manager supports the desktop microphone.
- [gestaltTelephoneSpeechRecognition](./api-1471330-speech_recognition_manager_attri/gestalttelephonespeechrecognition.md)
  If this bit is set, the Speech Recognition Manager supports telephone input. In versions 1.5 and earlier, this bit is always 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471330-speech_recognition_manager_attri)*