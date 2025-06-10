# sourceApplication

**Framework**: UIKit  
**Kind**: property

The bundle ID of the app that originated the request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceApplication: String? { get }
```

#### Discussion

If the request originated from another app belonging to your team, UIKit places the bundle ID of that app in this property. If the team identifier of the originating app is different than the team identifier of the current app, this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/sourceapplication)*