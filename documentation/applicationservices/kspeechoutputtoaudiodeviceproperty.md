# kSpeechOutputToAudioDeviceProperty

**Framework**: Application Services  
**Kind**: data  
**Role**: Global Variable

Set the speech output destination to an audio device file or to the computer’s speakers.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let kSpeechOutputToAudioDeviceProperty: CFString
```

```c
const CFStringRef kSpeechOutputToAudioDeviceProperty;
```

#### Discussion

The value associated with this property is a `CFNumber` object that contains an [`AudioDeviceID`](../CoreAudio/audiodeviceid.md). To play the speech output to an audio device, use the [`AudioDeviceID`](../CoreAudio/audiodeviceid.md) that represents the device; to generate sound through the computer’s speakers, use `0`.

This property works with the [`SetSpeechProperty(_:_:_:)`](./api-1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechoutputtoaudiodeviceproperty)*