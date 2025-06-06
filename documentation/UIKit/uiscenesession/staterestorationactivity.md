# stateRestorationActivity

**Framework**: UIKit  
**Kind**: property

An activity object you can use to restore the previous contents of your scene’s interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var stateRestorationActivity: NSUserActivity? { get set }
```

#### Discussion

Before disconnecting a scene, the system asks your delegate for an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object containing state information for that scene. If you provide that object, the system puts a copy of it in this property. Use the information in the user activity object to restore the scene to its previous state.

The system encrypts your app’s state restoration on disk. If the file is unavailable at scene-connection time, perhaps because the device is still locked, the initial value in this property is `nil`. When the data becomes available, the system updates the value accordingly.

## See Also

- [var userInfo: [String : Any]?](uiscenesession/userinfo.md)
  Custom attributes that you can associate with the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/staterestorationactivity)*