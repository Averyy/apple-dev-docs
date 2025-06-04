# isTableScrollingHapticFeedbackEnabled

**Framework**: WatchKit  
**Kind**: property

A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@MainActor
var isTableScrollingHapticFeedbackEnabled: Bool { get set }
```

#### Discussion

By default, this property is set to [`true`](https://developer.apple.com/documentation/swift/true). In Apple Watch Series 4 and later, the watch provides haptic feedback as the user rotates the digital crown. When this property is [`true`](https://developer.apple.com/documentation/swift/true), the watch provides haptic feedback whenever new rows scroll into view. However, if there are additional interface items at the top level, or if the table view contains a row that is taller than the screen, the crown falls back to providing linear feedback.

When this property is [`false`](https://developer.apple.com/documentation/swift/false), the watch provides linear feedback. For example, you can use this property to force linear feedback when a table contains rows of varying heights, and the row-based feedback doesn’t feel right.

## See Also

- [var isHapticFeedbackEnabled: Bool](wkcrownsequencer/ishapticfeedbackenabled.md)
  A Boolean value that determines whether the crown sequencer’s haptic feedback is enabled.
- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](wkinterfacecontroller/scroll(to:at:animated:).md)
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md)
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](wkinterfacecontroller/interfacedidscrolltotop.md)
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](wkinterfacecontroller/interfaceoffsetdidscrolltotop.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](wkinterfacecontroller/interfaceoffsetdidscrolltobottom.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled)*