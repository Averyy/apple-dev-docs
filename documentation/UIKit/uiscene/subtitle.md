# subtitle

**Framework**: UIKit  
**Kind**: property

A string that the app displays in the title bar of a window when running in macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var subtitle: String { get set }
```

#### Discussion

When this property is an empty string, the system removes the subtitle from the window layout. The default value is an empty string.

> **Note**:  Apps running in iOS ignore the [`subtitle`](uiscene/subtitle.md) property.

 Apps running in iOS ignore the [`subtitle`](uiscene/subtitle.md) property.

## See Also

- [var activationState: UIScene.ActivationState](uiscene/activationstate-swift.property.md)
  The current execution state of the scene.
- [UIScene.ActivationState](uiscene/activationstate-swift.enum.md)
  Constants that indicate the foreground or background execution state of your app.
- [var title: String!](uiscene/title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/subtitle)*