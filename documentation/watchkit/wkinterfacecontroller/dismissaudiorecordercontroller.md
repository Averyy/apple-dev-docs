# dismissAudioRecorderController()

**Framework**: WatchKit  
**Kind**: method

Dismisses the audio recording interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func dismissAudioRecorderController()
```

#### Discussion

Use this method to interrupt media playback and dismiss a modal media interface controller. When you dismiss the recording interface programmatically, the recording controller passes a value of [`false`](https://developer.apple.com/documentation/swift/false) for the `didSave` parameter of your completion block.

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](presentmediaplayercontroller(with:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:)))
  Displays a modal interface for playing the specified media file.
- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](dismissmediaplayercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller()))
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset))
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](audio-recording-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/audio-recording-options))
  Options to specify when recording audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller())*