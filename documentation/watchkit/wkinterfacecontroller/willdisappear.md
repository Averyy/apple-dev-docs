# willDisappear()

**Framework**: WatchKit  
**Kind**: method

Tells the interface controller that its view is now offscreen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func willDisappear()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

WatchKit calls this method shortly before removing your interface controller’s content from the screen. Use this method to stop animations or perform other interface-related tasks prior to deactivation.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

## See Also

- [func willActivate()](wkinterfacecontroller/willactivate.md)
  Tells the interface controller that the system is about to activate its view.
- [func didDeactivate()](wkinterfacecontroller/diddeactivate.md)
  Tells the interface controller that its view is no longer active.
- [func didAppear()](wkinterfacecontroller/didappear.md)
  Tells the interface controller that its view is now onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear())*