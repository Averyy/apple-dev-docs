# register(_:forCellReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a nib object that contains a cell with the table view under a specified identifier.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func register(_ nib: UINib?, forCellReuseIdentifier identifier: String)
```

#### Discussion

Before dequeueing any cells, call this method or the [`register(_:forCellReuseIdentifier:)`](uitableview/register(_:forcellreuseidentifier:)-3l3ct.md) method to tell the table view how to create new cells. If a cell of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the nib you specify in the `nib` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the nib from the specified reuse identifier.

## Parameters

- `nib`: A nib object that specifies the nib file to use to create the cell.
- `identifier`: The reuse identifier for the cell. This parameter must not be   and must not be an empty string.

## See Also

- [func tableView(UITableView, cellForRowAt: IndexPath) -> UITableViewCell](uitableviewdatasource/tableview(_:cellforrowat:).md)
  Asks the data source for a cell to insert in a particular location of the table view.
- [func register(AnyClass?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-3l3ct.md)
  Registers a class to use in creating new table cells.
- [func dequeueReusableCell(withIdentifier: String, for: IndexPath) -> UITableViewCell](uitableview/dequeuereusablecell(withidentifier:for:).md)
  Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.
- [func dequeueReusableCell(withIdentifier: String) -> UITableViewCell?](uitableview/dequeuereusablecell(withidentifier:).md)
  Returns a reusable table-view cell object after locating it by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/register(_:forcellreuseidentifier:)-5q6bo)*