# tableView(_:sectionForSectionIndexTitle:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the data source to return the index of the section having the given title and section title index.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, sectionForSectionIndexTitle title: String, at index: Int) -> Int
```

```objc
- (NSInteger) tableView:(UITableView *) tableView sectionForSectionIndexTitle:(NSString *) title atIndex:(NSInteger) index;
```

#### Return Value

An index number identifying a section.

#### Discussion

This method is passed the index number and title of an entry in the section index list and should return the index of the referenced section. To be clear, there are two index numbers in play here: an index to a section index title in the array returned by [`sectionIndexTitles(for:)`](./sectionindextitles%28for%29.md), and an index to a section of the table view; the former is passed in, and the latter is returned. You implement this method only for table views with a section index list — which can only be table views created in the plain style ([`UITableView.Style.plain`](../uitableview/style-swift.enum/plain.md)). Note that the array of section titles returned by [`sectionIndexTitles(for:)`](./sectionindextitles%28for%29.md) can have fewer items than the actual number of sections in the table view.

## Parameters

- `tableView`: The table-view object requesting this information.
- `title`: The title as displayed in the section index of `tableView`.
- `index`: An index number identifying a section title in the array returned by [`sectionIndexTitles(for:)`](./sectionindextitles%28for%29.md).

## See Also

### Related Documentation
- [func numberOfSections(in: UITableView) -> Int](./numberofsections%28in%29.md)
  Asks the data source to return the number of sections in the table view.
### Configuring an index
- [func sectionIndexTitles(for: UITableView) -> [String]?](./sectionindextitles%28for%29.md)
  Asks the data source to return the titles for the sections of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:sectionforsectionindextitle:at:))*