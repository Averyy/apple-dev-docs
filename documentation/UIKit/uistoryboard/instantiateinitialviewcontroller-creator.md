# instantiateInitialViewController(creator:)

**Framework**: UIKit  
**Kind**: method

Creates the initial view controller from the storyboard and initializes it using your custom initialization code.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func instantiateInitialViewController<ViewController>(creator: ((NSCoder) -> ViewController?)? = nil) -> ViewController? where ViewController : UIViewController
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Return Value

The initial view controller in the storyboard.

#### Discussion

Every storyboard file has an initial view controller that represents the default view controller to create. Typically, you use the initial view controller as the root view controller for a window. However, you can also instantiate the initial view controller when transitioning to content in a new storyboard file.

This method creates a new instance of the initial view controller using the custom block you provide. In your block, create the view controller using your custom initialization method and return it. Your custom initialization method must accept an [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) parameter and must call the inherited [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) method at some point during its execution. Not doing so is a programmer error.

## Parameters

- `creator`: If you return   from your block, this method creates the view controller using the default   method.

## See Also

- [func instantiateInitialViewController() -> UIViewController?](uistoryboard/instantiateinitialviewcontroller.md)
  Creates the initial view controller and initializes it with the data from the storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/instantiateinitialviewcontroller(creator:))*