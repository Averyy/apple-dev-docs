# preferredTransition

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that defines the transition animation when switching to the view controller.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var preferredTransition: UIViewController.Transition? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIViewControllerTransition * preferredTransition;
```

## Mentions

- [Enhancing your app with fluid transitions](../enhancing-your-app-with-fluid-transitions.md)

## Discussion

Use this property to define which transition the system uses when you present a view controller. For more information, see [Enhancing your app with fluid transitions](../enhancing-your-app-with-fluid-transitions.md).

## See Also

### Displaying view controllers
- [func show(UIViewController, sender: Any?)](../uinavigationcontroller/show%28_,sender%29.md)
  Presents the specified view controller in the navigation interface.
- [Enhancing your app with fluid transitions](../enhancing-your-app-with-fluid-transitions.md)
  Use the fluid zoom transition to provide a continuously interactive and responsive experience in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredtransition)*