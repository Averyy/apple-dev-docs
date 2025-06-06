# isMultipleTouchEnabled

**Framework**: Uikit  
**Kind**: property

A Boolean value that indicates whether the view receives more than one touch at a time.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isMultipleTouchEnabled: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the view receives all touches associated with a multi-touch sequence and starting within the view’s bounds. When set to [`false`](https://developer.apple.com/documentation/swift/false), the view receives only the first touch event in a multi-touch sequence that start within the view’s bounds. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  This property does not affect the gesture recognizers attached to the view. Gesture recognizers receive all touches that occur in the view.

Other views in the same window can still receive touch events when this property is [`false`](https://developer.apple.com/documentation/swift/false). If you want this view to handle multi-touch events exclusively, set the values of both this property and the [`isExclusiveTouch`](uiview/isexclusivetouch.md) property to [`true`](https://developer.apple.com/documentation/swift/true). This property does not prevent a view from being asked to handle multiple touches. For example, two subviews may both forward their touches to a common parent, such as a window or the root view of a view controller. This property determines how many touches initially targeting the view are delivered to that view.

## See Also

- [var isUserInteractionEnabled: Bool](uiview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isExclusiveTouch: Bool](uiview/isexclusivetouch.md)
  A Boolean value that indicates whether the receiver handles touch events exclusively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/ismultipletouchenabled)*