# transfersVerticalScrollingToParent

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the scroll view passes vertical scroll events to a superview.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
var transfersVerticalScrollingToParent: Bool { get set }
```

#### Discussion

The default value is `true`, in which case when the scroll view reaches either end of its vertical scroll axis it transfers scroll events to a containing scroll view. To stop this behavior, set the property to `false`.

## See Also

- [var transfersHorizontalScrollingToParent: Bool](uiscrollview/transfershorizontalscrollingtoparent.md)
  A Boolean value that determines whether the scroll view passes horizontal scroll events to a superview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/transfersverticalscrollingtoparent)*