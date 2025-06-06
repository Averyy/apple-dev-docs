# automaticallyAdjustsScrollIndicatorInsets

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyAdjustsScrollIndicatorInsets: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var indicatorStyle: UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.property.md)
  The style of the scroll indicators.
- [UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.enum.md)
  Defines constants that represent the styles of the scroll indicators.
- [var showsHorizontalScrollIndicator: Bool](uiscrollview/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](uiscrollview/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](uiscrollview/horizontalscrollindicatorinsets.md)
  The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [var verticalScrollIndicatorInsets: UIEdgeInsets](uiscrollview/verticalscrollindicatorinsets.md)
  The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [func flashScrollIndicators()](uiscrollview/flashscrollindicators.md)
  Displays the scroll indicators momentarily.
- [func withScrollIndicatorsShown(forContentOffsetChanges: () -> Void)](uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges:).md)
  Displays the scroll indicators during updates to the scroll view’s content offset.
- [var refreshControl: UIRefreshControl?](uiscrollview/refreshcontrol.md)
  The refresh control associated with the scroll view.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/automaticallyadjustsscrollindicatorinsets)*