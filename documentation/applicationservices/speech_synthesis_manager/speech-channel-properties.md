# Speech-Channel Properties

**Framework**: Application Services

Properties used with [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) or [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) to get or set the characteristics of a speech channel.

## Topics

### Constants
- [let kSpeechStatusProperty: CFString](kspeechstatusproperty.md)
  Get speech-status information for the speech channel.
- [let kSpeechErrorsProperty: CFString](kspeecherrorsproperty.md)
  Get speech-error information for the speech channel. 
- [let kSpeechInputModeProperty: CFString](kspeechinputmodeproperty.md)
  Get or set the speech channel’s current text-processing mode. 
- [let kSpeechCharacterModeProperty: CFString](kspeechcharactermodeproperty.md)
  Get or set the speech channel’s current character-processing mode.
- [let kSpeechNumberModeProperty: CFString](kspeechnumbermodeproperty.md)
  Get or set the speech channel’s current number-processing mode.
- [let kSpeechRateProperty: CFString](kspeechrateproperty.md)
  Get or set a speech channel’s speech rate.
- [let kSpeechPitchBaseProperty: CFString](kspeechpitchbaseproperty.md)
  Get or set the speech channel’s baseline speech pitch.
- [let kSpeechPitchModProperty: CFString](kspeechpitchmodproperty.md)
  Get or set a speech channel’s pitch modulation.
- [let kSpeechVolumeProperty: CFString](kspeechvolumeproperty.md)
  Get or set the speech volume for a speech channel.
- [let kSpeechSynthesizerInfoProperty: CFString](kspeechsynthesizerinfoproperty.md)
  Get information about the speech synthesizer being used on the specified speech channel.
- [let kSpeechRecentSyncProperty: CFString](kspeechrecentsyncproperty.md)
  Get the message code for the most recently encountered synchronization command.
- [let kSpeechPhonemeSymbolsProperty: CFString](kspeechphonemesymbolsproperty.md)
  Get a list of phoneme symbols and example words defined for the speech channel’s synthesizer.
- [let kSpeechCurrentVoiceProperty: CFString](kspeechcurrentvoiceproperty.md)
  Set the current voice on the current speech channel to the specified voice.
- [let kSpeechCommandDelimiterProperty: CFString](kspeechcommanddelimiterproperty.md)
  Set the embedded speech command delimiter characters to be used for the speech channel.
- [let kSpeechResetProperty: CFString](kspeechresetproperty.md)
  Set a speech channel back to its default state.
- [let kSpeechOutputToFileURLProperty: CFString](kspeechoutputtofileurlproperty.md)
  Set the speech output destination to a file or to the computer’s speakers.
- [let kSpeechOutputToExtAudioFileProperty: CFString](kspeechoutputtoextaudiofileproperty.md)
  Set the speech output destination to an extended audio file or to the computer’s speakers.
- [let kSpeechRefConProperty: CFString](kspeechrefconproperty.md)
  Set a speech channel’s reference constant value.
- [let kSpeechTextDoneCallBack: CFString](kspeechtextdonecallback.md)
  Set the callback function to be called when the Speech Synthesis Manager has finished processing speech being generated on the speech channel.
- [let kSpeechSpeechDoneCallBack: CFString](kspeechspeechdonecallback.md)
  Set the callback function to be called when the Speech Synthesis Manager has finished generating speech on the speech channel.
- [let kSpeechSyncCallBack: CFString](kspeechsynccallback.md)
  Set the callback function to be called when the Speech Synthesis Manager encounters a synchronization command within an embedded speech command in text being processed on the speech channel. 
- [let kSpeechPhonemeCallBack: CFString](kspeechphonemecallback.md)
  Set the callback function to be called every time the Speech Synthesis Manager is about to generate a phoneme on the speech channel.
- [let kSpeechErrorCFCallBack: CFString](kspeecherrorcfcallback.md)
  Set the callback function to be called when an error is encountered during the processing of an embedded command.
- [let kSpeechWordCFCallBack: CFString](kspeechwordcfcallback.md)
  Set the callback function to be called every time the Speech Synthesis Manager is about to generate a word on the speech channel.
- [let kSpeechPhonemeOptionsProperty: CFString](kspeechphonemeoptionsproperty.md)
  Get or set the options for the generation of phonetic output.
- [let kSpeechOutputToAudioDeviceProperty: CFString](kspeechoutputtoaudiodeviceproperty.md)
  Set the speech output destination to an audio device file or to the computer’s speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager/speech-channel_properties)*