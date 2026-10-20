# sectionIndexBackgroundColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color to use for the background of the table view’s section index.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionIndexBackgroundColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * sectionIndexBackgroundColor;
```

#### Discussion

Table views can display an index along the side of the view, making it easier for users to navigate the contents of the table quickly. This property specifies the color to use for the background of the index. The table view applies this color when the user isn’t touching the index. A value of `nil` represents the default color.

## See Also

### Configuring the table index
- [var sectionIndexMinimumDisplayRowCount: Int](./sectionindexminimumdisplayrowcount.md)
  The number of table rows at which to display the index list on the right edge of the table.
- [var sectionIndexColor: UIColor?](./sectionindexcolor.md)
  The color to use for the table view’s index text.
- [var sectionIndexTrackingBackgroundColor: UIColor?](./sectionindextrackingbackgroundcolor.md)
  The color to use for the table view’s index background area.
- [class let indexSearch: String](./indexsearch.md)
  A constant for adding the magnifying glass icon to the section index of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/sectionindexbackgroundcolor)*