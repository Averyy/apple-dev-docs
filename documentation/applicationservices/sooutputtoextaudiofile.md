# soOutputToExtAudioFile

**Framework**: Application Services  
**Kind**: data  
**Role**: Global Variable

Pass an [`ExtAudioFileRef`](../AudioToolbox/extaudiofileref.md) in the `speechInfo` parameter to write to this file, or `NULL` to generate sound.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var soOutputToExtAudioFile: OSType { get }
```

## Discussion

Note that the Speech Synthesis Manager may alter the [`kExtAudioFileProperty_ClientDataFormat`](../AudioToolbox/kextaudiofileproperty_clientdataformat.md) and [`kExtAudioFileProperty_ClientChannelLayout`](../AudioToolbox/kextaudiofileproperty_clientchannellayout.md) properties of the extended audio file object. The caller is responsible for closing the extended audio file object after the Speech Synthesis Manager is finished with it.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sooutputtoextaudiofile)*