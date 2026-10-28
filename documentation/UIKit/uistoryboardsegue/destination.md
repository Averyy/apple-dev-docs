# destination

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The destination view controller for the segue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
var destination: UIViewController { get }
```

```objc
@property (nonatomic, readonly) UIViewController * destinationViewController;
```

## Discussion

This property contains the view controller whose contents should be displayed at the end of the segue.

## See Also

### Accessing the segue attributes
- [var source: UIViewController](./source.md)
  The source view controller for the segue.
- [var identifier: String?](./identifier.md)
  The identifier for the segue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/destination)*