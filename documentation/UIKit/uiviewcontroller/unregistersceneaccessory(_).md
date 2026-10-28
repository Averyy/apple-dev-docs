# unregisterSceneAccessory(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Unregisters a scene accessory with the specified registration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func unregisterSceneAccessory(_ registration: UISceneAccessoryRegistration)
```

```objc
- (void) unregisterSceneAccessory:(UISceneAccessoryRegistration *) registration;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

## Discussion

If the scene accessory associated to this registration is currently being presented, it will be dismissed.

## See Also

### Registering scene accessories
- [func registerSceneAccessory(UISceneAccessory) -> UISceneAccessoryRegistration](./registersceneaccessory%28_%29.md)
  Registers a new scene accessory configuration associated with this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/unregistersceneaccessory(_:))*