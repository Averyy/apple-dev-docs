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
- [WKInterfaceScrollPosition.bottom](bottom.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition/bottom))
  The bottom of the screen.
- [WKInterfaceScrollPosition.centeredVertically](centeredvertically.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition/centeredvertically))
  The vertical center of the screen.
- [WKInterfaceScrollPosition.top](top.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition/top))
  The top of the screen.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](scroll(to:at:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:)))
  Scrolls the specified object to the given position onscreen.
- [func interfaceDidScrollToTop()](interfacedidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop()))
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](interfaceoffsetdidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop()))
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](interfaceoffsetdidscrolltobottom().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom()))
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition)*