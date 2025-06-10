# appIntent

**Framework**: UIKit  
**Kind**: property

The `AppIntent` that triggered scene creation `AppIntentSceneDelegate.scene(_:willPerform:)` will always be called after scene connection

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 16.0+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var appIntent: (any UISceneAppIntent)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/appintent)*