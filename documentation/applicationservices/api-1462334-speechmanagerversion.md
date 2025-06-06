# SpeechManagerVersion()

**Framework**: Application Services  
**Kind**: func

Determines the current version of the Speech SynthesisManager installed in the system.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func SpeechManagerVersion() -> NumVersion
```

#### Return_value

The version of theSpeech Synthesis Manager installed in the system, in the formatof the first 4 bytes of a `'vers'` resource. 

#### Discussion

Use this call to determine whether your program can accessfeatures of the Speech Synthesis Manager that are included in someSpeech Synthesis Manager releases but not in earlier ones.

## See Also

- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusy() -> Int16](1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechBusySystemWide() -> Int16](1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462334-speechmanagerversion)*