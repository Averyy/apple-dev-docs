# GetIndVoice(_:_:)

**Framework**: Application Services  
**Kind**: func

Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func GetIndVoice(_ index: Int16, _ voice: UnsafeMutablePointer<VoiceSpec>) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `GetIndVoice` functionreturns, in the voice specification structure pointed to by the `voice` parameter,a specification of the voice whose index is provided in the `index` parameter.Your application should make no assumptions about the order in whichvoices are indexed.

Your application should not add, remove, or modify a voiceand then call the `GetIndVoice` functionwith an index value other than `1`. To allow the Speech SynthesisManager to update its information about voices, your applicationshould always either call the `CountVoices` functionor call the `GetIndVoice` functionwith an index value of `1` after adding, removing, or modifying avoice or after a time at which the user might have done so.

If you specify an index value beyond the number of availablevoices, the `GetIndVoice` functionreturns a `voiceNotFound` error. 

## Parameters

- `index`: The index of the voice for which to obtain a voice specification structure. This number must range from   to the total number of voices, as returned by the   function. 
- `voice`: A pointer to the voice specification structure whose fields are to be filled in. 

## See Also

- [func CountVoices(UnsafeMutablePointer<Int16>) -> OSErr](1459947-countvoices.md)
  Determines how many voices are available.
- [func GetVoiceDescription(UnsafePointer<VoiceSpec>?, UnsafeMutablePointer<VoiceDescription>?, Int) -> OSErr](1463940-getvoicedescription.md)
  Gets a description of a voice by using the `GetVoiceDescription` function.
- [func GetVoiceInfo(UnsafePointer<VoiceSpec>?, OSType, UnsafeMutableRawPointer) -> OSErr](1461410-getvoiceinfo.md)
  Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 
- [func MakeVoiceSpec(OSType, OSType, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1461446-makevoicespec.md)
  Sets the fields of a voice specification structure. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464595-getindvoice)*