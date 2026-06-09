# registerSceneAccessory(_:)

**Framework**: UIKit  
**Kind**: method

Registers a new scene accessory configuration associated with this view controller.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func registerSceneAccessory(_ accessory: UISceneAccessory) -> UISceneAccessoryRegistration
```

#### Return Value

A registration object which can be used to monitor changes for the scene accessory or unregister it.

#### Discussion

The delegate type that the configuration defines will be called for all lifecycle events associated with the scene accessory.

## Parameters

- `accessory`: A configuration which defines system functionality necessary to present the scene accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/registersceneaccessory(_:))*