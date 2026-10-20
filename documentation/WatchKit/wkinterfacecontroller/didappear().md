# didAppear()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the interface controller that its view is now onscreen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func didAppear()
```

```objc
- (void) didAppear;
```

## Mentions

- [Navigating Between Scenes](../navigating-between-scenes.md)
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)

#### Discussion

WatchKit calls this method shortly after the interface controller’s contents appear onscreen. Use this method to configure animations or other interface-related tasks.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

## See Also

### Responding to activation and appearance events
- [func willActivate()](./willactivate%28%29.md)
  Tells the interface controller that the system is about to activate its view.
- [func didDeactivate()](./diddeactivate%28%29.md)
  Tells the interface controller that its view is no longer active.
- [func willDisappear()](./willdisappear%28%29.md)
  Tells the interface controller that its view is now offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear())*