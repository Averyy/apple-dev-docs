# compare(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns how one text position compares to another text position.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func compare(_ position: UITextPosition, to other: UITextPosition) -> ComparisonResult
```

#### Return Value

A value that indicates whether the two text positions are identical or whether one is before the other.

## Parameters

- `position`: A custom object that represents a location within a document.
- `other`: A custom object that represents another location within a document.

## See Also

- [func offset(from: UITextPosition, to: UITextPosition) -> Int](uitextinput/offset(from:to:).md)
  Returns the number of UTF-16 characters between one text position and another text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/compare(_:to:))*