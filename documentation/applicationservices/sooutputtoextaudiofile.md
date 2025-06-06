# soOutputToExtAudioFile

**Framework**: Application Services  
**Kind**: data

Pass an [`ExtAudioFileRef`](https://developer.apple.com/documentation/audiotoolbox/extaudiofileref) in the `speechInfo` parameter to write to this file, or `NULL` to generate sound.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var soOutputToExtAudioFile: OSType { get }
```

#### Discussion

Note that the Speech Synthesis Manager may alter the [`kExtAudioFileProperty_ClientDataFormat`](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_clientdataformat) and [`kExtAudioFileProperty_ClientChannelLayout`](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_clientchannellayout) properties of the extended audio file object. The caller is responsible for closing the extended audio file object after the Speech Synthesis Manager is finished with it.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sooutputtoextaudiofile)*