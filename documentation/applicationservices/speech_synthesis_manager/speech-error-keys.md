# Speech Error Keys

**Framework**: Application Services

Keys used with the `kSpeechErrorsProperty` property to describe errors encountered during speech processing and production.

## Topics

### Constants
- [let kSpeechErrorCount: CFString](kspeecherrorcount.md)
  The number of errors that have occurred in processing the current text string, since the last call to the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property.
- [let kSpeechErrorOldest: CFString](kspeecherroroldest.md)
  The error code of the first error that occurred since the last call to the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property. 
- [let kSpeechErrorOldestCharacterOffset: CFString](kspeecherroroldestcharacteroffset.md)
  The position in the text string of the first error that occurred since the last call to the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property.
- [let kSpeechErrorNewest: CFString](kspeecherrornewest.md)
  The error code of the most recent error that occurred since the last call to the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property.
- [let kSpeechErrorNewestCharacterOffset: CFString](kspeecherrornewestcharacteroffset.md)
  The position in the text string of the most recent error that occurred since the last call to the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager/speech_error_keys)*