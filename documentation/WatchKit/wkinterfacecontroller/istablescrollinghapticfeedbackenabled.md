# isTableScrollingHapticFeedbackEnabled

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var isTableScrollingHapticFeedbackEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isTableScrollingHapticFeedbackEnabled) BOOL tableScrollingHapticFeedbackEnabled;
```

#### Discussion

By default, this property is set to [`true`](../../Swift/true.md). In Apple Watch Series 4 and later, the watch provides haptic feedback as the user rotates the digital crown. When this property is [`true`](../../Swift/true.md), the watch provides haptic feedback whenever new rows scroll into view. However, if there are additional interface items at the top level, or if the table view contains a row that is taller than the screen, the crown falls back to providing linear feedback.

When this property is [`false`](../../Swift/false.md), the watch provides linear feedback. For example, you can use this property to force linear feedback when a table contains rows of varying heights, and the row-based feedback doesn’t feel right.

## See Also

### Related Documentation
- [var isHapticFeedbackEnabled: Bool](../wkcrownsequencer/ishapticfeedbackenabled.md)
  A Boolean value that determines whether the crown sequencer’s haptic feedback is enabled.
### Managing Scrolling
- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](./scroll%28to,at,animated%29.md)
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](../wkinterfacescrollposition.md)
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](./interfacedidscrolltotop%28%29.md)
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](./interfaceoffsetdidscrolltotop%28%29.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](./interfaceoffsetdidscrolltobottom%28%29.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled)*