# sectionIndexMinimumDisplayRowCount

**Framework**: UIKit  
**Kind**: property

The number of table rows at which to display the index list on the right edge of the table.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionIndexMinimumDisplayRowCount: Int { get set }
```

#### Discussion

This property is applicable only to table views in the [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) style. The default value is zero.

## See Also

- [var sectionIndexColor: UIColor?](uitableview/sectionindexcolor.md)
  The color to use for the table view’s index text.
- [var sectionIndexBackgroundColor: UIColor?](uitableview/sectionindexbackgroundcolor.md)
  The color to use for the background of the table view’s section index.
- [var sectionIndexTrackingBackgroundColor: UIColor?](uitableview/sectionindextrackingbackgroundcolor.md)
  The color to use for the table view’s index background area.
- [class let indexSearch: String](uitableview/indexsearch.md)
  A constant for adding the magnifying glass icon to the section index of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/sectionindexminimumdisplayrowcount)*