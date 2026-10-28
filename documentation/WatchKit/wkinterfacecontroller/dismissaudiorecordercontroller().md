# dismissAudioRecorderController()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the audio recording interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func dismissAudioRecorderController()
```

```objc
- (void) dismissAudioRecorderController;
```

## Discussion

Use this method to interrupt media playback and dismiss a modal media interface controller. When you dismiss the recording interface programmatically, the recording controller passes a value of [`false`](../../Swift/false.md) for the `didSave` parameter of your completion block.

## See Also

### Presenting video and audio interfaces
- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](./presentmediaplayercontroller%28with,options,completion%29.md)
  Displays a modal interface for playing the specified media file.
- [Media Player Options](../media-player-options.md)
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](./dismissmediaplayercontroller%28%29.md)
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](./presentaudiorecordercontroller%28withoutputurl,preset,options,completion%29.md)
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](../wkaudiorecorderpreset.md)
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](../audio-recording-options.md)
  Options to specify when recording audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller())*