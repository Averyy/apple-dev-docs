# WKInterfaceScrollPosition

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Onscreen scroll positions.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKInterfaceScrollPosition
```

```c
enum WKInterfaceScrollPosition : NSInteger;
```

## Topics

### Enumeration Cases
- [WKInterfaceScrollPosition.bottom](./wkinterfacescrollposition/bottom.md)
  The bottom of the screen.
- [WKInterfaceScrollPosition.centeredVertically](./wkinterfacescrollposition/centeredvertically.md)
  The vertical center of the screen.
- [WKInterfaceScrollPosition.top](./wkinterfacescrollposition/top.md)
  The top of the screen.
### Initializers
- [init?(rawValue: Int)](./wkinterfacescrollposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Scrolling
- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](./wkinterfacecontroller/scroll%28to,at,animated%29.md)
  Scrolls the specified object to the given position onscreen.
- [func interfaceDidScrollToTop()](./wkinterfacecontroller/interfacedidscrolltotop%28%29.md)
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](./wkinterfacecontroller/interfaceoffsetdidscrolltotop%28%29.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](./wkinterfacecontroller/interfaceoffsetdidscrolltobottom%28%29.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](./wkinterfacecontroller/istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition)*