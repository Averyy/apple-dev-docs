# scene(_:openURLContexts:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to open one or more URLs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>)
```

## Mentions

- [Collaborating and sharing copies of your data](collaborating-and-sharing-copies-of-your-data.md)

## Parameters

- `scene`: The scene that UIKit asks to open the URL.
- `URLContexts`: One or more   objects. Each object contains one URL to open and any additional information needed to open that URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:openurlcontexts:))*