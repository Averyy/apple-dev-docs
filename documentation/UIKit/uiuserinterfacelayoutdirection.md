# UIUserInterfaceLayoutDirection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the directional flow of the user interface.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum UIUserInterfaceLayoutDirection
```

```c
enum UIUserInterfaceLayoutDirection : NSInteger;
```

#### Overview

One of these constants is returned by the [`userInterfaceLayoutDirection`](./uiapplication/userinterfacelayoutdirection.md) property. It indicates the directionality of the language in the user interface of the app.

## Topics

### Constants
- [UIUserInterfaceLayoutDirection.leftToRight](./uiuserinterfacelayoutdirection/lefttoright.md)
  The layout direction is left to right.
- [UIUserInterfaceLayoutDirection.rightToLeft](./uiuserinterfacelayoutdirection/righttoleft.md)
  The layout direction right to left.
### Initializers
- [init?(rawValue: Int)](./uiuserinterfacelayoutdirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing the layout direction
- [var userInterfaceLayoutDirection: UIUserInterfaceLayoutDirection](./uiapplication/userinterfacelayoutdirection.md)
  The layout direction of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)*