# instantiateViewController(withIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates the view controller with the specified identifier and initializes it with the data from the storyboard.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func instantiateViewController(withIdentifier identifier: String) -> UIViewController
```

```objc
- (UIViewController *) instantiateViewControllerWithIdentifier:(NSString *) identifier;
```

#### Return Value

The view controller corresponding to the specified identifier string. If no view controller has the given identifier, this method throws an exception.

#### Discussion

Use this method to create a view controller object to present programmatically. Each time you call this method, it creates a new instance of the view controller using the [`init(coder:)`](../uiviewcontroller/init%28coder%29.md) method.

## Parameters

- `identifier`: An identifier string that uniquely identifies the view controller in the storyboard file. At design time, put this same string in the Storyboard ID attribute of your view controller in Interface Builder. This identifier is not a property of the view controller object itself. The storyboard uses it to locate the appropriate data for your view controller.

  If the specified identifier does not exist in the storyboard file, this method raises an exception.

## See Also

### Instantiating Storyboard View Controllers
- [func instantiateViewController<ViewController>(identifier: String, creator: ((NSCoder) -> ViewController?)?) -> ViewController](./instantiateviewcontroller%28identifier,creator%29.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/instantiateviewcontroller(withidentifier:))*