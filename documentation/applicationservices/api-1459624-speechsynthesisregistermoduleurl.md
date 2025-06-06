# SpeechSynthesisRegisterModuleURL(_:)

**Framework**: Application Services  
**Kind**: func

Registers and makes available a speech synthesizer or voice.

**Availability**:
- macOS 10.6+ - Deprecated in 13.0

## Declaration

```swift
func SpeechSynthesisRegisterModuleURL(_ url: CFURL) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `SpeechSynthesisRegisterModuleURL` function registers the speech synthesizer or voice specified by `url` and makes it available to the calling process. Before a synthesizer’s voices can be registered, the synthesizer must be registered (or loaded automatically by the Speech Synthesis Manager). If you call `SpeechSynthesisRegisterModuleURL` to register a voice and you receive the [`incompatibleVoice`](https://developer.apple.com/documentation/coreservices/incompatiblevoice) result code, it’s likely that the synthesizer associated with the voice needs to be registered. If you call this function to register a synthesizer or voice that has already been registered, `SpeechSynthesisRegisterModuleURL` does nothing and returns an error.

A registered synthesizer or voice is known only to the application that registered it. For this reason, each application must call `SpeechSynthesisRegisterModuleURL` to register the synthesizer or voice it uses, even if a suite of applications work together and use the same synthesizer and voice.

An application that called `SpeechSynthesisRegisterModuleURL` to register a synthesizer or voice should do the following if the volume containing the synthesizer or voice is about to be unmounted:

- Call [`DisposeSpeechChannel(_:)`](1462081-disposespeechchannel.md) to dispose of each speech channel that uses the synthesizer or voice
- Call [`SpeechSynthesisUnregisterModuleURL(_:)`](1462511-speechsynthesisunregistermoduleu.md) to unregister the synthesizer or voice

## Parameters

- `url`: The file URL of the synthesizer plug-in or voice to register (note that the synthesizer plug-in or voice must be on a mounted volume to be available for registration).

## See Also

- [func SpeechSynthesisUnregisterModuleURL(CFURL) -> OSErr](1462511-speechsynthesisunregistermoduleu.md)
  Unregisters a registered speech synthesizer or voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459624-speechsynthesisregistermoduleurl)*