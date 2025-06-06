# SpeechXtndData

**Framework**: Application Services  
**Kind**: struct

Defines a speech extension data structure. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SpeechXtndData
```

#### Overview

The speech extension data structure allows you to use the [`GetSpeechInfo`](1552220-getspeechinfo.md) and [`SetSpeechInfo`](1552223-setspeechinfo.md) functions with selectors defined by particular synthesizers. By requiring that you pass to one of these functions a pointer to a speech extension data structure, synthesizers can permit the exchange of data in any format.

## Topics

### Initializers
- [init()](speechxtnddata/1459302-init.md)
- [init(synthCreator: OSType, synthData: (UInt8, UInt8))](speechxtnddata/1461482-init.md)
### Instance Properties
- [var synthCreator: OSType](speechxtnddata/1462619-synthcreator.md)
  The synthesizer’s creator ID, identical to the value stored in the `synthManufacturer` field of a speech version information structure. You should set this field to the appropriate value before calling `GetSpeechInfo` or `SetSpeechInfo`.
- [var synthData: (UInt8, UInt8)](speechxtnddata/1459201-synthdata.md)
  Synthesizer-specific data. The size and format of the data in this field may vary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechxtnddata)*