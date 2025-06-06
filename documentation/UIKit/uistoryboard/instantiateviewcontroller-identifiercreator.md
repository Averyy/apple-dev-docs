# instantiateViewController(identifier:creator:)

**Framework**: UIKit  
**Kind**: method

Creates the specified view controller from the storyboard and initializes it using your custom initialization code.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func instantiateViewController<ViewController>(identifier: String, creator: ((NSCoder) -> ViewController?)? = nil) -> ViewController where ViewController : UIViewController
```

#### Return Value

The view controller corresponding to the specified identifier string. If no view controller has the given identifier, this method throws an exception.

#### Discussion

Use this method to create a view controller object to present programmatically. Each time you call this method, it creates a new instance of the view controller using the block you provide.

In your block, create the view controller using your custom initialization method and return it. Your custom initialization method must accept an [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) parameter and must call the inherited [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) method at some point during its execution. Not doing so is a programmer error. After initializing the storyboard state, initialize your view controller’s custom properties.

## Parameters

- `identifier`: If the specified identifier does not exist in the storyboard file, this method raises an exception.
- `creator`: If you return   from your block, this method creates the view controller using the default   method.

## See Also

- [func instantiateViewController(withIdentifier: String) -> UIViewController](uistoryboard/instantiateviewcontroller(withidentifier:).md)
  Creates the view controller with the specified identifier and initializes it with the data from the storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/instantiateviewcontroller(identifier:creator:))*