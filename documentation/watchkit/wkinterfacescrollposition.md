# WKInterfaceScrollPosition

**Framework**: WatchKit  
**Kind**: enum

Onscreen scroll positions.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKInterfaceScrollPosition
```

## Topics

### Enumeration Cases
- [WKInterfaceScrollPosition.bottom](wkinterfacescrollposition/bottom.md)
  The bottom of the screen.
- [WKInterfaceScrollPosition.centeredVertically](wkinterfacescrollposition/centeredvertically.md)
  The vertical center of the screen.
- [WKInterfaceScrollPosition.top](wkinterfacescrollposition/top.md)
  The top of the screen.
### Initializers
- [init?(rawValue: Int)](wkinterfacescrollposition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](wkinterfacecontroller/scroll(to:at:animated:).md)
  Scrolls the specified object to the given position onscreen.
- [func interfaceDidScrollToTop()](wkinterfacecontroller/interfacedidscrolltotop.md)
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](wkinterfacecontroller/interfaceoffsetdidscrolltotop.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](wkinterfacecontroller/interfaceoffsetdidscrolltobottom.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](wkinterfacecontroller/istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition)*