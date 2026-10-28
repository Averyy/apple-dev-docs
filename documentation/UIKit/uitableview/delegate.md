# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UITableViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UITableViewDelegate> delegate;
```

## Discussion

The delegate must adopt the [`UITableViewDelegate`](../uitableviewdelegate.md) protocol. The delegate isn’t retained.

## See Also

### Related Documentation
- [var dataSource: (any UITableViewDataSource)?](./datasource.md)
  The object that acts as the data source of the table view.
### Managing interactions with the table
- [protocol UITableViewDelegate](../uitableviewdelegate.md)
  Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/delegate)*