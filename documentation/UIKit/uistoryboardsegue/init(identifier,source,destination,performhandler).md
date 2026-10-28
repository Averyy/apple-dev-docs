# init(identifier:source:destination:performHandler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a segue that calls a block to perform the segue transition.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
convenience init(identifier: String?, source: UIViewController, destination: UIViewController, performHandler: @escaping () -> Void)
```

```objc
+ (instancetype) segueWithIdentifier:(NSString *) identifier source:(UIViewController *) source destination:(UIViewController *) destination performHandler:(void (^)()) performHandler;
```

## Return Value

An initialized segue object.

## Discussion

You use this method as an alternative to creating a subclass. Your perform handler should do all of the work necessary to transition between the source and destination view controllers, exactly as if you were implementing the [`perform()`](./perform%28%29.md) method.

## Parameters

- `identifier`: The identifier you want to associate with this particular instance of the segue. You can use this identifier to differentiate one type of segue from another at runtime.
- `source`: The view controller visible at the start of the segue.
- `destination`: The view controller to display after the completion of the segue.
- `performHandler`: A block to be called when the segue’s [`perform()`](./perform%28%29.md) method is called.

## See Also

### Related Documentation
- [func perform()](./perform%28%29.md)
  Performs the visual transition for the segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/init(identifier:source:destination:performhandler:))*