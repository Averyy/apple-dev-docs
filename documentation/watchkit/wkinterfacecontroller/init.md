# init()

**Framework**: Watchkit  
**Kind**: init

Returns an initialized interface controller object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor init()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

The initialized interface controller object.

## Discussion

This method is the designated initializer for interface controller objects. Override this method as needed and use it to prepare your interface controller for use. In your implementation, call `super` first and then perform your own initialization.

> ❗ **Important**:  If the interface controller has outlets connected to objects in your storyboard file, the super implementation creates those interface objects and assigns them to your declared properties; however, the system cannot guarantee that these objects are ready for use yet. Instead, defer any code that interacts with the user interface to the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method.

 If the interface controller has outlets connected to objects in your storyboard file, the super implementation creates those interface objects and assigns them to your declared properties; however, the system cannot guarantee that these objects are ready for use yet. Instead, defer any code that interacts with the user interface to the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method.

In a page-based interface, all interface controllers are initialized up front but only the first one is displayed initially. The others are not displayed until the user navigates to the corresponding page. If your interface controller displays information that can change between initialization and the display of the page, use the [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method to refresh your content. Use the [`didAppear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()) method to start animations or perform tasks that should wait until the interface appears onscreen.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func didAppear()](didappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()))
- [func willActivate()](willactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()))
- [func awake(withContext: Any?)](awake(withcontext:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)))
- [func setTitle(String?)](settitle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/settitle(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/init())*