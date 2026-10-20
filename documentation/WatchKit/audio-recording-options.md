# Audio Recording Options

**Framework**: WatchKit  
**Role**: API Collection

Options to specify when recording audio.

## Topics

### Constants
- [let WKAudioRecorderControllerOptionsActionTitleKey: String](./wkaudiorecordercontrolleroptionsactiontitlekey.md)
  The title to display on the button that the user taps to accept a recording. The value of this key is an [`NSString`](../Foundation/nsstring.md) object. If you do not specify this option, the button title is set to “Save”.
- [let WKAudioRecorderControllerOptionsAlwaysShowActionTitleKey: String](./wkaudiorecordercontrolleroptionsalwaysshowactiontitlekey.md)
  The behavior for showing the action button. The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object with a Boolean value. When the value is [`true`](../Swift/true.md), the recording interface always shows the action button. When the value is [`false`](../Swift/false.md), the sheet shows the button only after the user has recorded some audio. The default value for this option is YES.
- [let WKAudioRecorderControllerOptionsAutorecordKey: String](./wkaudiorecordercontrolleroptionsautorecordkey.md)
  The automatic recording behavior of the action sheet. The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object with a Boolean value. When the value is [`true`](../Swift/true.md), the recording interface starts recording as soon as it is presented. When the value is [`false`](../Swift/false.md), the user must start recording manually. The default value for this option is [`true`](../Swift/true.md).
- [let WKAudioRecorderControllerOptionsMaximumDurationKey: String](./wkaudiorecordercontrolleroptionsmaximumdurationkey.md)
  The maximum length of recorded audio clips. The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object with an [`TimeInterval`](../Foundation/timeinterval.md) value containing the maximum duration in seconds. If you do not specify this option, there is no maximum recording time.

## See Also

### Presenting video and audio interfaces
- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](./wkinterfacecontroller/presentmediaplayercontroller%28with,options,completion%29.md)
  Displays a modal interface for playing the specified media file.
- [Media Player Options](./media-player-options.md)
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](./wkinterfacecontroller/dismissmediaplayercontroller%28%29.md)
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](./wkinterfacecontroller/presentaudiorecordercontroller%28withoutputurl,preset,options,completion%29.md)
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](./wkaudiorecorderpreset.md)
  Constants indicating the quality of audio recordings.
- [func dismissAudioRecorderController()](./wkinterfacecontroller/dismissaudiorecordercontroller%28%29.md)
  Dismisses the audio recording interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/audio-recording-options)*