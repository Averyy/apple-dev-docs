# dismissMediaPlayerController()

**Framework**: WatchKit  
**Kind**: method

Dismisses the media interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func dismissMediaPlayerController()
```

#### Discussion

Use this method to dismiss a modal media interface controller programmatically. When you dismiss the media interface programmatically, WatchKit passes a value of [`false`](https://developer.apple.com/documentation/swift/false) for the `didPlayToEnd` parameter of your completion block and passes a value of `0.0` for the`endTime` parameter.

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](presentmediaplayercontroller(with:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:)))
  Displays a modal interface for playing the specified media file.
- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
  Keys indicating media playback options.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset))
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](audio-recording-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/audio-recording-options))
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](dismissaudiorecordercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller()))
  Dismisses the audio recording interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller())*