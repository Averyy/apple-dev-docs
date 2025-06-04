# scroll(to:at:animated:)

**Framework**: Watchkit  
**Kind**: method

Scrolls the specified object to the given position onscreen.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor func scroll(to object: WKInterfaceObject, at scrollPosition: WKInterfaceScrollPosition, animated: Bool)
```

## Parameters

- `object`: The interface object to scroll to.
- `scrollPosition`: The specified object’s desired position on the screen.
- `animated`: A Boolean value that determines whether the scroll action is animated.

## See Also

- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition))
- [func interfaceDidScrollToTop()](interfacedidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop()))
- [func interfaceOffsetDidScrollToTop()](interfaceoffsetdidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop()))
- [func interfaceOffsetDidScrollToBottom()](interfaceoffsetdidscrolltobottom().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom()))
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:))*