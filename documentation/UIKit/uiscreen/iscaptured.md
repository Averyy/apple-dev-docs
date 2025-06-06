# isCaptured

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the system is actively cloning the screen to another destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+

## Declaration

```swift
@MainActor
var isCaptured: Bool { get }
```

#### Discussion

A value of `YES` indicates the system is actively recording, mirroring, or using AirPlay to stream the contents of the screen.

Observe this property and optionally take an appropriate action in your app to prevent the capture of your content. For example, a media app might stop any current media playback and present a dialog to the user describing the reason for the pause.

> ❗ **Important**:  The system doesn’t include video content encrypted using [`FairPlay Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/) (FPS) when recording, mirroring, or using AirPlay to stream the contents of the screen. However, although it blacks out FPS-encrypted video content, it includes FPS-encrypted audio content. To prevent the system from recording the audio portion, observe the `isCaptured` property and take appropriate action in your app as described above.

 The system doesn’t include video content encrypted using [`FairPlay Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/) (FPS) when recording, mirroring, or using AirPlay to stream the contents of the screen. However, although it blacks out FPS-encrypted video content, it includes FPS-encrypted audio content. To prevent the system from recording the audio portion, observe the `isCaptured` property and take appropriate action in your app as described above.

UIKit sends the [`capturedDidChangeNotification`](uiscreen/captureddidchangenotification.md) notification when the capture status of the screen changes.

## See Also

- [class let userDidTakeScreenshotNotification: NSNotification.Name](uiapplication/userdidtakescreenshotnotification.md)
  A notification that posts when a person takes a screenshot on the device.
- [var mirrored: UIScreen?](uiscreen/mirrored.md)
  The screen an external display mirrors from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/iscaptured)*