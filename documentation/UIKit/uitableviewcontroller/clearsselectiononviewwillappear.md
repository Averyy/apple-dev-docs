# clearsSelectionOnViewWillAppear

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating if the controller clears the selection when the table appears.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearsSelectionOnViewWillAppear: Bool { get set }
```

```objc
@property (nonatomic) BOOL clearsSelectionOnViewWillAppear;
```

## Mentions

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md)

## Discussion

The default value of this property is [`true`](../../Swift/true.md). When [`true`](../../Swift/true.md), the table view controller clears the table’s current selection when it receives a [`viewWillAppear(_:)`](../uiviewcontroller/viewwillappear%28_%29.md) message. Setting this property to [`false`](../../Swift/false.md) preserves the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcontroller/clearsselectiononviewwillappear)*