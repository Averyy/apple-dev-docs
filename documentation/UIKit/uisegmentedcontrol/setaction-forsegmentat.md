# setAction(_:forSegmentAt:)

**Framework**: UIKit  
**Kind**: method

Sets the action for the segment at the index you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setAction(_ action: UIAction, forSegmentAt segment: Int)
```

#### Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [`UIActionHandler`](uiactionhandler.md), as well as handlers for the [`valueChanged`](uicontrol/event/valuechanged.md) and [`primaryActionTriggered`](uicontrol/event/primaryactiontriggered.md) control events.

> **Note**:  This method asserts an error if the action’s [`UIAction.Identifier`](uiaction/identifier-swift.struct.md) doesn’t match the action of the existing segment at this index, or isn’t unique within all actions associated with the segmented control.

 This method asserts an error if the action’s [`UIAction.Identifier`](uiaction/identifier-swift.struct.md) doesn’t match the action of the existing segment at this index, or isn’t unique within all actions associated with the segmented control.

## Parameters

- `action`: A   object to set on the segment at the index you specify.
- `segment`: An integer index of a segment.

## See Also

- [func actionForSegment(at: Int) -> UIAction?](uisegmentedcontrol/actionforsegment(at:).md)
  Fetches the action of the segment at the index you specify, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setaction(_:forsegmentat:))*