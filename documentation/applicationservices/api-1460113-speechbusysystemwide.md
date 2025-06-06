# SpeechBusySystemWide()

**Framework**: Application Services  
**Kind**: func

Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func SpeechBusySystemWide() -> Int16
```

#### Return_value

The total number ofspeech channels currently synthesizing speech on the computer, whetherthey were initiated by your application or process’s code or bysome other process executing concurrently. Paused speech channelsare counted among those channels that are synthesizing speech. 

#### Discussion

This function is useful when you want to ensure that no speechis currently being produced anywhere on the Macintosh computer beforeinitiating speech. Although the Speech Synthesis Manager allowsdifferent applications to produce speech simultaneously, this canbe confusing to the user. As a result, it is often a good idea foryour application to check that no other process is producing speechbefore producing speech itself. If the difference between the valuesreturned by `SpeechBusySystemWide` andthe `SpeechBusy` functionis `0`, no other process is producing speech. 

## See Also

- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusy() -> Int16](1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechManagerVersion() -> NumVersion](1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460113-speechbusysystemwide)*