# isStatusBarHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the status bar is currently hidden.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isStatusBarHidden: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isStatusBarHidden) BOOL statusBarHidden;
```

#### Discussion

To customize the status bar’s visibility for each of your view controllers, override your view controller’s [`prefersStatusBarHidden`](../uiviewcontroller/prefersstatusbarhidden.md) property.

## See Also

### Getting the status bar configuration
- [var statusBarStyle: UIStatusBarStyle](./statusbarstyle.md)
  The current appearance of the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistatusbarmanager/isstatusbarhidden)*