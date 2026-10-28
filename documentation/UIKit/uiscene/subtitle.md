# subtitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that the app displays in the title bar of a window when running in macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var subtitle: String { get set }
```

```objc
@property (nonatomic, copy) NSString * subtitle;
```

## Discussion

When this property is an empty string, the system removes the subtitle from the window layout. The default value is an empty string.

> **Note**:  Apps running in iOS ignore the [`subtitle`](./subtitle.md) property.

## See Also

### Getting the scene attributes
- [var activationState: UIScene.ActivationState](./activationstate-swift.property.md)
  The current execution state of the scene.
- [UIScene.ActivationState](./activationstate-swift.enum.md)
  Constants that indicate the foreground or background execution state of your app.
- [var title: String!](./title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/subtitle)*