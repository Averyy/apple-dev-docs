# didAppear()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that its view is now onscreen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func didAppear()
```

## Mentions

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

WatchKit calls this method shortly after the interface controller’s contents appear onscreen. Use this method to configure animations or other interface-related tasks.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

## See Also

- [func willActivate()](wkinterfacecontroller/willactivate.md)
  Tells the interface controller that the system is about to activate its view.
- [func didDeactivate()](wkinterfacecontroller/diddeactivate.md)
  Tells the interface controller that its view is no longer active.
- [func willDisappear()](wkinterfacecontroller/willdisappear.md)
  Tells the interface controller that its view is now offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear())*