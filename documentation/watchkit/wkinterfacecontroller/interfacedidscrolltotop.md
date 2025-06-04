# interfaceDidScrollToTop()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor func interfaceDidScrollToTop()
```

## Overview

The default implementation of this method does nothing. You can override it to take actions after the scroll-to-top action completes. If the interface is already scrolled to the top, this method may be called immediately.

## See Also

- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](scroll(to:at:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:)))
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition))
- [func interfaceOffsetDidScrollToTop()](interfaceoffsetdidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop()))
- [func interfaceOffsetDidScrollToBottom()](interfaceoffsetdidscrolltobottom().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom()))
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop())*