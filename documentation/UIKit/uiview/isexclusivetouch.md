# isExclusiveTouch

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver handles touch events exclusively.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
var isExclusiveTouch: Bool { get set }
```

```objc
@property (nonatomic, getter=isExclusiveTouch) BOOL exclusiveTouch;
```

#### Discussion

Setting this property to [`true`](../../Swift/true.md) causes the receiver to block the delivery of touch events to other views in the same window. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the event-related behavior
- [var isUserInteractionEnabled: Bool](./isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isMultipleTouchEnabled: Bool](./ismultipletouchenabled.md)
  A Boolean value that indicates whether the view receives more than one touch at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/isexclusivetouch)*