# Speech-Channel Information Constants

**Framework**: Application Services

Selectors that can be passed to the `GetSpeechInfo` or `SetSpeechInfo` functions.

#### Overview

See the [`GetSpeechInfo`](1552220-getspeechinfo.md) and [`SetSpeechInfo`](1552223-setspeechinfo.md) functions. 

## Topics

### Constants
- [var soStatus: OSType](sostatus.md)
- [var soErrors: OSType](soerrors.md)
- [var soInputMode: OSType](soinputmode.md)
- [var soCharacterMode: OSType](socharactermode.md)
- [var soNumberMode: OSType](sonumbermode.md)
- [var soRate: OSType](sorate.md)
- [var soPitchBase: OSType](sopitchbase.md)
- [var soPitchMod: OSType](sopitchmod.md)
- [var soVolume: OSType](sovolume.md)
- [var soSynthType: OSType](sosynthtype.md)
- [var soRecentSync: OSType](sorecentsync.md)
- [var soPhonemeSymbols: OSType](sophonemesymbols.md)
- [var soCurrentVoice: OSType](socurrentvoice.md)
- [var soCommandDelimiter: OSType](socommanddelimiter.md)
- [var soReset: OSType](soreset.md)
- [var soCurrentA5: OSType](socurrenta5.md)
- [var soRefCon: OSType](sorefcon.md)
- [var soTextDoneCallBack: OSType](sotextdonecallback.md)
- [var soSpeechDoneCallBack: OSType](sospeechdonecallback.md)
- [var soSyncCallBack: OSType](sosynccallback.md)
- [var soErrorCallBack: OSType](soerrorcallback.md)
- [var soPhonemeCallBack: OSType](sophonemecallback.md)
- [var soWordCallBack: OSType](sowordcallback.md)
- [var soSynthExtension: OSType](sosynthextension.md)
- [var soSoundOutput: OSType](sosoundoutput.md)
  Get or set the speech channel’s current outputchannel.
- [var soOutputToFileWithCFURL: OSType](sooutputtofilewithcfurl.md)
  Pass a `CFURLRef` in the `speechInfo` parameter to write to this file, or `NULL` to generate sound.
- [var soOutputToExtAudioFile: OSType](sooutputtoextaudiofile.md)
  Pass an [`ExtAudioFileRef`](https://developer.apple.com/documentation/audiotoolbox/extaudiofileref) in the `speechInfo` parameter to write to this file, or `NULL` to generate sound.
- [var soPhonemeOptions: OSType](sophonemeoptions.md)
  Get or set options for the generation of phonetic output. See [`Phoneme Generation Options`](speech_synthesis_manager/1552233-phoneme_generation_options.md) for a complete list of options.
- [var soOutputToAudioDevice: OSType](sooutputtoaudiodevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager/1552228-speech-channel_information_constants)*