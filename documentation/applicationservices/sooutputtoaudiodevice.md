# soOutputToAudioDevice

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.6+

## Declaration

```swift
var soOutputToAudioDevice: OSType { get }
```

#### Discussion

Pass a pointer to an [`AudioDeviceID`](https://developer.apple.com/documentation/coreaudio/audiodeviceid) in the `speechInfo` parameter to play to this file, or `0` to play through the default audio output device.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sooutputtoaudiodevice)*