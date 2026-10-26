# Speech-Channel Information Constants

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Selectors that can be passed to the `GetSpeechInfo` or `SetSpeechInfo` functions.

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
- [soStatus](./api-1552228-speech-channel_information_constants/sostatus.md)
- [soErrors](./api-1552228-speech-channel_information_constants/soerrors.md)
- [soInputMode](./api-1552228-speech-channel_information_constants/soinputmode.md)
- [soCharacterMode](./api-1552228-speech-channel_information_constants/socharactermode.md)
- [soNumberMode](./api-1552228-speech-channel_information_constants/sonumbermode.md)
- [soRate](./api-1552228-speech-channel_information_constants/sorate.md)
- [soPitchBase](./api-1552228-speech-channel_information_constants/sopitchbase.md)
- [soPitchMod](./api-1552228-speech-channel_information_constants/sopitchmod.md)
- [soVolume](./api-1552228-speech-channel_information_constants/sovolume.md)
- [soSynthType](./api-1552228-speech-channel_information_constants/sosynthtype.md)
- [soRecentSync](./api-1552228-speech-channel_information_constants/sorecentsync.md)
- [soPhonemeSymbols](./api-1552228-speech-channel_information_constants/sophonemesymbols.md)
- [soCurrentVoice](./api-1552228-speech-channel_information_constants/socurrentvoice.md)
- [soCommandDelimiter](./api-1552228-speech-channel_information_constants/socommanddelimiter.md)
- [soReset](./api-1552228-speech-channel_information_constants/soreset.md)
- [soCurrentA5](./api-1552228-speech-channel_information_constants/socurrenta5.md)
- [soRefCon](./api-1552228-speech-channel_information_constants/sorefcon.md)
- [soTextDoneCallBack](./api-1552228-speech-channel_information_constants/sotextdonecallback.md)
- [soSpeechDoneCallBack](./api-1552228-speech-channel_information_constants/sospeechdonecallback.md)
- [soSyncCallBack](./api-1552228-speech-channel_information_constants/sosynccallback.md)
- [soErrorCallBack](./api-1552228-speech-channel_information_constants/soerrorcallback.md)
- [soPhonemeCallBack](./api-1552228-speech-channel_information_constants/sophonemecallback.md)
- [soWordCallBack](./api-1552228-speech-channel_information_constants/sowordcallback.md)
- [soSynthExtension](./api-1552228-speech-channel_information_constants/sosynthextension.md)
- [soSoundOutput](./api-1552228-speech-channel_information_constants/sosoundoutput.md)
  Get or set the speech channel’s current outputchannel.
- [soOutputToFileWithCFURL](./api-1552228-speech-channel_information_constants/sooutputtofilewithcfurl.md)
  Pass a `CFURLRef` in the `speechInfo` parameter to write to this file, or `NULL` to generate sound.
- [soOutputToExtAudioFile](./api-1552228-speech-channel_information_constants/sooutputtoextaudiofile.md)
  Pass an [`ExtAudioFileRef`](../AudioToolbox/extaudiofileref.md) in the `speechInfo` parameter to write to this file, or `NULL` to generate sound.
- [soPhonemeOptions](./api-1552228-speech-channel_information_constants/sophonemeoptions.md)
  Get or set options for the generation of phonetic output. See [Phoneme Generation Options](./api-1552233-phoneme_generation_options.md) for a complete list of options.
- [soOutputToAudioDevice](./api-1552228-speech-channel_information_constants/sooutputtoaudiodevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants)*