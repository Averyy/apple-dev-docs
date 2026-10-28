# soOutputToAudioDevice

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.6+

## Declaration

```c
soOutputToAudioDevice = 'opad'
```

## Discussion

Pass a pointer to an [`AudioDeviceID`](../../CoreAudio/audiodeviceid.md) in the `speechInfo` parameter to play to this file, or `0` to play through the default audio output device.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/sooutputtoaudiodevice)*