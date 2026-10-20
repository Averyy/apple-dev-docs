# nibBundle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s nib bundle if it exists.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
var nibBundle: Bundle? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSBundle * nibBundle;
```

## See Also

### Related Documentation
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Creates a view controller with the nib file in the specified bundle.
### Getting the storyboard and nib information
- [var storyboard: UIStoryboard?](./storyboard.md)
  The storyboard from which the view controller originated.
- [var nibName: String?](./nibname.md)
  The name of the view controller’s nib file, if one was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/nibbundle)*