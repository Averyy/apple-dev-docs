# brightnessDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when a screen’s brightness changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
nonisolated
class let brightnessDidChangeNotification: NSNotification.Name
```

#### Discussion

The object of the notification is the [`UIScreen`](uiscreen.md) object whose [`brightness`](uiscreen/brightness.md) property changed. There is no `userInfo` dictionary.

## See Also

- [class let modeDidChangeNotification: NSNotification.Name](uiscreen/modedidchangenotification.md)
  A notification that posts when a screen’s mode changes.
- [class let capturedDidChangeNotification: NSNotification.Name](uiscreen/captureddidchangenotification.md)
  A notification that posts when the capture status of a screen changes.
- [class let referenceDisplayModeStatusDidChangeNotification: NSNotification.Name](uiscreen/referencedisplaymodestatusdidchangenotification.md)
  A notification that posts when there’s a change to a screen’s reference display mode status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/brightnessdidchangenotification)*