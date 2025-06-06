# delegate

**Framework**: UIKit  
**Kind**: property

The search bar’s delegate object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UISearchBarDelegate)? { get set }
```

#### Discussion

The delegate should conform to the [`UISearchBarDelegate`](uisearchbardelegate.md) protocol. Set this property to further modify the behavior. The default value is `nil`.

## See Also

- [protocol UISearchBarDelegate](uisearchbardelegate.md)
  A collection of optional methods that you implement to make a search bar control functional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/delegate)*