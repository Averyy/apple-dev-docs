# UIScrollType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define the type of the scroll.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
enum UIScrollType
```

```c
enum UIScrollType : NSUInteger;
```

## Topics

### Constants
- [UIScrollType.discrete](./uiscrolltype/discrete.md)
  A discrete scroll type that originates from a device like a mouse with a scroll wheel.
- [UIScrollType.continuous](./uiscrolltype/continuous.md)
  A continuous scroll type that originates from a device like a trackpad.
### Initializers
- [init?(rawValue: UInt)](./uiscrolltype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tracking scroll events
- [var allowedScrollTypesMask: UIScrollTypeMask](./uipangesturerecognizer/allowedscrolltypesmask.md)
  A scroll type mask that enables recognition of scroll events.
- [struct UIScrollTypeMask](./uiscrolltypemask.md)
  A bit mask identifying the scroll type of a pan gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrolltype)*