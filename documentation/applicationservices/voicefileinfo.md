# VoiceFileInfo

**Framework**: Application Services  
**Kind**: struct

Defines a voice file information structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct VoiceFileInfo
```

#### Overview

A voice file information structure specifies the file in which a voice is stored and the resource ID of the voice within that file. Use the [`GetVoiceInfo(_:_:_:)`](1461410-getvoiceinfo.md) function to obtain a voice file information structure for a voice.

## Topics

### Initializers
- [init()](voicefileinfo/1464655-init.md)
- [init(fileSpec: FSSpec, resID: Int16)](voicefileinfo/1460648-init.md)
### Instance Properties
- [var fileSpec: FSSpec](voicefileinfo/1460824-filespec.md)
  A file system specification structure that contains the volume, directory, and name of the file containing the voice. Generally, files containing a single voice are of type `kTextToSpeechVoiceFileType`, and files containing multiple voices are of type `kTextToSpeechVoiceBundleType`. 
- [var resID: Int16](voicefileinfo/1462134-resid.md)
  The resource ID of the voice in the file. Voices are stored in resources of type `kTextToSpeechVoiceType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/voicefileinfo)*