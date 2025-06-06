# containsStart

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the rectangle contains the start of the selection.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var containsStart: Bool { get }
```

#### Discussion

The value of this property is used to determine the placement of the selection handles in bidirectional text. It provides a clue to the system about whether the start of the selection is in the specified rectangle.

## See Also

- [var containsEnd: Bool](uitextselectionrect/containsend.md)
  A Boolean value that indicates whether the rectangle contains the end of the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionrect/containsstart)*