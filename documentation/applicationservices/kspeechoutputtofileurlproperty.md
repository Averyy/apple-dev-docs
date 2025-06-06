# kSpeechOutputToFileURLProperty

**Framework**: Application Services  
**Kind**: data

Set the speech output destination to a file or to the computer’s speakers.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechOutputToFileURLProperty: CFString
```

#### Discussion

The value associated with this property is a `CFURL` object. To write the speech output to a file, use the file’s `CFURLRef`; to generate the sound through the computer’s speakers, use `NULL`.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechoutputtofileurlproperty)*