# Speech-Channel Modes for Core Foundation-based Functions

**Framework**: Application Services

The available text-processing and number-processing modes for a speech channel.

## Topics

### Constants
- [let kSpeechModeText: CFString](kspeechmodetext.md)
  Used with [`kSpeechInputModeProperty`](kspeechinputmodeproperty.md) to indicate that the speech channel is in text-processing mode.
- [let kSpeechModePhoneme: CFString](kspeechmodephoneme.md)
  Used with [`kSpeechInputModeProperty`](kspeechinputmodeproperty.md) to indicate that the speech channel is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
- [let kSpeechModeNormal: CFString](kspeechmodenormal.md)
  When the speech channel is in text-processing mode, indicates that the synthesizer should process characters as expected and assemble digits into numbers. Use this value with [`kSpeechCharacterModeProperty`](kspeechcharactermodeproperty.md) and [`kSpeechNumberModeProperty`](kspeechnumbermodeproperty.md).
- [let kSpeechModeLiteral: CFString](kspeechmodeliteral.md)
  When the speech channel is in text-processing mode, indicates that characters and digits are spoken literally (for example, “cat” is spoken as “C-A-T” and “12” is spoken as "one, two"). Use this value with [`kSpeechCharacterModeProperty`](kspeechcharactermodeproperty.md) and [`kSpeechNumberModeProperty`](kspeechnumbermodeproperty.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager/speech-channel_modes_for_core_foundation-based_functions)*