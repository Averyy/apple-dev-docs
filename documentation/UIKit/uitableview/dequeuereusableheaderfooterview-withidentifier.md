# dequeueReusableHeaderFooterView(withIdentifier:)

**Framework**: UIKit  
**Kind**: method

Returns a reusable header or footer view after locating it by its identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dequeueReusableHeaderFooterView(withIdentifier identifier: String) -> UITableViewHeaderFooterView?
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Return Value

A [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md) object with the associated identifier or `nil` if no such object exists in the reusable view queue.

#### Discussion

For performance reasons, a table view’s delegate should generally reuse [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md) objects when it’s asked to provide them. A table view maintains a queue or list of [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md) objects that the table view’s delegate has marked for reuse. It marks a view for reuse by assigning it a reuse identifier when it creates it (in the [`init(reuseIdentifier:)`](uitableviewheaderfooterview/init(reuseidentifier:).md) method of [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md)).

You can use this method to access specific template header and footer views that you previously created. You can access a view’s reuse identifier through its [`reuseIdentifier`](uitableviewheaderfooterview/reuseidentifier.md) property.

## Parameters

- `identifier`: A string identifying the header or footer view to be reused. This parameter must not be  .

## See Also

- [func register(UINib?, forHeaderFooterViewReuseIdentifier: String)](uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc.md)
  Registers a nib object that contains a header or footer with the table view under a specified identifier.
- [func register(AnyClass?, forHeaderFooterViewReuseIdentifier: String)](uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb.md)
  Registers a class to use in creating new table header or footer views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/dequeuereusableheaderfooterview(withidentifier:))*