# sectionIndexMinimumDisplayRowCount

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of table rows at which to display the index list on the right edge of the table.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionIndexMinimumDisplayRowCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger sectionIndexMinimumDisplayRowCount;
```

#### Discussion

This property is applicable only to table views in the [`UITableView.Style.plain`](./style-swift.enum/plain.md) style. The default value is zero.

## See Also

### Configuring the table index
- [var sectionIndexColor: UIColor?](./sectionindexcolor.md)
  The color to use for the table view’s index text.
- [var sectionIndexBackgroundColor: UIColor?](./sectionindexbackgroundcolor.md)
  The color to use for the background of the table view’s section index.
- [var sectionIndexTrackingBackgroundColor: UIColor?](./sectionindextrackingbackgroundcolor.md)
  The color to use for the table view’s index background area.
- [class let indexSearch: String](./indexsearch.md)
  A constant for adding the magnifying glass icon to the section index of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/sectionindexminimumdisplayrowcount)*