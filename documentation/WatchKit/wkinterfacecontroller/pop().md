# pop()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Pops the current interface controller from the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func pop()
```

```objc
- (void) popController;
```

## Mentions

- [Navigating Between Scenes](../navigating-between-scenes.md)

## Discussion

After pushing an interface controller onto the screen, use this method to remove it and display the previous interface controller again. The system animates the transition back to the previous interface controller asynchronously.

Always call this method from your WatchKit extension’s main thread.

## See Also

### Implementing a navigation interface
- [func pushController(withName: String, context: Any?)](./pushcontroller%28withname,context%29.md)
  Pushes a new interface controller onto the screen.
- [func popToRootController()](./poptorootcontroller%28%29.md)
  Pops all interface controllers except the app’s initial interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pop())*