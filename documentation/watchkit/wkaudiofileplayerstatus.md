# WKAudioFilePlayerStatus

**Framework**: Watchkit  
**Kind**: enum

Constants that represent the status of the player.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKAudioFilePlayerStatus
```

## Topics

### Constants
- [WKAudioFilePlayerStatus.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/unknown))
  The status of the item is unknown because the player has not yet loaded the audio file for playback.
- [WKAudioFilePlayerStatus.readyToPlay](readytoplay.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/readytoplay))
  The player is ready to play its item.
- [WKAudioFilePlayerStatus.failed](failed.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/failed))
  The player can no longer play the audio because of an error. Use the [`error`](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/error) property to get information about the error that occurred.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus)*