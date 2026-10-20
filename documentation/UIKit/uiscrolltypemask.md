# UIScrollTypeMask

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A bit mask identifying the scroll type of a pan gesture.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
struct UIScrollTypeMask
```

```c
enum UIScrollTypeMask : NSInteger;
```

## Topics

### Scroll types
- [static var all: UIScrollTypeMask](./uiscrolltypemask/all.md)
  A scroll type that’s either discrete or continuous.
- [static var continuous: UIScrollTypeMask](./uiscrolltypemask/continuous.md)
  A continuous scroll type from a device, like a trackpad.
- [static var discrete: UIScrollTypeMask](./uiscrolltypemask/discrete.md)
  A discrete scroll type from a device, like a mouse.
### Initializer
- [init(rawValue: Int)](./uiscrolltypemask/init%28rawvalue%29.md)
  Creates a new scroll type mask from the raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Tracking scroll events
- [var allowedScrollTypesMask: UIScrollTypeMask](./uipangesturerecognizer/allowedscrolltypesmask.md)
  A scroll type mask that enables recognition of scroll events.
- [enum UIScrollType](./uiscrolltype.md)
  Constants that define the type of the scroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrolltypemask)*