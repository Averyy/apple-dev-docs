# verticalScrollIndicatorInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The vertical distance the scroll indicators are inset from the edge of the scroll view.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 13.1+
- tvOS 11.1+
- visionOS 1.0+

## Declaration

```swift
var verticalScrollIndicatorInsets: UIEdgeInsets { get set }
```

```objc
@property (nonatomic) UIEdgeInsets verticalScrollIndicatorInsets;
```

## Discussion

The default value is [`zero`](../uiedgeinsets/zero.md).

## See Also

### Managing the scroll indicator and refresh control
- [var indicatorStyle: UIScrollView.IndicatorStyle](./indicatorstyle-swift.property.md)
  The style of the scroll indicators.
- [UIScrollView.IndicatorStyle](./indicatorstyle-swift.enum.md)
  Defines constants that represent the styles of the scroll indicators.
- [var showsHorizontalScrollIndicator: Bool](./showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](./showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](./horizontalscrollindicatorinsets.md)
  The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [var automaticallyAdjustsScrollIndicatorInsets: Bool](./automaticallyadjustsscrollindicatorinsets.md)
  A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [func flashScrollIndicators()](./flashscrollindicators%28%29.md)
  Displays the scroll indicators momentarily.
- [func withScrollIndicatorsShown(forContentOffsetChanges: () -> Void)](./withscrollindicatorsshown%28forcontentoffsetchanges%29.md)
  Displays the scroll indicators during updates to the scroll view’s content offset.
- [var refreshControl: UIRefreshControl?](./refreshcontrol.md)
  The refresh control associated with the scroll view.
- [class UIRefreshControl](../uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/verticalscrollindicatorinsets)*