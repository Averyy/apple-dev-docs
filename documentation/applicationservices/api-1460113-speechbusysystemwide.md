# SpeechBusySystemWide()

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func SpeechBusySystemWide() -> Int16
```

```c
SInt16 SpeechBusySystemWide(void);
```

## Return Value

The total number ofspeech channels currently synthesizing speech on the computer, whetherthey were initiated by your application or process’s code or bysome other process executing concurrently. Paused speech channelsare counted among those channels that are synthesizing speech. 

## Discussion

This function is useful when you want to ensure that no speechis currently being produced anywhere on the Macintosh computer beforeinitiating speech. Although the Speech Synthesis Manager allowsdifferent applications to produce speech simultaneously, this canbe confusing to the user. As a result, it is often a good idea foryour application to check that no other process is producing speechbefore producing speech itself. If the difference between the valuesreturned by `SpeechBusySystemWide` andthe `SpeechBusy` functionis `0`, no other process is producing speech. 

## See Also

### Obtaining Information About Speech and Speech Channels
- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](./api-1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](./api-1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](./api-1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusy() -> Int16](./api-1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechManagerVersion() -> NumVersion](./api-1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.
- [GetSpeechInfo](./api-1552220-getspeechinfo.md)
  Gets information about a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460113-speechbusysystemwide)*