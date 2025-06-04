# dismissMediaPlayerController()

**Framework**: Watchkit  
**Kind**: method

Dismisses the media interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func dismissMediaPlayerController()
```

## Overview

Use this method to dismiss a modal media interface controller programmatically. When you dismiss the media interface programmatically, WatchKit passes a value of [`false`](https://developer.apple.com/documentation/swift/false) for the `didPlayToEnd` parameter of your completion block and passes a value of `0.0` for the`endTime` parameter.

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](presentmediaplayercontroller(with:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:)))
- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset))
- [Audio Recording Options](audio-recording-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/audio-recording-options))
- [func dismissAudioRecorderController()](dismissaudiorecordercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller())*