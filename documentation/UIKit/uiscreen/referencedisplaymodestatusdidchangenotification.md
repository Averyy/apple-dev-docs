# referenceDisplayModeStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when there’s a change to a screen’s reference display mode status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+

## Declaration

```swift
nonisolated
class let referenceDisplayModeStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification’s [`object`](https://developer.apple.com/documentation/Foundation/Notification/object) is the changed screen. Use that object’s [`referenceDisplayModeStatus`](uiscreen/referencedisplaymodestatus-swift.property.md) property to retrieve the new status.

The system posts this notification on the main actor.

## See Also

- [class let brightnessDidChangeNotification: NSNotification.Name](uiscreen/brightnessdidchangenotification.md)
  A notification that posts when a screen’s brightness changes.
- [class let modeDidChangeNotification: NSNotification.Name](uiscreen/modedidchangenotification.md)
  A notification that posts when a screen’s mode changes.
- [class let capturedDidChangeNotification: NSNotification.Name](uiscreen/captureddidchangenotification.md)
  A notification that posts when the capture status of a screen changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatusdidchangenotification)*