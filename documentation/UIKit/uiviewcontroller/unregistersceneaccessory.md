# unregisterSceneAccessory(_:)

**Framework**: UIKit  
**Kind**: method

Unregisters a scene accessory with the specified registration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func unregisterSceneAccessory(_ registration: UISceneAccessoryRegistration)
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Discussion

If the scene accessory associated to this registration is currently being presented, it will be dismissed.

## See Also

- [func registerSceneAccessory(UISceneAccessory) -> UISceneAccessoryRegistration](uiviewcontroller/registersceneaccessory(_:).md)
  Registers a new scene accessory configuration associated with this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/unregistersceneaccessory(_:))*