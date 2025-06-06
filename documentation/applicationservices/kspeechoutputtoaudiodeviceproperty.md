# kSpeechOutputToAudioDeviceProperty

**Framework**: Application Services  
**Kind**: data

Set the speech output destination to an audio device file or to the computer’s speakers.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let kSpeechOutputToAudioDeviceProperty: CFString
```

#### Discussion

The value associated with this property is a `CFNumber` object that contains an [`AudioDeviceID`](https://developer.apple.com/documentation/coreaudio/audiodeviceid). To play the speech output to an audio device, use the [`AudioDeviceID`](https://developer.apple.com/documentation/coreaudio/audiodeviceid) that represents the device; to generate sound through the computer’s speakers, use `0`.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechoutputtoaudiodeviceproperty)*