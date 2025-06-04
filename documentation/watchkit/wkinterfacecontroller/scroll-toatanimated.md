# scroll(to:at:animated:)

**Framework**: WatchKit  
**Kind**: method

Scrolls the specified object to the given position onscreen.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
func scroll(to object: WKInterfaceObject, at scrollPosition: WKInterfaceScrollPosition, animated: Bool)
```

## Parameters

- `object`: The interface object to scroll to.
- `scrollPosition`: The specified object’s desired position on the screen.
- `animated`: A Boolean value that determines whether the scroll action is animated.

## See Also

- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition))
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](interfacedidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop()))
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](interfaceoffsetdidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop()))
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](interfaceoffsetdidscrolltobottom().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom()))
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:))*