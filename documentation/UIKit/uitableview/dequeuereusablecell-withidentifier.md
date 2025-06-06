# dequeueReusableCell(withIdentifier:)

**Framework**: UIKit  
**Kind**: method

Returns a reusable table-view cell object after locating it by its identifier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dequeueReusableCell(withIdentifier identifier: String) -> UITableViewCell?
```

#### Return Value

A [`UITableViewCell`](uitableviewcell.md) object with the associated `identifier`, or `nil` if no such object exists in the reusable-cell queue.

#### Discussion

For performance reasons, a table view’s data source should generally reuse [`UITableViewCell`](uitableviewcell.md) objects when it assigns cells to rows in its [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) method. A table view maintains a queue or list of [`UITableViewCell`](uitableviewcell.md) objects that the data source has marked for reuse. Call this method from your data source object when asked to provide a new cell for the table view. This method dequeues an existing cell if one is available or creates a new one using the class or nib file you previously registered. If no cell is available for reuse and you didn’t register a class or nib file, this method returns `nil`.

If you registered a class for the specified `identifier` and a new cell must be created, this method initializes the cell by calling its [`init(style:reuseIdentifier:)`](uitableviewcell/init(style:reuseidentifier:).md) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [`prepareForReuse()`](uitableviewcell/prepareforreuse().md) method instead.

## Parameters

- `identifier`: A string identifying the cell object to be reused. This parameter must not be  .

## See Also

- [func register(UINib?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-5q6bo.md)
  Registers a nib object that contains a cell with the table view under a specified identifier.
- [func register(AnyClass?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-3l3ct.md)
  Registers a class to use in creating new table cells.
- [func dequeueReusableCell(withIdentifier: String, for: IndexPath) -> UITableViewCell](uitableview/dequeuereusablecell(withidentifier:for:).md)
  Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/dequeuereusablecell(withidentifier:))*