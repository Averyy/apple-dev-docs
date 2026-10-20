# UIStatusBarAnimation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the animation of the status bar as it’s hidden or made visible.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
enum UIStatusBarAnimation
```

```c
enum UIStatusBarAnimation : NSInteger;
```

#### Overview

Constants of the [`UIStatusBarAnimation`](./uistatusbaranimation.md) type are arguments of the [`setStatusBarHidden(_:with:)`](./uiapplication/setstatusbarhidden%28_,with%29.md) method.

## Topics

### Constants
- [UIStatusBarAnimation.none](./uistatusbaranimation/none.md)
  No animation is applied to the status bar as it is shown or hidden.
- [UIStatusBarAnimation.fade](./uistatusbaranimation/fade.md)
  The status bar fades in and out as it is shown or hidden, respectively.
- [UIStatusBarAnimation.slide](./uistatusbaranimation/slide.md)
  The status bar slides in or out as it is shown or hidden, respectively.
### Initializers
- [init?(rawValue: Int)](./uistatusbaranimation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated enumerations
- [struct UIDirectionalRectEdge](./uidirectionalrectedge.md)
  Constants that specify an edge or a set of edges, taking the user interface layout direction into account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistatusbaranimation)*