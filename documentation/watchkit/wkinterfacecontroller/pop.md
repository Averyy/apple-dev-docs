# pop()

**Framework**: Watchkit  
**Kind**: method

Pops the current interface controller from the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func pop()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

After pushing an interface controller onto the screen, use this method to remove it and display the previous interface controller again. The system animates the transition back to the previous interface controller asynchronously.

Always call this method from your WatchKit extension’s main thread.

## See Also

- [func pushController(withName: String, context: Any?)](pushcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pushcontroller(withname:context:)))
- [func popToRootController()](poptorootcontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/poptorootcontroller()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pop())*