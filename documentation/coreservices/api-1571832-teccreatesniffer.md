# TECCreateSniffer

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a sniffer object and returns a reference to it. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCreateSniffer(TECSnifferObjectRef *encodingSniffer, const TextEncoding testEncodings[], ItemCount numTextEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

The `TECCreateSniffer` functionpolls plug-ins for available sniffers, creates a sniffer object capableof sniffing each of the specified encodings that it can find a snifferfunction for, and returns a reference to it. You use this snifferobject reference with sniffer functions such as  [`TECSniffTextEncoding`](./api-1571836-tecsnifftextencoding.md). If no snifferfunction is available for an encoding, no error is returned and `TECSniffTextEncoding` indicateslater that the encoding was not examined.

To remove a sniffer object, you must call the function  [`TECDisposeSniffer`](./api-1571854-tecdisposesniffer.md). 

## Parameters

- `encodingSniffer`: A pointer to a sniffer object reference, which is of type [`TECSnifferObjectRef`](./tecsnifferobjectref.md). On return, the reference pertains to the newly created sniffer object. 
- `testEncodings`: An array of text encoding specifications supplied by the caller; `TECCreateSniffer` creates a sniffer that can detect each of these encodings. 
- `numTextEncodings`: The number of text encoding specifications in the `testEncodings[] `array. 

## See Also

### Using Sniffers to Investigate Encodings
- [TECClearSnifferContextInfo](./api-1571850-tecclearsniffercontextinfo.md)
  Resets a sniffer object to its initial settings so youcan reuse it.
- [TECDisposeSniffer](./api-1571854-tecdisposesniffer.md)
  Disposes of a sniffer object.
- [TECCountAvailableSniffers](./api-1571795-teccountavailablesniffers.md)
  Counts and returns the number of sniffers available inall installed plug-ins.
- [TECGetAvailableSniffers](./api-1571841-tecgetavailablesniffers.md)
  Returns the list of sniffers available in all installedplug-ins.
- [TECSniffTextEncoding](./api-1571836-tecsnifftextencoding.md)
  Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571832-teccreatesniffer)*