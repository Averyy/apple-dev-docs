# indexSearch

**Framework**: UIKit  
**Kind**: property

A constant for adding the magnifying glass icon to the section index of a table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class let indexSearch: String
```

#### Discussion

If the data source includes this constant string in the array of strings it returns in [`sectionIndexTitles(for:)`](uitableviewdatasource/sectionindextitles(for:).md), the section index displays a magnifying glass icon at the corresponding index location. This location should generally be the first title in the index.

## See Also

- [var sectionIndexMinimumDisplayRowCount: Int](uitableview/sectionindexminimumdisplayrowcount.md)
  The number of table rows at which to display the index list on the right edge of the table.
- [var sectionIndexColor: UIColor?](uitableview/sectionindexcolor.md)
  The color to use for the table view’s index text.
- [var sectionIndexBackgroundColor: UIColor?](uitableview/sectionindexbackgroundcolor.md)
  The color to use for the background of the table view’s section index.
- [var sectionIndexTrackingBackgroundColor: UIColor?](uitableview/sectionindextrackingbackgroundcolor.md)
  The color to use for the table view’s index background area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/indexsearch)*