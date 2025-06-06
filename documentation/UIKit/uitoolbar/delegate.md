# delegate

**Framework**: UIKit  
**Kind**: property

The toolbar’s delegate object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIToolbarDelegate)? { get set }
```

#### Discussion

The delegate should conform to the `UIToolbarDelegate` protocol. You may not set the delegate when the toolbar is managed by a navigation controller. The default value is `nil`.

## See Also

- [protocol UIToolbarDelegate](uitoolbardelegate.md)
  The interface that toolbar delegate objects implement to manage the toolbar behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/delegate)*