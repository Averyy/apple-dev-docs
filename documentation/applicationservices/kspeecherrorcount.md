# kSpeechErrorCount

**Framework**: Application Services  
**Kind**: data

The number of errors that have occurred in processing the current text string, since the last call to the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechErrorCount: CFString
```

#### Discussion

Using the `kSpeechErrorOldest` keys and the `kSpeechErrorNewest` keys, you can get information about the oldest and most recent errors that occurred since the last call to [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md), but you cannot get information about any intervening errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeecherrorcount)*