# SpeechVersionInfo

**Framework**: Application Services  
**Kind**: struct

Defines a speech version information structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SpeechVersionInfo
```

#### Overview

By calling the [`GetSpeechInfo`](1552220-getspeechinfo.md) function with the `soSynthType` selector, you can obtain a speech version information structure, which provides information about the speech synthesizer currently being used. 

## Topics

### Initializers
- [init()](speechversioninfo/1462191-init.md)
- [init(synthType: OSType, synthSubType: OSType, synthManufacturer: OSType, synthFlags: Int32, synthVersion: NumVersion)](speechversioninfo/1458819-init.md)
### Instance Properties
- [var synthFlags: Int32](speechversioninfo/1464789-synthflags.md)
  A set of flags indicating which synthesizer features are activated. Specific constants define the bits in this field whose meanings are defined for all synthesizers.
- [var synthManufacturer: OSType](speechversioninfo/1458822-synthmanufacturer.md)
  A unique identification of a synthesizer engine. If you develop synthesizers, then you should register a different four-character code for each synthesizer you develop with Developer Technical Support. The `creatorID` field of the voice specification structure and the `synthCreator` field of a speech extension data structure should each be set to the value stored in this field for the desired synthesizer.
- [var synthSubType: OSType](speechversioninfo/1460351-synthsubtype.md)
  The specific type of the synthesizer. Currently, no specific types of synthesizer are defined. If you define a new type of synthesizer, you should register the four-character code for your type with Developer Technical Support.
- [var synthType: OSType](speechversioninfo/1459500-synthtype.md)
  The general type of the synthesizer. For the current version of the Speech Synthesis Manager, this field always contains the value `kTextToSpeechSynthType`, indicating that the synthesizer converts text into speech.
- [var synthVersion: NumVersion](speechversioninfo/1459222-synthversion.md)
  The version number of the synthesizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechversioninfo)*