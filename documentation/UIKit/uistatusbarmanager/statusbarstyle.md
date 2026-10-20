# statusBarStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current appearance of the status bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var statusBarStyle: UIStatusBarStyle { get }
```

```objc
@property (nonatomic, readonly) UIStatusBarStyle statusBarStyle;
```

#### Discussion

To customize the status bar’s style for each of your view controllers, override their [`preferredStatusBarStyle`](../uiviewcontroller/preferredstatusbarstyle.md) property.

## See Also

### Getting the status bar configuration
- [var isStatusBarHidden: Bool](./isstatusbarhidden.md)
  A Boolean value that indicates whether the status bar is currently hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistatusbarmanager/statusbarstyle)*