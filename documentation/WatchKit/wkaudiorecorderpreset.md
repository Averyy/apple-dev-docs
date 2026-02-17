# WKAudioRecorderPreset

**Framework**: WatchKit  
**Kind**: enum

Constants indicating the quality of audio recordings.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKAudioRecorderPreset
```

## Topics

### Constants
- [WKAudioRecorderPreset.narrowBandSpeech](wkaudiorecorderpreset/narrowbandspeech.md)
  Audio quality suitable for basic speech recording. This preset records audio with an 8 kHz sampling rate using either the LPCM 128 kbps or AAC 24 kbps format.
- [WKAudioRecorderPreset.wideBandSpeech](wkaudiorecorderpreset/widebandspeech.md)
  Audio quality suitable for higher fidelity speech recording. This preset records audio with a 16 kHz sampling rate using either the LPCM 256 kbps or AAC 32 kbps format.
- [WKAudioRecorderPreset.highQualityAudio](wkaudiorecorderpreset/highqualityaudio.md)
  A high-quality audio recording. This preset records audio with a 44.1 kHz sampling rate using either the LPCM 705.6 kbps or AAC 96 kbps format.
### Initializers
- [init?(rawValue: Int)](wkaudiorecorderpreset/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:).md)
  Displays a modal interface for playing the specified media file.
- [Media Player Options](media-player-options.md)
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](wkinterfacecontroller/dismissmediaplayercontroller.md)
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md)
  Display a standard interface for recording audio from the user’s Apple Watch.
- [Audio Recording Options](audio-recording-options.md)
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](wkinterfacecontroller/dismissaudiorecordercontroller.md)
  Dismisses the audio recording interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset)*