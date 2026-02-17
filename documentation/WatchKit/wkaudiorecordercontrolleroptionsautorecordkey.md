# WKAudioRecorderControllerOptionsAutorecordKey

**Framework**: WatchKit  
**Kind**: var

The automatic recording behavior of the action sheet. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with a Boolean value. When the value is [`true`](https://developer.apple.com/documentation/Swift/true), the recording interface starts recording as soon as it is presented. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the user must start recording manually. The default value for this option is [`true`](https://developer.apple.com/documentation/Swift/true).

**Availability**:
- watchOS 2.0+

## Declaration

```swift
let WKAudioRecorderControllerOptionsAutorecordKey: String
```

## See Also

- [let WKAudioRecorderControllerOptionsActionTitleKey: String](wkaudiorecordercontrolleroptionsactiontitlekey.md)
  The title to display on the button that the user taps to accept a recording. The value of this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object. If you do not specify this option, the button title is set to “Save”.
- [let WKAudioRecorderControllerOptionsAlwaysShowActionTitleKey: String](wkaudiorecordercontrolleroptionsalwaysshowactiontitlekey.md)
  The behavior for showing the action button. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with a Boolean value. When the value is [`true`](https://developer.apple.com/documentation/Swift/true), the recording interface always shows the action button. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the sheet shows the button only after the user has recorded some audio. The default value for this option is YES.
- [let WKAudioRecorderControllerOptionsMaximumDurationKey: String](wkaudiorecordercontrolleroptionsmaximumdurationkey.md)
  The maximum length of recorded audio clips. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with an [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) value containing the maximum duration in seconds. If you do not specify this option, there is no maximum recording time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiorecordercontrolleroptionsautorecordkey)*