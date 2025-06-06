# position(from:toBoundary:inDirection:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Return the next text position at a boundary of a text unit of the given granularity in a given direction.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func position(from position: UITextPosition, toBoundary granularity: UITextGranularity, inDirection direction: UITextDirection) -> UITextPosition?
```

#### Return Value

The next boundary position of a text unit of the given granularity in the given direction, or `nil` if there is no such position.

## Parameters

- `position`: A text-position object that represents a location in a document.
- `granularity`: A constant that indicates a certain granularity of text unit.
- `direction`: A constant that indicates a direction relative to  . The constant can be of type UITextStorageDirection or UITextLayoutDirection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/position(from:toboundary:indirection:))*