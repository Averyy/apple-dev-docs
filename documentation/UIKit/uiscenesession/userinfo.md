# userInfo

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Custom attributes that you can associate with the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [String : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * userInfo;
```

## See Also

### Getting additional session information
- [var stateRestorationActivity: NSUserActivity?](./staterestorationactivity.md)
  An activity object you can use to restore the previous contents of your scene’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/userinfo)*