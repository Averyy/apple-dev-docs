# pop()

**Framework**: Watchkit  
**Kind**: method

Pops the current interface controller from the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func pop()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

After pushing an interface controller onto the screen, use this method to remove it and display the previous interface controller again. The system animates the transition back to the previous interface controller asynchronously.

Always call this method from your WatchKit extension’s main thread.

## See Also

- [func pushController(withName: String, context: Any?)](wkinterfacecontroller/pushcontroller(withname:context:).md)
  Pushes a new interface controller onto the screen.
- [func popToRootController()](wkinterfacecontroller/poptorootcontroller.md)
  Pops all interface controllers except the app’s initial interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pop())*