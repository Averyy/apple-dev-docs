# popToRootController()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Pops all interface controllers except the app’s initial interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func popToRootController()
```

```objc
- (void) popToRootController;
```

#### Discussion

Use this method to return your interface to its initial configuration. You might do this so that you can reset your navigation hierarchy to its initial state before pushing one or more different interface controllers onto the navigation stack.

Always call this method from your WatchKit extension’s main thread.

## See Also

### Implementing a navigation interface
- [func pushController(withName: String, context: Any?)](./pushcontroller%28withname,context%29.md)
  Pushes a new interface controller onto the screen.
- [func pop()](./pop%28%29.md)
  Pops the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/poptorootcontroller())*