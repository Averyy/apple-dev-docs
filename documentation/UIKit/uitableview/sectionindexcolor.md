# sectionIndexColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color to use for the table view’s index text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionIndexColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * sectionIndexColor;
```

## Discussion

Table views can display an index along the side of the view, making it easier for users to navigate the contents of the table quickly. This property specifies the color to use for text displayed in this region. A value of `nil` represents the default color.

## See Also

### Configuring the table index
- [var sectionIndexMinimumDisplayRowCount: Int](./sectionindexminimumdisplayrowcount.md)
  The number of table rows at which to display the index list on the right edge of the table.
- [var sectionIndexBackgroundColor: UIColor?](./sectionindexbackgroundcolor.md)
  The color to use for the background of the table view’s section index.
- [var sectionIndexTrackingBackgroundColor: UIColor?](./sectionindextrackingbackgroundcolor.md)
  The color to use for the table view’s index background area.
- [class let indexSearch: String](./indexsearch.md)
  A constant for adding the magnifying glass icon to the section index of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/sectionindexcolor)*