# itemIdentifier(for:)

**Framework**: UIKit  
**Kind**: method

Returns an identifier for the item at the specified index path in the table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func itemIdentifier(for indexPath: IndexPath) -> Any?
```

#### Return Value

The item’s identifier, or `nil` if no item is found at the provided index path.

#### Discussion

This method is a constant time operation, O(1), which means you can look up an index path from its corresponding item identifier with no significant overhead.

## Parameters

- `indexPath`: The index path of the item in the table view.

## See Also

- [func indexPath(forItemIdentifier: Any) -> IndexPath?](uitableviewdiffabledatasourcereference/indexpath(foritemidentifier:).md)
  Returns an index path for the item with the specified identifier in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/itemidentifier(for:))*