# dismissMediaPlayerController()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the media interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func dismissMediaPlayerController()
```

```objc
- (void) dismissMediaPlayerController;
```

#### Discussion

Use this method to dismiss a modal media interface controller programmatically. When you dismiss the media interface programmatically, WatchKit passes a value of [`false`](../../Swift/false.md) for the `didPlayToEnd` parameter of your completion block and passes a value of `0.0` for the`endTime` parameter.

## See Also

### Presenting video and audio interfaces
- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](./presentmediaplayercontroller%28with,options,completion%29.md)
  Displays a modal interface for playing the specified media file.
- [Media Player Options](../media-player-options.md)
  Keys indicating media playback options.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](./presentaudiorecordercontroller%28withoutputurl,preset,options,completion%29.md)
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](../wkaudiorecorderpreset.md)
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](../audio-recording-options.md)
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](./dismissaudiorecordercontroller%28%29.md)
  Dismisses the audio recording interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller())*