# instantiateViewController(withIdentifier:)

**Framework**: UIKit  
**Kind**: method

Creates the view controller with the specified identifier and initializes it with the data from the storyboard.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func instantiateViewController(withIdentifier identifier: String) -> UIViewController
```

#### Return Value

The view controller corresponding to the specified identifier string. If no view controller has the given identifier, this method throws an exception.

#### Discussion

Use this method to create a view controller object to present programmatically. Each time you call this method, it creates a new instance of the view controller using the [`init(coder:)`](uiviewcontroller/init(coder:).md) method.

## Parameters

- `identifier`: If the specified identifier does not exist in the storyboard file, this method raises an exception.

## See Also

- [func instantiateViewController<ViewController>(identifier: String, creator: ((NSCoder) -> ViewController?)?) -> ViewController](uistoryboard/instantiateviewcontroller(identifier:creator:).md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/instantiateviewcontroller(withidentifier:))*