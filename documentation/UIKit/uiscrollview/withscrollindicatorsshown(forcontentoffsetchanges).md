# withScrollIndicatorsShown(forContentOffsetChanges:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays the scroll indicators during updates to the scroll view’s content offset.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func withScrollIndicatorsShown(forContentOffsetChanges changes: () -> Void)
```

```objc
- (void) withScrollIndicatorsShownForContentOffsetChanges:(void (^)()) changes;
```

#### Discussion

The scroll view displays the scroll indicator for an axis if the content offset changes along that axis; otherwise, the scroll indicator for that axis remains hidden. For example, if you update the content offset horizontally in the `changes` block, the scroll view shows the horizontal scroll indicator but not the vertical scroll indicator.

If you animate changes to the content offset in the `changes` block, the scroll view displays its scroll indicators in their original locations, animates them to the destination locations, then fades them out. Otherwise, the scroll view displays its scroll indicators in the destination locations, then fades them out.

## Parameters

- `changes`: A block that changes the scroll view’s content offset.

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
- [var verticalScrollIndicatorInsets: UIEdgeInsets](./verticalscrollindicatorinsets.md)
  The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [var automaticallyAdjustsScrollIndicatorInsets: Bool](./automaticallyadjustsscrollindicatorinsets.md)
  A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [func flashScrollIndicators()](./flashscrollindicators%28%29.md)
  Displays the scroll indicators momentarily.
- [var refreshControl: UIRefreshControl?](./refreshcontrol.md)
  The refresh control associated with the scroll view.
- [class UIRefreshControl](../uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges:))*