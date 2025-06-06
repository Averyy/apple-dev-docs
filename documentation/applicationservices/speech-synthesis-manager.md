# Speech Synthesis Manager

**Framework**: Application Services

#### Overview

The Speech Synthesis Manager, formerly called the Speech Manager, is the part of macOS that provides a standardized method for Mac apps to generate synthesized speech. For example, you may want your application to incorporate the capability to speak its dialog box messages to the user. A word-processing application might use the Speech Synthesis Manager to implement a command that speaks a selected section of a document to the user. Because sound samples can take up large amounts of room on disk, using text in place of sampled sound is extremely efficient. For example, a multimedia application might use the Speech Synthesis Manager to provide a narration of a QuickTime movie instead of including sampled-sound data on a movie track.

OS X v10.5 introduces native support for performing speech synthesis tasks using Core Foundation-based objects, such as speaking text represented as `CFString` objects and managing speech channel properties using a `CFDictionary`-based property dictionary. You should begin using these Core Foundation-based programming interfaces as soon as it’s convenient, because future synthesizers will accept Core Foundation strings and data structures directly through the speech synthesis framework. In the meantime, existing buffer-based clients and synthesizers will continue to work as before, with strings and other data structures getting automatically converted as necessary.

##### 1679841

You can check for version and feature availability information by using the Speech Synthesis Manager selectors defined in the [`Gestalt Manager`](https://developer.apple.com/documentation/coreservices/carbon_core/gestalt_manager).

## Topics

### Changing Speech Attributes
- [func SetSpeechProperty(SpeechChannel, CFString, CFTypeRef?) -> OSErr](1459256-setspeechproperty.md)
  Sets the value of the specified speech-channel property.
- [func SetSpeechPitch(SpeechChannel, Fixed) -> OSErr](1462674-setspeechpitch.md)
  Sets the speech pitch on a designated speech channel.
- [func SetSpeechRate(SpeechChannel, Fixed) -> OSErr](1459896-setspeechrate.md)
  Sets the speech rate of a designated speech channel.
### Converting Text To Phonemes
- [func CopyPhonemesFromText(SpeechChannel, CFString, UnsafeMutablePointer<CFString?>) -> OSErr](1460918-copyphonemesfromtext.md)
  Converts the specified text string into its equivalent phonemic representation.
### Installing a Pronunciation Dictionary
- [func UseSpeechDictionary(SpeechChannel, CFDictionary) -> OSErr](1463688-usespeechdictionary.md)
  Registers a speech dictionary with a speech channel.
### Managing Speech Channels
- [func DisposeSpeechChannel(SpeechChannel) -> OSErr](1462081-disposespeechchannel.md)
  Disposes of an existing speech channel.
- [func NewSpeechChannel(UnsafeMutablePointer<VoiceSpec>?, UnsafeMutablePointer<SpeechChannel?>) -> OSErr](1461367-newspeechchannel.md)
  Creates a new speech channel.
### Obtaining Information About Speech and Speech Channels
- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusy() -> Int16](1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechBusySystemWide() -> Int16](1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [func SpeechManagerVersion() -> NumVersion](1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.
### Getting Information About Voices
- [func CountVoices(UnsafeMutablePointer<Int16>) -> OSErr](1459947-countvoices.md)
  Determines how many voices are available.
- [func GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1464595-getindvoice.md)
  Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.
- [func GetVoiceDescription(UnsafePointer<VoiceSpec>?, UnsafeMutablePointer<VoiceDescription>?, Int) -> OSErr](1463940-getvoicedescription.md)
  Gets a description of a voice by using the `GetVoiceDescription` function.
- [func GetVoiceInfo(UnsafePointer<VoiceSpec>?, OSType, UnsafeMutableRawPointer) -> OSErr](1461410-getvoiceinfo.md)
  Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 
- [func MakeVoiceSpec(OSType, OSType, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1461446-makevoicespec.md)
  Sets the fields of a voice specification structure. 
### Starting, Stopping, and Pausing Speech
- [func ContinueSpeech(SpeechChannel) -> OSErr](1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [func PauseSpeechAt(SpeechChannel, Int32) -> OSErr](1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [func SpeakCFString(SpeechChannel, CFString, CFDictionary?) -> OSErr](1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [func StopSpeech(SpeechChannel) -> OSErr](1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [func StopSpeechAt(SpeechChannel, Int32) -> OSErr](1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.
### Registering and Unregistering Synthesizers and Voices
- [func SpeechSynthesisRegisterModuleURL(CFURL) -> OSErr](1459624-speechsynthesisregistermoduleurl.md)
  Registers and makes available a speech synthesizer or voice.
- [func SpeechSynthesisUnregisterModuleURL(CFURL) -> OSErr](1462511-speechsynthesisunregistermoduleu.md)
  Unregisters a registered speech synthesizer or voice.
### Callbacks
- [typealias SpeechDoneProcPtr](speechdoneprocptr.md)
  Defines a pointer to a speech-done callback functionwhich is called when the Speech Synthesis Manager finishes speakinga buffer of text.
- [typealias SpeechErrorProcPtr](speecherrorprocptr.md)
  Defines a pointer to an error callback functionthat handles syntax errors within commands embedded in a text bufferbeing processed by the Speech Synthesis Manager.
- [typealias SpeechErrorCFProcPtr](speecherrorcfprocptr.md)
  Defines a pointer to an error callback function that handles syntax errors within commands embedded in a `CFString` object being processed by the Speech Synthesis Manager.
- [typealias SpeechPhonemeProcPtr](speechphonemeprocptr.md)
  Defines a pointer to a phoneme callback functionthat is called by the Speech Synthesis Manager before it pronouncesa phoneme.
- [typealias SpeechSyncProcPtr](speechsyncprocptr.md)
  Defines a pointer to a synchronization callbackfunction that is called when the Speech Synthesis Manager encountersa synchronization command embedded in a text buffer.
- [typealias SpeechTextDoneProcPtr](speechtextdoneprocptr.md)
  Defines a pointer to a text-done callback functionthat is called when the Speech Synthesis Manager has finished processinga buffer of text.
- [typealias SpeechWordProcPtr](speechwordprocptr.md)
  Defines a pointer to a word callback functionthat is called by the Speech Synthesis Manager before it pronouncesa word.
- [typealias SpeechWordCFProcPtr](speechwordcfprocptr.md)
  Defines a pointer to a Core Foundation-based word callback function that is called by the Speech Synthesis Manager before it pronounces a word.
### Data Types
- [struct DelimiterInfo](delimiterinfo.md)
  Defines a delimiter information structure.
- [struct PhonemeDescriptor](phonemedescriptor.md)
  Defines a phoneme descriptor structure.
- [struct PhonemeInfo](phonemeinfo.md)
  Defines a structure that stores information about a phoneme.
- [struct SpeechChannelRecord](speechchannelrecord.md)
  Represents a speech channel.
- [typealias SpeechChannel](speechchannel.md)
  Defines a pointer to a speech channel record.
- [typealias SpeechDoneUPP](speechdoneupp.md)
  Defines a universal procedure pointer (UPP) to a speech-done callback function.
- [struct SpeechErrorInfo](speecherrorinfo.md)
  Defines a speech error information structure.
- [typealias SpeechErrorUPP](speecherrorupp.md)
  Defines a universal procedure pointer (UPP) to an error callback function.
- [typealias SpeechPhonemeUPP](speechphonemeupp.md)
  Defines a universal procedure pointer (UPP) to a phoneme callback function.
- [struct SpeechStatusInfo](speechstatusinfo.md)
  Defines a speech status information structure, which stores information about the status of a speech channel.
- [typealias SpeechSyncUPP](speechsyncupp.md)
  Defines a universal procedure pointer (UPP) to a synchronization callback function.
- [typealias SpeechTextDoneUPP](speechtextdoneupp.md)
  Defines a universal procedure pointer (UPP) to a text-done callback function.
- [struct SpeechVersionInfo](speechversioninfo.md)
  Defines a speech version information structure.
- [typealias SpeechWordUPP](speechwordupp.md)
  Defines a universal procedure pointer (UPP) to a word callback function.
- [struct SpeechXtndData](speechxtnddata.md)
  Defines a speech extension data structure. 
- [struct VoiceDescription](voicedescription.md)
  Defines a voice description structure.
- [struct VoiceFileInfo](voicefileinfo.md)
  Defines a voice file information structure.
- [struct VoiceSpec](voicespec.md)
  Defines a voice specification structure.
### Constants
- [Control Flags Constants](speech_synthesis_manager/1552213-control_flags_constants.md)
  Flags that indicate which synthesizer features are active.
- [Gender Constants](speech_synthesis_manager/1552246-gender_constants.md)
  Constants that indicate the gender of the individual represented by avoice.
- [Audio Unit Constants](speech_synthesis_manager/1552263-audio_unit_constants.md)
  Constants that identify values in a speech synthesis audio unit.
- [Stop Speech Locations](speech_synthesis_manager/1552264-stop_speech_locations.md)
  Locations that indicate where speech should be paused or stopped.
- [Speech Synthesis Manager Operating System Types](speech_synthesis_manager/1552231-speech_synthesis_manager_operati.md)
  The `OSType` definitions used by the Speech Synthesis Manager.
- [Speech-Channel Modes](speech_synthesis_manager/1552256-speech-channel_modes.md)
  The available text-processing and number-processing modes for a speech channel.
- [Speech-Channel Modes for Core Foundation-based Functions](speech_synthesis_manager/speech-channel_modes_for_core_foundation-based_functions.md)
  The available text-processing and number-processing modes for a speech channel.
- [Voice Information Selectors](speech_synthesis_manager/1552254-voice_information_selectors.md)
  The types of voice data that can be requested by the `GetVoiceInfo` function.
- [Speech-Channel Information Constants](speech_synthesis_manager/1552228-speech-channel_information_constants.md)
  Selectors that can be passed to the `GetSpeechInfo` or `SetSpeechInfo` functions.
- [Phoneme Generation Options](speech_synthesis_manager/1552233-phoneme_generation_options.md)
  Flags that specify options for the generation of phonetic output.
- [Speech-Channel Properties](speech_synthesis_manager/speech-channel_properties.md)
  Properties used with [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) or [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) to get or set the characteristics of a speech channel.
- [Synthesizer Option Keys](speech_synthesis_manager/synthesizer_option_keys.md)
  Keys used to specify synthesizer options.
- [Speech Status Keys](speech_synthesis_manager/speech_status_keys.md)
  Keys used with the `kSpeechStatusProperty` property to specify the status of the speech channel.
- [Speech Error Keys](speech_synthesis_manager/speech_error_keys.md)
  Keys used with the `kSpeechErrorsProperty` property to describe errors encountered during speech processing and production.
- [Speech Synthesizer Information Keys](speech_synthesis_manager/speech_synthesizer_information_keys.md)
  Keys used with the `kSpeechSynthesizerInfoProperty` property to get information about the synthesizer.
- [Phoneme Symbols Keys](speech_synthesis_manager/phoneme_symbols_keys.md)
  Keys used with the `kSpeechPhonemeSymbolsProperty` property to provide information about the phoneme being processed.
- [Current Voice Keys](speech_synthesis_manager/current_voice_keys.md)
  Keys used with the `kSpeechCurrentVoiceProperty` property to specify information about the current voice.
- [Command Delimiter Keys](speech_synthesis_manager/command_delimiter_keys.md)
  Keys used with the `kSpeechCommandDelimiterProperty` property to specify information about the command delimiter strings.
- [Speech Dictionary Keys](speech_synthesis_manager/speech_dictionary_keys.md)
  Keys used in a speech dictionary to override the synthesizer’s default pronunciation of a word.
- [Error Callback User-Information String](speech_synthesis_manager/error_callback_user-information_string.md)
  Specifies information about the text being synthesized when an error occurs.
### Result Codes
- [var noSynthFound: Int](../coreservices/nosynthfound.md)
  Could not find the specified speech synthesizer
- [var synthOpenFailed: Int](../coreservices/synthopenfailed.md)
  Could not open another speech synthesizerchannel
- [var synthNotReady: Int](../coreservices/synthnotready.md)
  Speech synthesizer is still busy speaking
- [var bufTooSmall: Int](../coreservices/buftoosmall.md)
  Output buffer is too small to hold result
- [var voiceNotFound: Int](../coreservices/voicenotfound.md)
  Voice resource not found
- [var incompatibleVoice: Int](../coreservices/incompatiblevoice.md)
  Specified voice cannot be used with synthesizer
- [var badDictFormat: Int](../coreservices/baddictformat.md)
  Pronunciation dictionary format error
- [var badInputText: Int](../coreservices/badinputtext.md)
  Raw phoneme text contains invalid characters

## See Also

- [Apple Event Manager](apple_event_manager.md)
- [ColorSync Manager](colorsync_manager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)*