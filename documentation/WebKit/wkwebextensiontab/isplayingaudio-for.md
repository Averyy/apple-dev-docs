# isPlayingAudio(for:)

**Framework**: Webkit  
**Kind**: method

Called to check if the tab is currently playing audio.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func isPlayingAudio(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

Defaults to `NO` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/isplayingaudio(for:))*