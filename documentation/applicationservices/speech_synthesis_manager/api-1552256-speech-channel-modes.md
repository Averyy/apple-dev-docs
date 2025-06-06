# Speech-Channel Modes

**Framework**: Application Services

The available text-processing and number-processing modes for a speech channel.

## Topics

### Constants
- [var modeText: OSType](modetext.md)
  Used with [`soInputMode`](soinputmode.md) to indicate that the speech channel is in text-processing mode.
- [var modePhonemes: OSType](modephonemes.md)
  Used with [`soInputMode`](soinputmode.md) to indicate that the speech channel is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
- [var modeNormal: OSType](modenormal.md)
  When the speech channel is in text-processing mode, indicates that the synthesizer should process characters as expected and assemble digits into numbers. Use this value with [`soCharacterMode`](socharactermode.md) and [`soNumberMode`](sonumbermode.md).
- [var modeLiteral: OSType](modeliteral.md)
  When the speech channel is in text-processing mode, indicates that characters and digits are spoken literally (for example, “cat” is spoken as “C-A-T” and “12” is spoken as "one, two"). Use this value with [`soCharacterMode`](socharactermode.md) and [`soNumberMode`](sonumbermode.md).
- [var modeTune: OSType](modetune.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager/1552256-speech-channel_modes)*