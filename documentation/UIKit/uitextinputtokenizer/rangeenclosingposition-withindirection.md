# rangeEnclosingPosition(_:with:inDirection:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Return the range for the text enclosing a text position in a text unit of a given granularity in a given direction.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func rangeEnclosingPosition(_ position: UITextPosition, with granularity: UITextGranularity, inDirection direction: UITextDirection) -> UITextRange?
```

#### Return Value

A text-range representing a text unit of the given granularity in the given direction, or `nil` if there is no such enclosing unit.  Whether a boundary position is enclosed depends on the given direction, using the same rule as the [`isPosition(_:withinTextUnit:inDirection:)`](uitextinputtokenizer/isposition(_:withintextunit:indirection:).md) method.

#### Discussion

In this method, return the range for the text enclosing a text position in a text unit of the given granularity, or `nil` if there is no such enclosing unit.  If the text position is entirely enclosed within a text unit of the given granularity, it is considered enclosed. If the text position is at a text-unit boundary, it is considered enclosed only if the next position in the given direction is entirely enclosed.

## Parameters

- `position`: A text-position object that represents a location in a document.
- `granularity`: A constant that indicates a certain granularity of text unit.
- `direction`: A constant that indicates a direction relative to  . The constant can be of type UITextStorageDirection or UITextLayoutDirection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/rangeenclosingposition(_:with:indirection:))*