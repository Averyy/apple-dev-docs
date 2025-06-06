# offset(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the number of UTF-16 characters between one text position and another text position.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func offset(from: UITextPosition, to toPosition: UITextPosition) -> Int
```

#### Return Value

The number of UTF-16 characters between `fromPosition` and `toPosition`.

## Parameters

- `from`: A custom object that represents a location within a document.
- `toPosition`: A custom object that represents another location within document.

## See Also

- [func compare(UITextPosition, to: UITextPosition) -> ComparisonResult](uitextinput/compare(_:to:).md)
  Returns how one text position compares to another text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/offset(from:to:))*