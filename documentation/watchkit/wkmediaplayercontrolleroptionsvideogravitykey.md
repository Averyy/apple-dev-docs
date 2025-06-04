# WKMediaPlayerControllerOptionsVideoGravityKey

**Framework**: WatchKit  
**Kind**: var

The behavior for resizing the video to fit the available space. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an appropriate constant of the [`WKVideoGravity`](https://developer.apple.com/documentation/watchkit/wkvideogravity) type.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
let WKMediaPlayerControllerOptionsVideoGravityKey: String
```

## See Also

- [let WKMediaPlayerControllerOptionsAutoplayKey: String](wkmediaplayercontrolleroptionsautoplaykey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmediaplayercontrolleroptionsautoplaykey))
  The option to play a media file automatically when it is displayed. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value indicating whether the media file should begin playing automatically when the interface is displayed. Playback is also contingent upon the file being available and ready to play on Apple Watch. If you do not specify this option, the user must initiate playback.
- [let WKMediaPlayerControllerOptionsStartTimeKey: String](wkmediaplayercontrolleroptionsstarttimekey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmediaplayercontrolleroptionsstarttimekey))
  The number of seconds into the media file at which to begin playback. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) value. Playback begins at the specified number of seconds past the original start point of the media file. If you do not specify this option, playback begins at the beginning of the media file.
- [let WKMediaPlayerControllerOptionsLoopsKey: String](wkmediaplayercontrolleroptionsloopskey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmediaplayercontrolleroptionsloopskey))
  The behavior for playing the media in a loop. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. Set the value to [`true`](https://developer.apple.com/documentation/swift/true) to play the media file in a loop. If this key is not present, the media file plays one time and then ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkmediaplayercontrolleroptionsvideogravitykey)*