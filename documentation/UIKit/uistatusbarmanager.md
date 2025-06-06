# UIStatusBarManager

**Framework**: UIKit  
**Kind**: class

An object that describes the configuration of the status bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIStatusBarManager
```

#### Overview

Use a [`UIStatusBarManager`](uistatusbarmanager.md) object to get the current configuration of the status bar for its associated scene. You don’t create [`UIStatusBarManager`](uistatusbarmanager.md) objects directly. Instead, you retrieve an existing object from the [`statusBarManager`](uiwindowscene/statusbarmanager.md) property of a [`UIWindowScene`](uiwindowscene.md) object.

You don’t use this object to modify the configuration of the status bar. Instead, you set the status bar configuration individually for each of your [`UIViewController`](uiviewcontroller.md) objects. For example, to modify the default visibility of the status bar, override the [`prefersStatusBarHidden`](uiviewcontroller/prefersstatusbarhidden.md) property of your view controller.

## Topics

### Getting the status bar configuration
- [var isStatusBarHidden: Bool](uistatusbarmanager/isstatusbarhidden.md)
  A Boolean value that indicates whether the status bar is currently hidden.
- [var statusBarStyle: UIStatusBarStyle](uistatusbarmanager/statusbarstyle.md)
  The current appearance of the status bar.
### Getting the frame rectangle
- [var statusBarFrame: CGRect](uistatusbarmanager/statusbarframe.md)
  The frame rectangle of the status bar.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIDevice](uidevice.md)
  A representation of the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistatusbarmanager)*