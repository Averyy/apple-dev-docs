# isPosition(_:atBoundary:inDirection:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Return whether a text position is at a boundary of a text unit of a specified granularity in a specified direction.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func isPosition(_ position: UITextPosition, atBoundary granularity: UITextGranularity, inDirection direction: UITextDirection) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the text position is at the given text-unit boundary in the given direction; [`false`](https://developer.apple.com/documentation/Swift/false) if it is not at the boundary.

## Parameters

- `position`: A text-position object that represents a location in a document.
- `granularity`: A constant that indicates a certain granularity of text unit.
- `direction`: A constant that indicates a direction relative to  . The constant can be of type UITextStorageDirection or UITextLayoutDirection.

## See Also

- [func isPosition(UITextPosition, withinTextUnit: UITextGranularity, inDirection: UITextDirection) -> Bool](uitextinputtokenizer/isposition(_:withintextunit:indirection:).md)
  Return whether a text position is within a text unit of a specified granularity in a specified direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/isposition(_:atboundary:indirection:))*