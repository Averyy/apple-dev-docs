# reuseIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string for identifying a reusable cell.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var reuseIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * reuseIdentifier;
```

## Discussion

The reuse identifier is associated with a [`UITableViewCell`](../uitableviewcell.md) object that the table-view’s delegate creates with the intent to reuse it as the basis (for performance reasons) for multiple rows of a table view. It is assigned to the cell object in [`initWithFrame:reuseIdentifier:`](./initwithframe_reuseidentifier_.md) and cannot be changed thereafter. A [`UITableView`](../uitableview.md) object maintains a queue (or list) of the currently reusable cells, each with its own reuse identifier, and makes them available to the delegate in the [`dequeueReusableCell(withIdentifier:)`](../uitableview/dequeuereusablecell%28withidentifier%29.md) method.

## See Also

### Reusing cells
- [func prepareForReuse()](./prepareforreuse%28%29.md)
  Prepares a reusable cell for reuse by the table view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/reuseidentifier)*