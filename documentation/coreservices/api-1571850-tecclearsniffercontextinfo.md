# TECClearSnifferContextInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Resets a sniffer object to its initial settings so youcan reuse it.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECClearSnifferContextInfo(TECSnifferObjectRef encodingSniffer);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

Sniffers maintain state information about the input encodingbuffer and the number of errors and features found for each encoding;this information allows a caller to progressively sniff an inputbuffer in sequential chunks. Before sniffing a buffer that containscompletely new information you must clear any state informationby calling `TECClearSnifferContextInfo`. 

## Parameters

- `encodingSniffer`: A pointer to the sniffer object you want to reset. 

## See Also

### Using Sniffers to Investigate Encodings
- [TECCreateSniffer](./api-1571832-teccreatesniffer.md)
  Creates a sniffer object and returns a reference to it. 
- [TECDisposeSniffer](./api-1571854-tecdisposesniffer.md)
  Disposes of a sniffer object.
- [TECCountAvailableSniffers](./api-1571795-teccountavailablesniffers.md)
  Counts and returns the number of sniffers available inall installed plug-ins.
- [TECGetAvailableSniffers](./api-1571841-tecgetavailablesniffers.md)
  Returns the list of sniffers available in all installedplug-ins.
- [TECSniffTextEncoding](./api-1571836-tecsnifftextencoding.md)
  Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571850-tecclearsniffercontextinfo)*