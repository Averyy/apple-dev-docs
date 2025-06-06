# MakeVoiceSpec(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the fields of a voice specification structure. 

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func MakeVoiceSpec(_ creator: OSType, _ id: OSType, _ voice: UnsafeMutablePointer<VoiceSpec>) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

A voice specification structure is a unique voice ID usedby the Speech Synthesis Manager. Most voice management functionsexpect to be passed a pointer to a voice specification structure.When you already know the creator and ID for a voice, you shoulduse the `MakeVoiceSpec` functionto create such a structure rather than filling in the fields ofone directly. On exit, the voice specification structure pointedto by the `voice` parameter containsthe appropriate values. You should never set the fields of sucha structure directly. 

## Parameters

- `creator`: The ID of the synthesizer that your application requires.
- `id`: The ID of the voice on the synthesizer specified by the   parameter.
- `voice`: A pointer to the voice specification structure whose fields are to be filled in. 

## See Also

- [func CountVoices(UnsafeMutablePointer<Int16>) -> OSErr](1459947-countvoices.md)
  Determines how many voices are available.
- [func GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1464595-getindvoice.md)
  Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.
- [func GetVoiceDescription(UnsafePointer<VoiceSpec>?, UnsafeMutablePointer<VoiceDescription>?, Int) -> OSErr](1463940-getvoicedescription.md)
  Gets a description of a voice by using the `GetVoiceDescription` function.
- [func GetVoiceInfo(UnsafePointer<VoiceSpec>?, OSType, UnsafeMutableRawPointer) -> OSErr](1461410-getvoiceinfo.md)
  Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461446-makevoicespec)*