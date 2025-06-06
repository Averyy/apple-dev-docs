# numberOfSections

**Framework**: UIKit  
**Kind**: property

The number of sections in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var numberOfSections: Int { get }
```

#### Discussion

[`UITableView`](uitableview.md) gets the value in this property from its data source and caches it.

## See Also

- [func numberOfRows(inSection: Int) -> Int](uitableview/numberofrows(insection:).md)
  Returns the number of rows (table cells) in a specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/numberofsections)*