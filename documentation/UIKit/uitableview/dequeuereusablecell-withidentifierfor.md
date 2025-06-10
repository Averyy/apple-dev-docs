# dequeueReusableCell(withIdentifier:for:)

**Framework**: UIKit  
**Kind**: method

Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dequeueReusableCell(withIdentifier identifier: String, for indexPath: IndexPath) -> UITableViewCell
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
- [Filling a table with data](filling-a-table-with-data.md)

#### Return Value

A [`UITableViewCell`](uitableviewcell.md) object with the associated reuse identifier. This method always returns a valid cell.

#### Discussion

Call this method only from the [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) method of your table view data source object. This method returns an existing cell of the specified type, if one is available, or it creates and returns a new cell using the class or storyboard you provided earlier. Don’t call this method outside of your data source’s [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) method. If you need to create cells at other times, call [`dequeueReusableCell(withIdentifier:)`](uitableview/dequeuereusablecell(withidentifier:).md) instead.

> ❗ **Important**:  You must specify a cell with a matching identifier in your storyboard file. You may also register a class or nib file using the [`register(_:forCellReuseIdentifier:)`](uitableview/register(_:forcellreuseidentifier:)-5q6bo.md) or [`register(_:forCellReuseIdentifier:)`](uitableview/register(_:forcellreuseidentifier:)-3l3ct.md) method, but must do so before calling this method.

When creating new cells from your storyboard or nib file, this method loads the cell object and initializes it using its [`init(coder:)`](uitableview/init(coder:).md) method. When creating cells from a registered class, this method creates the cell and initializes it by calling its [`init(style:reuseIdentifier:)`](uitableviewcell/init(style:reuseidentifier:).md) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [`prepareForReuse()`](uitableviewcell/prepareforreuse().md) method instead.

## Parameters

- `identifier`: A string identifying the cell object to be reused. This parameter must not be  .
- `indexPath`: The index path specifying the location of the cell. Always specify the index path provided to you by your data source object. This method uses the index path to perform additional configuration based on the cell’s position in the table view.

## See Also

- [func register(UINib?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-5q6bo.md)
  Registers a nib object that contains a cell with the table view under a specified identifier.
- [func register(AnyClass?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-3l3ct.md)
  Registers a class to use in creating new table cells.
- [func dequeueReusableCell(withIdentifier: String) -> UITableViewCell?](uitableview/dequeuereusablecell(withidentifier:).md)
  Returns a reusable table-view cell object after locating it by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/dequeuereusablecell(withidentifier:for:))*