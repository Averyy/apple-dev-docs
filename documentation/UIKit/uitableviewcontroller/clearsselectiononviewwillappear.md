# clearsSelectionOnViewWillAppear

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating if the controller clears the selection when the table appears.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var clearsSelectionOnViewWillAppear: Bool { get set }
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). When [`true`](https://developer.apple.com/documentation/Swift/true), the table view controller clears the table’s current selection when it receives a [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) message. Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) preserves the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcontroller/clearsselectiononviewwillappear)*