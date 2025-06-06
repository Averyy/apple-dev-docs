# isPosition(_:withinTextUnit:inDirection:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Return whether a text position is within a text unit of a specified granularity in a specified direction.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func isPosition(_ position: UITextPosition, withinTextUnit granularity: UITextGranularity, inDirection direction: UITextDirection) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the text position is within a text unit of the specified granularity in the specified direction; otherwise, return [`false`](https://developer.apple.com/documentation/swift/false). If the text position is  a boundary, return [`true`](https://developer.apple.com/documentation/swift/true) only if the boundary is part of the text unit in the given direction.

## Parameters

- `position`: A text-position object that represents a location in a document.
- `granularity`: A constant that indicates a certain granularity of text unit.
- `direction`: A constant that indicates a direction relative to  . The constant can be of type UITextStorageDirection or UITextLayoutDirection.

## See Also

- [func isPosition(UITextPosition, atBoundary: UITextGranularity, inDirection: UITextDirection) -> Bool](uitextinputtokenizer/isposition(_:atboundary:indirection:).md)
  Return whether a text position is at a boundary of a text unit of a specified granularity in a specified direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/isposition(_:withintextunit:indirection:))*