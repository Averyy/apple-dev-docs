# WKAudioRecorderPreset

**Framework**: Watchkit  
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
- [WKAudioRecorderPreset.narrowBandSpeech](narrowbandspeech.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/narrowbandspeech))
  Audio quality suitable for basic speech recording. This preset records audio with an 8 kHz sampling rate using either the LPCM 128 kbps or AAC 24 kbps format.
- [WKAudioRecorderPreset.wideBandSpeech](widebandspeech.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/widebandspeech))
  Audio quality suitable for higher fidelity speech recording. This preset records audio with a 16 kHz sampling rate using either the LPCM 256 kbps or AAC 32 kbps format.
- [WKAudioRecorderPreset.highQualityAudio](highqualityaudio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/highqualityaudio))
  A high-quality audio recording. This preset records audio with a 44.1 kHz sampling rate using either the LPCM 705.6 kbps or AAC 96 kbps format.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](presentmediaplayercontroller(with:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:)))
- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
- [func dismissMediaPlayerController()](dismissmediaplayercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller()))
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
- [Audio Recording Options](audio-recording-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/audio-recording-options))
- [func dismissAudioRecorderController()](dismissaudiorecordercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset)*