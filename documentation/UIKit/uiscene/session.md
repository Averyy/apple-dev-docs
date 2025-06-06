# session

**Framework**: UIKit  
**Kind**: property

The session associated with the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var session: UISceneSession { get }
```

#### Discussion

UIKit maintains a session object for each scene. The session object contains a unique identifier for the scene and other information about its configuration.

## See Also

- [class UISceneSession](uiscenesession.md)
  An object that contains information about one of your app’s scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/session)*