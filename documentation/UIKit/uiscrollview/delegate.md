# delegate

**Framework**: UIKit  
**Kind**: property

The delegate of the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIScrollViewDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`UIScrollViewDelegate`](uiscrollviewdelegate.md) protocol. The [`UIScrollView`](uiscrollview.md) class, which doesn’t retain the delegate, invokes each protocol method the delegate implements.

## See Also

- [protocol UIScrollViewDelegate](uiscrollviewdelegate.md)
  The interface for the delegate of a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/delegate)*