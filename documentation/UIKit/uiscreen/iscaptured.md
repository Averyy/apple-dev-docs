# isCaptured

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system is actively cloning the screen to another destination.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2

> **Deprecated**: Use [`sceneCaptureState`](../uitraitcollection/scenecapturestate.md) instead.

## Declaration

```swift
var isCaptured: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCaptured) BOOL captured;
```

## Discussion

A value of `YES` indicates the system is actively recording, mirroring, or using AirPlay to stream the contents of the screen.

Observe this property and optionally take an appropriate action in your app to prevent the capture of your content. For example, a media app might stop any current media playback and present a dialog to the user describing the reason for the pause.

> ❗ **Important**:  The system doesn’t include video content encrypted using [FairPlay Streaming](https://developer.apple.com/streaming/fps/) (FPS) when recording, mirroring, or using AirPlay to stream the contents of the screen. However, although it blacks out FPS-encrypted video content, it includes FPS-encrypted audio content. To prevent the system from recording the audio portion, observe the `isCaptured` property and take appropriate action in your app as described above.

UIKit sends the [`capturedDidChangeNotification`](./captureddidchangenotification.md) notification when the capture status of the screen changes.

## See Also

### Related Documentation
- [class let userDidTakeScreenshotNotification: NSNotification.Name](../uiapplication/userdidtakescreenshotnotification.md)
  A notification that posts when a person takes a screenshot on the device.
### Deprecated properties
- [class var main: UIScreen](./main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](./screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](./applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](./focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](./focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](./supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/iscaptured)*