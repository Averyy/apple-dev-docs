# scroll(to:at:animated:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the specified object to the given position onscreen.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
func scroll(to object: WKInterfaceObject, at scrollPosition: WKInterfaceScrollPosition, animated: Bool)
```

```objc
- (void) scrollToObject:(WKInterfaceObject *) object atScrollPosition:(WKInterfaceScrollPosition) scrollPosition animated:(BOOL) animated;
```

## Parameters

- `object`: The interface object to scroll to.
- `scrollPosition`: The specified object’s desired position on the screen.
- `animated`: A Boolean value that determines whether the scroll action is animated.

## See Also

### Managing Scrolling
- [enum WKInterfaceScrollPosition](../wkinterfacescrollposition.md)
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](./interfacedidscrolltotop%28%29.md)
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](./interfaceoffsetdidscrolltotop%28%29.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](./interfaceoffsetdidscrolltobottom%28%29.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](./istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:))*