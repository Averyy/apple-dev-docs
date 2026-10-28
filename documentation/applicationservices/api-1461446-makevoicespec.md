# MakeVoiceSpec(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Sets the fields of a voice specification structure. 

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func MakeVoiceSpec(_ creator: OSType, _ id: OSType, _ voice: UnsafeMutablePointer<VoiceSpec>) -> OSErr
```

```c
OSErr MakeVoiceSpec(OSType creator, OSType id, VoiceSpec *voice);
```

## Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Discussion

A voice specification structure is a unique voice ID usedby the Speech Synthesis Manager. Most voice management functionsexpect to be passed a pointer to a voice specification structure.When you already know the creator and ID for a voice, you shoulduse the `MakeVoiceSpec` functionto create such a structure rather than filling in the fields ofone directly. On exit, the voice specification structure pointedto by the `voice` parameter containsthe appropriate values. You should never set the fields of sucha structure directly. 

## Parameters

- `creator`: The ID of the synthesizer that your application requires.
- `id`: The ID of the voice on the synthesizer specified by the `creator` parameter.
- `voice`: A pointer to the voice specification structure whose fields are to be filled in. 

## See Also

### Getting Information About Voices
- [func CountVoices(UnsafeMutablePointer<Int16>) -> OSErr](./api-1459947-countvoices.md)
  Determines how many voices are available.
- [func GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr](./api-1464595-getindvoice.md)
  Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.
- [func GetVoiceDescription(UnsafePointer<VoiceSpec>?, UnsafeMutablePointer<VoiceDescription>?, Int) -> OSErr](./api-1463940-getvoicedescription.md)
  Gets a description of a voice by using the `GetVoiceDescription` function.
- [func GetVoiceInfo(UnsafePointer<VoiceSpec>?, OSType, UnsafeMutableRawPointer) -> OSErr](./api-1461410-getvoiceinfo.md)
  Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461446-makevoicespec)*