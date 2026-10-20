# registerSceneAccessory(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers a new scene accessory configuration associated with this view controller.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func registerSceneAccessory(_ accessory: UISceneAccessory) -> UISceneAccessoryRegistration
```

```objc
- (UISceneAccessoryRegistration *) registerSceneAccessory:(UISceneAccessory *) accessory;
```

#### Return Value

A registration object which can be used to monitor changes for the scene accessory or unregister it.

#### Discussion

The delegate type that the configuration defines will be called for all lifecycle events associated with the scene accessory.

## Parameters

- `accessory`: A configuration which defines system functionality necessary to present the scene accessory.

## See Also

### Registering scene accessories
- [func unregisterSceneAccessory(UISceneAccessoryRegistration)](./unregistersceneaccessory%28_%29.md)
  Unregisters a scene accessory with the specified registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/registersceneaccessory(_:))*