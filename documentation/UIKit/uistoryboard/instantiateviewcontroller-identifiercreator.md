# instantiateViewController(identifier:creator:)

**Framework**: UIKit  
**Kind**: method

Creates the specified view controller from the storyboard and initializes it using your custom initialization code.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
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

In your block, create the view controller using your custom initialization method and return it. Your custom initialization method must accept an [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) parameter and must call the inherited [`init(coder:)`](uiviewcontroller/init(coder:).md) method at some point during its execution. Not doing so is a programmer error. After initializing the storyboard state, initialize your view controller’s custom properties.

## Parameters

- `identifier`: A string that uniquely identifies the view controller in the storyboard file. At design time, put this same string in the Storyboard ID attribute of your view controller in Interface Builder. This identifier is not a property of the view controller object itself. The storyboard uses it to locate the appropriate data for your view controller. If the specified identifier does not exist in the storyboard file, this method raises an exception.
- `creator`: A block containing your custom creation code for the view controller. Use this block to create the view controller, initialize it with the provided `coder` object and any custom information you require, and return the result. This block returns a new view controller object and takes the following parameter: - **coder**: The coder object containing the storyboard data to use when configuring the view controller. If you return `nil` from your block, this method creates the view controller using the default [`init(coder:)`](uiviewcontroller/init(coder:).md) method.

## See Also

- [func instantiateViewController(withIdentifier: String) -> UIViewController](uistoryboard/instantiateviewcontroller(withidentifier:).md)
  Creates the view controller with the specified identifier and initializes it with the data from the storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/instantiateviewcontroller(identifier:creator:))*