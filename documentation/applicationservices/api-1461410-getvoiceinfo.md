# GetVoiceInfo(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func GetVoiceInfo(_ voice: UnsafePointer<VoiceSpec>?, _ selector: OSType, _ voiceInfo: UnsafeMutableRawPointer) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

This function is intended primarily for use by synthesizers,but an application can call it too. 

The `GetVoiceInfo` functionaccepts a selector in the `selector` parameterthat determines the type of information you wish to obtain aboutthe voice specified in the `voice` parameter. Thefunction then fills the fields of the data structure appropriateto the selector you specify in the `voiceInfo` parameter.

If the voice specification is invalid, `GetVoiceInfo` returnsa `voiceNotFound` error.If there is not enough memory to load the voice into memory to obtaininformation about it, `GetVoiceInfo` returnsthe result code `memFullErr`. 

## Parameters

- `voice`: A pointer to the voice specification structure identifying the voice about which your application requires information, or   to obtain information on the system default voice. 
- `selector`: A specification of the type of data being requested. For current versions of the Speech Synthesis Manager, you should set this field either to  , if you would like to use the   function to mimic the   function, or to  , if you would like to obtain information about the location of a voice on disk.
- `voiceInfo`: A pointer to the appropriate data structure. If the selector is  , then   should be a pointer to a voice description structure, and the   field of the structure should be set to the length of the voice description structure. If the selector is  , then   should be a pointer to a voice file information structure. 

## See Also

- [func CountVoices(UnsafeMutablePointer<Int16>) -> OSErr](1459947-countvoices.md)
  Determines how many voices are available.
- [func GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1464595-getindvoice.md)
  Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.
- [func GetVoiceDescription(UnsafePointer<VoiceSpec>?, UnsafeMutablePointer<VoiceDescription>?, Int) -> OSErr](1463940-getvoicedescription.md)
  Gets a description of a voice by using the `GetVoiceDescription` function.
- [func MakeVoiceSpec(OSType, OSType, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1461446-makevoicespec.md)
  Sets the fields of a voice specification structure. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461410-getvoiceinfo)*