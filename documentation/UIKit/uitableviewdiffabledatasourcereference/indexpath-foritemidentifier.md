# indexPath(forItemIdentifier:)

**Framework**: UIKit  
**Kind**: method

Returns an index path for the item with the specified identifier in the table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func indexPath(forItemIdentifier identifier: Any) -> IndexPath?
```

#### Return Value

The item’s index path, or `nil` if no item is found with the provided item identifier.

#### Discussion

This method is a constant time operation, O(1), which means you can look up an index path from its corresponding item identifier with no significant overhead.

## Parameters

- `identifier`: The identifier of the item in the table view.

## See Also

- [func itemIdentifier(for: IndexPath) -> Any?](uitableviewdiffabledatasourcereference/itemidentifier(for:).md)
  Returns an identifier for the item at the specified index path in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/indexpath(foritemidentifier:))*