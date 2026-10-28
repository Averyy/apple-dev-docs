# compare(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns how one text position compares to another text position.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func compare(_ position: UITextPosition, to other: UITextPosition) -> ComparisonResult
```

```objc
- (NSComparisonResult) comparePosition:(UITextPosition *) position toPosition:(UITextPosition *) other;
```

## Return Value

A value that indicates whether the two text positions are identical or whether one is before the other.

## Parameters

- `position`: A custom object that represents a location within a document.
- `other`: A custom object that represents another location within a document.

## See Also

### Evaluating text positions
- [func offset(from: UITextPosition, to: UITextPosition) -> Int](./offset%28from,to%29.md)
  Returns the number of UTF-16 characters between one text position and another text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/compare(_:to:))*