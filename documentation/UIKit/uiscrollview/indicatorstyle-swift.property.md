# indicatorStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of the scroll indicators.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var indicatorStyle: UIScrollView.IndicatorStyle { get set }
```

```objc
@property (nonatomic) UIScrollViewIndicatorStyle indicatorStyle;
```

#### Discussion

The default style is [`UIScrollView.IndicatorStyle.default`](./indicatorstyle-swift.enum/default.md). See [`UIScrollView.IndicatorStyle`](./indicatorstyle-swift.enum.md) for descriptions of these constants.

## See Also

### Managing the scroll indicator and refresh control
- [UIScrollView.IndicatorStyle](./indicatorstyle-swift.enum.md)
  Defines constants that represent the styles of the scroll indicators.
- [var showsHorizontalScrollIndicator: Bool](./showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](./showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](./horizontalscrollindicatorinsets.md)
  The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [var verticalScrollIndicatorInsets: UIEdgeInsets](./verticalscrollindicatorinsets.md)
  The vertical distance the scroll indicators are inset from the edge of the scroll view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/indicatorstyle-swift.property)*