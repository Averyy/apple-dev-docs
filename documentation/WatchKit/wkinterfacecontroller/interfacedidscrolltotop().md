# interfaceDidScrollToTop()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
func interfaceDidScrollToTop()
```

```objc
- (void) interfaceDidScrollToTop;
```

## Discussion

The default implementation of this method does nothing. You can override it to take actions after the scroll-to-top action completes. If the interface is already scrolled to the top, this method may be called immediately.

## See Also

### Managing Scrolling
- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](./scroll%28to,at,animated%29.md)
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](../wkinterfacescrollposition.md)
  Onscreen scroll positions.
- [func interfaceOffsetDidScrollToTop()](./interfaceoffsetdidscrolltotop%28%29.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](./interfaceoffsetdidscrolltobottom%28%29.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](./istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop())*