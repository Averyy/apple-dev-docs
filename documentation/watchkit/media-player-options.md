# Media Player Options

**Framework**: Watchkit

Keys indicating media playback options.

## Topics

### Constants
- [let WKMediaPlayerControllerOptionsAutoplayKey: String](wkmediaplayercontrolleroptionsautoplaykey.md)
  The option to play a media file automatically when it is displayed. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value indicating whether the media file should begin playing automatically when the interface is displayed. Playback is also contingent upon the file being available and ready to play on Apple Watch. If you do not specify this option, the user must initiate playback.
- [let WKMediaPlayerControllerOptionsStartTimeKey: String](wkmediaplayercontrolleroptionsstarttimekey.md)
  The number of seconds into the media file at which to begin playback. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) value. Playback begins at the specified number of seconds past the original start point of the media file. If you do not specify this option, playback begins at the beginning of the media file.
- [let WKMediaPlayerControllerOptionsVideoGravityKey: String](wkmediaplayercontrolleroptionsvideogravitykey.md)
  The behavior for resizing the video to fit the available space. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an appropriate constant of the [`WKVideoGravity`](wkvideogravity.md) type.
- [let WKMediaPlayerControllerOptionsLoopsKey: String](wkmediaplayercontrolleroptionsloopskey.md)
  The behavior for playing the media in a loop. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. Set the value to [`true`](https://developer.apple.com/documentation/swift/true) to play the media file in a loop. If this key is not present, the media file plays one time and then ends.

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:).md)
  Displays a modal interface for playing the specified media file.
- [func dismissMediaPlayerController()](wkinterfacecontroller/dismissmediaplayercontroller.md)
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md)
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md)
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](audio-recording-options.md)
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](wkinterfacecontroller/dismissaudiorecordercontroller.md)
  Dismisses the audio recording interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/media-player-options)*