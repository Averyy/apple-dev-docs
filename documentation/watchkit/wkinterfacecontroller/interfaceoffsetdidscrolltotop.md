# interfaceOffsetDidScrollToTop()

**Framework**: WatchKit  
**Kind**: method

Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
func interfaceOffsetDidScrollToTop()
```

#### Discussion

The default implementation of this method does nothing. You can override this method to take actions when the user scrolls to the top of the interface.

## See Also

- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](scroll(to:at:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:)))
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition))
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](interfacedidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop()))
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](interfaceoffsetdidscrolltobottom().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom()))
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop())*