# UIScrollView.IndicatorStyle

**Framework**: UIKit  
**Kind**: enum

Defines constants that represent the styles of the scroll indicators.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum IndicatorStyle
```

#### Overview

You use these constants to set the value of the [`indicatorStyle`](uiscrollview/indicatorstyle-swift.property.md) style.

## Topics

### Constants
- [UIScrollView.IndicatorStyle.default](uiscrollview/indicatorstyle-swift.enum/default.md)
  The default style of scroll indicator, which is black with a white border.
- [UIScrollView.IndicatorStyle.black](uiscrollview/indicatorstyle-swift.enum/black.md)
  A style of indicator which is black and smaller than the default style.
- [UIScrollView.IndicatorStyle.white](uiscrollview/indicatorstyle-swift.enum/white.md)
  A style of indicator is white and smaller than the default style.
### Initializers
- [init?(rawValue: Int)](uiscrollview/indicatorstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var indicatorStyle: UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.property.md)
  The style of the scroll indicators.
- [var showsHorizontalScrollIndicator: Bool](uiscrollview/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](uiscrollview/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](uiscrollview/horizontalscrollindicatorinsets.md)
  The horizontal distance the scroll indicators are inset from the edge of the scroll view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/indicatorstyle-swift.enum)*