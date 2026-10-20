# sceneAccessoryUserInfo

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An optional user info object, provided when creating the `UISceneAccessory` for this scene accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var sceneAccessoryUserInfo: Any? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) id sceneAccessoryUserInfo;
```

## Mentions

- [Presenting content on a connected display](../../presenting-content-on-a-connected-display.md)

#### Discussion

This object can be used to associate data to the scene accessory configuration to be passed to the scene delegate when the scene connects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/sceneaccessoryuserinfo)*