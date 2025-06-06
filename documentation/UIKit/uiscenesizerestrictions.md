# UISceneSizeRestrictions

**Framework**: UIKit  
**Kind**: class

An object that specifies the minimum and maximum sizes for resizable windows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISceneSizeRestrictions
```

#### Overview

Don’t create a [`UISceneSizeRestrictions`](uiscenesizerestrictions.md) object yourself. Instead, fetch an existing one from the [`sizeRestrictions`](uiwindowscene/sizerestrictions.md) property of your window scene, and modify its properties to set the minimum and maximum window sizes. The system provides this object only when it supports variable-sized windows.

## Topics

### Setting the size restrictions
- [var minimumSize: CGSize](uiscenesizerestrictions/minimumsize.md)
  The minimum width and height supported by your app’s windows.
- [var maximumSize: CGSize](uiscenesizerestrictions/maximumsize.md)
  The maximum width and height supported by your app’s windows.
- [var allowsFullScreen: Bool](uiscenesizerestrictions/allowsfullscreen.md)
  A Boolean value that indicates whether the scene can appear full screen.

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

- [var traitCollection: UITraitCollection](uiwindowscene/traitcollection.md)
  The traits that describe the current environment of the scene.
- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/coordinatespace.md)
  The coordinate space occupied by the scene.
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/interfaceorientation.md)
  The orientation to use when displaying content in your windows.
- [var sizeRestrictions: UISceneSizeRestrictions?](uiwindowscene/sizerestrictions.md)
  The minimum and maximum size of the app’s windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesizerestrictions)*