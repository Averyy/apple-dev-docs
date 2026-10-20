# UIWindowScene.PresentationStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The placement of a window scene relative to other scenes in the workspace.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`placement`](./activationrequestoptions/placement.md) instead.

## Declaration

```swift
enum PresentationStyle
```

```c
enum UIWindowScenePresentationStyle : NSUInteger;
```

## Topics

### Constants
- [UIWindowScene.PresentationStyle.automatic](./presentationstyle/automatic.md)
  The system determines the most appropriate style.
- [UIWindowScene.PresentationStyle.prominent](./presentationstyle/prominent.md)
  Presents prominently above others in the current space.
- [UIWindowScene.PresentationStyle.standard](./presentationstyle/standard.md)
  The default style of the system.
### Initializers
- [init?(rawValue: UInt)](./presentationstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [var coordinateSpace: any UICoordinateSpace](./coordinatespace.md)
  The coordinate space occupied by the scene.
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  The orientation to use when displaying content in your windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle)*