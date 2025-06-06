# GetVoiceDescription(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Gets a description of a voice by using the `GetVoiceDescription` function.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func GetVoiceDescription(_ voice: UnsafePointer<VoiceSpec>?, _ info: UnsafeMutablePointer<VoiceDescription>?, _ infoLength: Int) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `GetVoiceDescription` functionfills out the voice description structure pointed to by the `info` parameterwith the correct information for the voice specified by the `voice` parameter. Itfills in the `length` fieldof the voice description structure with the number of bytes actuallycopied. This value will always be less than or equal to the valuethat your application passes in `infoLength` beforecalling `GetVoiceDescription`.This scheme allows applications targeted for the current versionof the Speech Synthesis Manager to work on future versions thatmight have longer voice description structures; it also allows youto write code for future versions of the Speech Synthesis Managerthat will also run on computers that support only the current version.

If the voice specification structure does not identify anavailable voice, `GetVoiceDescription` returnsa `voiceNotFound` error. 

## Parameters

- `voice`: A pointer to the voice specification structure identifying the voice to be described, or   to obtain a description of the system default voice. 
- `info`: A pointer to a voice description structure. If this parameter is  , the function does not fill in the fields of the voice description structure; instead, it simply determines whether the   parameter specifies an available voice and, if not, returns a   error. 
- `infoLength`: The length, in bytes, of the voice description structure. In the current version of the Speech Synthesis Manager, the voice description structure contains 362 bytes. However, you should always use the   function to determine the length of this structure. 

## See Also

- [func CountVoices(UnsafeMutablePointer<Int16>) -> OSErr](1459947-countvoices.md)
  Determines how many voices are available.
- [func GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1464595-getindvoice.md)
  Gets a voice specification structure for a voice bypassing an index to the `GetIndVoice` function.
- [func GetVoiceInfo(UnsafePointer<VoiceSpec>?, OSType, UnsafeMutableRawPointer) -> OSErr](1461410-getvoiceinfo.md)
  Gets the same information about a voice that the `GetVoiceDescription` function provides,or to determine in which file and resource a voice is stored. 
- [func MakeVoiceSpec(OSType, OSType, UnsafeMutablePointer<VoiceSpec>) -> OSErr](1461446-makevoicespec.md)
  Sets the fields of a voice specification structure. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463940-getvoicedescription)*