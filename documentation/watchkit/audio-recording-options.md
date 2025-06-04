# Audio Recording Options

**Framework**: Watchkit

Options to specify when recording audio.

## Topics

### Constants
- [let WKAudioRecorderControllerOptionsActionTitleKey: String](wkaudiorecordercontrolleroptionsactiontitlekey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecordercontrolleroptionsactiontitlekey))
  The title to display on the button that the user taps to accept a recording. The value of this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object. If you do not specify this option, the button title is set to “Save”.
- [let WKAudioRecorderControllerOptionsAlwaysShowActionTitleKey: String](wkaudiorecordercontrolleroptionsalwaysshowactiontitlekey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecordercontrolleroptionsalwaysshowactiontitlekey))
  The behavior for showing the action button. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with a Boolean value. When the value is [`true`](https://developer.apple.com/documentation/swift/true), the recording interface always shows the action button. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the sheet shows the button only after the user has recorded some audio. The default value for this option is YES.
- [let WKAudioRecorderControllerOptionsAutorecordKey: String](wkaudiorecordercontrolleroptionsautorecordkey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecordercontrolleroptionsautorecordkey))
  The automatic recording behavior of the action sheet. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with a Boolean value. When the value is [`true`](https://developer.apple.com/documentation/swift/true), the recording interface starts recording as soon as it is presented. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the user must start recording manually. The default value for this option is [`true`](https://developer.apple.com/documentation/swift/true).
- [let WKAudioRecorderControllerOptionsMaximumDurationKey: String](wkaudiorecordercontrolleroptionsmaximumdurationkey.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecordercontrolleroptionsmaximumdurationkey))
  The maximum length of recorded audio clips. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with an [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) value containing the maximum duration in seconds. If you do not specify this option, there is no maximum recording time.

## See Also

- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](presentmediaplayercontroller(with:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:)))
- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
- [func dismissMediaPlayerController()](dismissmediaplayercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller()))
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset))
- [func dismissAudioRecorderController()](dismissaudiorecordercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/audio-recording-options)*