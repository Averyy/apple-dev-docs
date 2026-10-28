# TECDisposeSniffer

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes of a sniffer object.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECDisposeSniffer(TECSnifferObjectRef encodingSniffer);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

This function releases all memory allocated to the snifferobject created by the  [`TECCreateSniffer`](./api-1571832-teccreatesniffer.md) function. 

## Parameters

- `encodingSniffer`: The sniffer object reference you want to remove. 

## See Also

### Using Sniffers to Investigate Encodings
- [TECCreateSniffer](./api-1571832-teccreatesniffer.md)
  Creates a sniffer object and returns a reference to it. 
- [TECClearSnifferContextInfo](./api-1571850-tecclearsniffercontextinfo.md)
  Resets a sniffer object to its initial settings so youcan reuse it.
- [TECCountAvailableSniffers](./api-1571795-teccountavailablesniffers.md)
  Counts and returns the number of sniffers available inall installed plug-ins.
- [TECGetAvailableSniffers](./api-1571841-tecgetavailablesniffers.md)
  Returns the list of sniffers available in all installedplug-ins.
- [TECSniffTextEncoding](./api-1571836-tecsnifftextencoding.md)
  Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571854-tecdisposesniffer)*