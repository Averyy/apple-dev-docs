# kSpeechOutputToExtAudioFileProperty

**Framework**: Application Services  
**Kind**: data

Set the speech output destination to an extended audio file or to the computer’s speakers.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let kSpeechOutputToExtAudioFileProperty: CFString
```

#### Discussion

The value associated with this property is a `CFNumber` object whose value is an `ExtAudioFileRef`. To write the speech output to an extended audio file, use the file’s [`ExtAudioFileRef`](https://developer.apple.com/documentation/audiotoolbox/extaudiofileref); to generate sound through the computer’s speakers, use `NULL`.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechoutputtoextaudiofileproperty)*