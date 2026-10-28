# storyboard

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The storyboard from which the view controller originated.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
var storyboard: UIStoryboard? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIStoryboard * storyboard;
```

## Discussion

If the view controller was not instantiated from a storyboard, this property is `nil`.

## See Also

### Getting the storyboard and nib information
- [var nibName: String?](./nibname.md)
  The name of the view controller’s nib file, if one was specified.
- [var nibBundle: Bundle?](./nibbundle.md)
  The view controller’s nib bundle if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/storyboard)*