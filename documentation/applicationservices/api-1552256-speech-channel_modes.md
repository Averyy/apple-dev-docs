# Speech-Channel Modes

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

The available text-processing and number-processing modes for a speech channel.

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : OSType {
    ...
};
```

## Topics

### Constants
- [modeText](./api-1552256-speech-channel_modes/modetext.md)
  Used with [`soInputMode`](./api-1552228-speech-channel_information_constants/soinputmode.md) to indicate that the speech channel is in text-processing mode.
- [modePhonemes](./api-1552256-speech-channel_modes/modephonemes.md)
  Used with [`soInputMode`](./api-1552228-speech-channel_information_constants/soinputmode.md) to indicate that the speech channel is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
- [modeNormal](./api-1552256-speech-channel_modes/modenormal.md)
  When the speech channel is in text-processing mode, indicates that the synthesizer should process characters as expected and assemble digits into numbers. Use this value with [`soCharacterMode`](./api-1552228-speech-channel_information_constants/socharactermode.md) and [`soNumberMode`](./api-1552228-speech-channel_information_constants/sonumbermode.md).
- [modeLiteral](./api-1552256-speech-channel_modes/modeliteral.md)
  When the speech channel is in text-processing mode, indicates that characters and digits are spoken literally (for example, “cat” is spoken as “C-A-T” and “12” is spoken as "one, two"). Use this value with [`soCharacterMode`](./api-1552228-speech-channel_information_constants/socharactermode.md) and [`soNumberMode`](./api-1552228-speech-channel_information_constants/sonumbermode.md).
- [modeTune](./api-1552256-speech-channel_modes/modetune.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552256-speech-channel_modes)*