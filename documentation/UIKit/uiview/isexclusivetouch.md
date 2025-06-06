# isExclusiveTouch

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the receiver handles touch events exclusively.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isExclusiveTouch: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) causes the receiver to block the delivery of touch events to other views in the same window. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isUserInteractionEnabled: Bool](uiview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isMultipleTouchEnabled: Bool](uiview/ismultipletouchenabled.md)
  A Boolean value that indicates whether the view receives more than one touch at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/isexclusivetouch)*