# appIntent

**Framework**: UIKit  
**Kind**: property

The `AppIntent` that triggered scene creation `AppIntentSceneDelegate.scene(_:willPerform:)` will always be called after scene connection

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var appIntent: (any UISceneAppIntent)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/appintent)*