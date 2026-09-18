# UIVerticalBarBehavior

**Framework**: UIKit  
**Kind**: enum

A behavior that determines whether the vertical bar is used.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
enum UIVerticalBarBehavior
```

#### Overview

Return this type from [`preferredVerticalBarBehavior`](uiviewcontroller/preferredverticalbarbehavior.md) to apply the preferred behavior.

## Topics

### Specifying vertical bar behavior
- [UIVerticalBarBehavior.automatic](uiverticalbarbehavior/automatic.md)
  The system determines whether the vertical bar is rendered.
- [UIVerticalBarBehavior.disabled](uiverticalbarbehavior/disabled.md)
  The vertical bar is disabled.
### Initializers
- [init?(rawValue: Int)](uiverticalbarbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var preferredVerticalBarBehavior: UIVerticalBarBehavior](uiviewcontroller/preferredverticalbarbehavior.md)
  The vertical bar behavior that this view controller prefers.
- [var childForPreferredVerticalBarBehavior: UIViewController?](uiviewcontroller/childforpreferredverticalbarbehavior.md)
  Which child view controller, if any, should control the vertical bar behavior.
- [func setNeedsUpdateOfVerticalBarConfiguration()](uiviewcontroller/setneedsupdateofverticalbarconfiguration.md)
  Signals to the system that the preferred vertical bar configuration, such as its behavior, has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiverticalbarbehavior)*