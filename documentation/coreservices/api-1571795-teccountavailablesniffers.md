# TECCountAvailableSniffers

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts and returns the number of sniffers available inall installed plug-ins.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCountAvailableSniffers(ItemCount *numberOfEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

This function counts every instance of a sniffer. If differentconversion plug-ins support a sniffer for the same encoding, thesniffer is counted more than once. Since the `TECGetAvailableSniffers` functionignores duplicate sniffers, `TECCountAvailableSniffers` mayreturn a number greater than the number of array elements neededfor the `availableSniffers[]` parameterof the `TECGetAvailableSniffers` function. 

## Parameters

- `numberOfEncodings`: On return, a pointer to the number of sniffers in all installed plug-ins. You can use this number to determine what size array to allocate for a parameter of the [`TECGetAvailableSniffers`](./api-1571841-tecgetavailablesniffers.md) function. 

## See Also

### Using Sniffers to Investigate Encodings
- [TECCreateSniffer](./api-1571832-teccreatesniffer.md)
  Creates a sniffer object and returns a reference to it. 
- [TECClearSnifferContextInfo](./api-1571850-tecclearsniffercontextinfo.md)
  Resets a sniffer object to its initial settings so youcan reuse it.
- [TECDisposeSniffer](./api-1571854-tecdisposesniffer.md)
  Disposes of a sniffer object.
- [TECGetAvailableSniffers](./api-1571841-tecgetavailablesniffers.md)
  Returns the list of sniffers available in all installedplug-ins.
- [TECSniffTextEncoding](./api-1571836-tecsnifftextencoding.md)
  Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571795-teccountavailablesniffers)*