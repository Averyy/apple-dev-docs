# interfaceOffsetDidScrollToBottom()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor func interfaceOffsetDidScrollToBottom()
```

## Overview

The default implementation of this method does nothing. You can override this method to take actions when the user scrolls to the bottom of the interface.

## See Also

- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](scroll(to:at:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:)))
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition))
- [func interfaceDidScrollToTop()](interfacedidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop()))
- [func interfaceOffsetDidScrollToTop()](interfaceoffsetdidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop()))
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom())*