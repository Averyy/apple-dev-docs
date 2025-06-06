# horizontalScrollIndicatorInsets

**Framework**: UIKit  
**Kind**: property

The horizontal distance the scroll indicators are inset from the edge of the scroll view.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 13.1+
- tvOS 11.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var horizontalScrollIndicatorInsets: UIEdgeInsets { get set }
```

#### Discussion

The default value is [`zero`](uiedgeinsets/zero.md).

## See Also

- [var indicatorStyle: UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.property.md)
  The style of the scroll indicators.
- [UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.enum.md)
  Defines constants that represent the styles of the scroll indicators.
- [var showsHorizontalScrollIndicator: Bool](uiscrollview/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](uiscrollview/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var verticalScrollIndicatorInsets: UIEdgeInsets](uiscrollview/verticalscrollindicatorinsets.md)
  The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [var automaticallyAdjustsScrollIndicatorInsets: Bool](uiscrollview/automaticallyadjustsscrollindicatorinsets.md)
  A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [func flashScrollIndicators()](uiscrollview/flashscrollindicators.md)
  Displays the scroll indicators momentarily.
- [func withScrollIndicatorsShown(forContentOffsetChanges: () -> Void)](uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges:).md)
  Displays the scroll indicators during updates to the scroll view’s content offset.
- [var refreshControl: UIRefreshControl?](uiscrollview/refreshcontrol.md)
  The refresh control associated with the scroll view.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/horizontalscrollindicatorinsets)*