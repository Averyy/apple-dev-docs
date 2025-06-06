# UIScrollTypeMask

**Framework**: UIKit  
**Kind**: struct

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

## Topics

### Scroll types
- [static var all: UIScrollTypeMask](uiscrolltypemask/all.md)
  A scroll type that’s either discrete or continuous.
- [static var continuous: UIScrollTypeMask](uiscrolltypemask/continuous.md)
  A continuous scroll type from a device, like a trackpad.
- [static var discrete: UIScrollTypeMask](uiscrolltypemask/discrete.md)
  A discrete scroll type from a device, like a mouse.
### Initializer
- [init(rawValue: Int)](uiscrolltypemask/init(rawvalue:).md)
  Creates a new scroll type mask from the raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var allowedScrollTypesMask: UIScrollTypeMask](uipangesturerecognizer/allowedscrolltypesmask.md)
  A scroll type mask that enables recognition of scroll events.
- [enum UIScrollType](uiscrolltype.md)
  Constants that define the type of the scroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrolltypemask)*