# kSpeechResetProperty

**Framework**: Application Services  
**Kind**: data

Set a speech channel back to its default state.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechResetProperty: CFString
```

#### Discussion

You can use this function to, for example, set speech pitch and speech rate to default values. There is no value associated with this property; to reset the channel to its default state, set the string to `NULL`.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechresetproperty)*