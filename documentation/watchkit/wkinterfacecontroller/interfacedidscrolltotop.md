# interfaceDidScrollToTop()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
func interfaceDidScrollToTop()
```

#### Discussion

The default implementation of this method does nothing. You can override it to take actions after the scroll-to-top action completes. If the interface is already scrolled to the top, this method may be called immediately.

## See Also

- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](wkinterfacecontroller/scroll(to:at:animated:).md)
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md)
  Onscreen scroll positions.
- [func interfaceOffsetDidScrollToTop()](wkinterfacecontroller/interfaceoffsetdidscrolltotop.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](wkinterfacecontroller/interfaceoffsetdidscrolltobottom.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](wkinterfacecontroller/istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop())*