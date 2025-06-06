# actionForSegment(at:)

**Framework**: UIKit  
**Kind**: method

Fetches the action of the segment at the index you specify, if one exists.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func actionForSegment(at segment: Int) -> UIAction?
```

#### Return Value

The [`UIAction`](uiaction.md) for the segment at the index you specify, or `nil` if the segment doesn’t have an action assigned.

## Parameters

- `segment`: An integer value index of a segment.

## See Also

- [func setAction(UIAction, forSegmentAt: Int)](uisegmentedcontrol/setaction(_:forsegmentat:).md)
  Sets the action for the segment at the index you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/actionforsegment(at:))*