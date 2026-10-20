# UIScrollView.IndicatorStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Defines constants that represent the styles of the scroll indicators.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum IndicatorStyle
```

```c
enum UIScrollViewIndicatorStyle : NSInteger;
```

#### Overview

You use these constants to set the value of the [`indicatorStyle`](./indicatorstyle-swift.property.md) style.

## Topics

### Constants
- [UIScrollView.IndicatorStyle.default](./indicatorstyle-swift.enum/default.md)
  The default style of scroll indicator, which is black with a white border.
- [UIScrollView.IndicatorStyle.black](./indicatorstyle-swift.enum/black.md)
  A style of indicator which is black and smaller than the default style.
- [UIScrollView.IndicatorStyle.white](./indicatorstyle-swift.enum/white.md)
  A style of indicator is white and smaller than the default style.
### Initializers
- [init?(rawValue: Int)](./indicatorstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the scroll indicator and refresh control
- [var indicatorStyle: UIScrollView.IndicatorStyle](./indicatorstyle-swift.property.md)
  The style of the scroll indicators.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/indicatorstyle-swift.enum)*