# init()

**Framework**: Watchkit  
**Kind**: init

Returns an initialized interface controller object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
init()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Return Value

The initialized interface controller object.

#### Discussion

This method is the designated initializer for interface controller objects. Override this method as needed and use it to prepare your interface controller for use. In your implementation, call `super` first and then perform your own initialization.

> ❗ **Important**:  If the interface controller has outlets connected to objects in your storyboard file, the super implementation creates those interface objects and assigns them to your declared properties; however, the system cannot guarantee that these objects are ready for use yet. Instead, defer any code that interacts with the user interface to the [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method.

 If the interface controller has outlets connected to objects in your storyboard file, the super implementation creates those interface objects and assigns them to your declared properties; however, the system cannot guarantee that these objects are ready for use yet. Instead, defer any code that interacts with the user interface to the [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method.

In a page-based interface, all interface controllers are initialized up front but only the first one is displayed initially. The others are not displayed until the user navigates to the corresponding page. If your interface controller displays information that can change between initialization and the display of the page, use the [`willActivate()`](wkinterfacecontroller/willactivate().md) method to refresh your content. Use the [`didAppear()`](wkinterfacecontroller/didappear().md) method to start animations or perform tasks that should wait until the interface appears onscreen.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func didAppear()](wkinterfacecontroller/didappear.md)
  Tells the interface controller that its view is now onscreen.
- [func willActivate()](wkinterfacecontroller/willactivate.md)
  Tells the interface controller that the system is about to activate its view.
- [func awake(withContext: Any?)](wkinterfacecontroller/awake(withcontext:).md)
  Initializes the interface controller with the specified context data.
- [func setTitle(String?)](wkinterfacecontroller/settitle(_:).md)
  Sets the title of the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/init())*