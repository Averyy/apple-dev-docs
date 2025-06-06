# VoiceDescription

**Framework**: Application Services  
**Kind**: struct

Defines a voice description structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct VoiceDescription
```

#### Overview

By calling the [`GetVoiceDescription(_:_:_:)`](1463940-getvoicedescription.md) function, you can obtain information about a voice in a voice description structure.

## Topics

### Initializers
- [init()](voicedescription/1460513-init.md)
- [init(length: Int32, voice: VoiceSpec, version: Int32, name: Str63, comment: Str255, gender: Int16, age: Int16, script: Int16, language: Int16, region: Int16, reserved: (Int32, Int32, Int32, Int32))](voicedescription/1463154-init.md)
### Instance Properties
- [var age: Int16](voicedescription/1462733-age.md)
  The approximate age in years of the individual represented by the voice.
- [var comment: Str255](voicedescription/1461098-comment.md)
  Additional text information about the voice. Some synthesizers use this field to store a phrase that can be spoken.
- [var gender: Int16](voicedescription/1460238-gender.md)
  The gender of the individual represented by the voice. See [`Gender Constants`](speech_synthesis_manager/1552246-gender_constants.md).
- [var language: Int16](voicedescription/1464160-language.md)
  A code that indicates the language of voice output.
- [var length: Int32](voicedescription/1463606-length.md)
  The size of the voice description structure, in bytes.
- [var name: Str63](voicedescription/1459756-name.md)
  The name of the voice, preceded by a length byte. Names must be 63 characters or less.
- [var region: Int16](voicedescription/1462975-region.md)
  A code that indicates the region represented by the voice.
- [var reserved: (Int32, Int32, Int32, Int32)](voicedescription/1462772-reserved.md)
  Reserved. May be used to hold a 32-bit encoding value, if necessary (see the description of the `script` field for more information).
- [var script: Int16](voicedescription/1461925-script.md)
  The encoding code of the text that the voice can process.
- [var version: Int32](voicedescription/1464717-version.md)
  The version number of the voice.
- [var voice: VoiceSpec](voicedescription/1462456-voice.md)
  A voice specification structure that uniquely identifies the voice. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/voicedescription)*