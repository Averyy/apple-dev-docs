# CountVoices(_:)

**Framework**: Application Services  
**Kind**: func

Determines how many voices are available.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func CountVoices(_ numVoices: UnsafeMutablePointer<Int16>) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `CountVoices` functionreturns, in the `numVoices` parameter,the number of voices available. The application can then use thisinformation to call the `GetIndVoice` functionto obtain voice specification structures for one or more of thevoices.

Each time `CountVoices` iscalled, the Speech Synthesis Manager searches for new voices. 

## Parameters

- `numVoices`: On exit, a pointer to the number of voices that the application can use. 

## See Also

- [func GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1464595-getindvoice.md)
  Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.
- [func GetVoiceDescription(UnsafePointer<VoiceSpec>?, UnsafeMutablePointer<VoiceDescription>?, Int) -> OSErr](1463940-getvoicedescription.md)
  Gets a description of a voice by using the `GetVoiceDescription` function.
- [func GetVoiceInfo(UnsafePointer<VoiceSpec>?, OSType, UnsafeMutableRawPointer) -> OSErr](1461410-getvoiceinfo.md)
  Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 
- [func MakeVoiceSpec(OSType, OSType, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1461446-makevoicespec.md)
  Sets the fields of a voice specification structure. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459947-countvoices)*