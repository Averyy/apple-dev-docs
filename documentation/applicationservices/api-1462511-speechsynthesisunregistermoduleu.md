# SpeechSynthesisUnregisterModuleURL(_:)

**Framework**: Application Services  
**Kind**: func

Unregisters a registered speech synthesizer or voice.

**Availability**:
- macOS 10.6+ - Deprecated in 13.0

## Declaration

```swift
func SpeechSynthesisUnregisterModuleURL(_ url: CFURL) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `SpeechSynthesisUnregisterModuleURL` function unregisters the speech synthesizer or voice specified by `url`. When a synthesizer is unregistered, all voices that require that synthesizer are automatically unregistered.

Note that if a speech channel is currently using a synthesizer or voice that becomes unregistered, the speech channel is considered inactive and will return an error when the application tries to access it.

An application that called [`SpeechSynthesisRegisterModuleURL(_:)`](1459624-speechsynthesisregistermoduleurl.md) to register a synthesizer or voice should do the following if the volume containing the synthesizer or voice is about to be unmounted:

- Call [`DisposeSpeechChannel(_:)`](1462081-disposespeechchannel.md) to dispose of each speech channel that uses the synthesizer or voice
- Call `SpeechSynthesisUnregisterModuleURL` to unregister the synthesizer or voice

If you call `SpeechSynthesisUnregisterModuleURL` to unregister a synthesizer or voice and you receive either the [`noSynthFound`](https://developer.apple.com/documentation/coreservices/nosynthfound) or [`voiceNotFound`](https://developer.apple.com/documentation/coreservices/voicenotfound) result codes, it means that the synthesizer or voice is not currently registered.

## Parameters

- `url`: The file URL of the synthesizer plug-in or voice to unregister.

## See Also

- [func SpeechSynthesisRegisterModuleURL(CFURL) -> OSErr](1459624-speechsynthesisregistermoduleurl.md)
  Registers and makes available a speech synthesizer or voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462511-speechsynthesisunregistermoduleu)*