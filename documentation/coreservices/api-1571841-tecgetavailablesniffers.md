# TECGetAvailableSniffers

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the list of sniffers available in all installedplug-ins.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetAvailableSniffers(TextEncoding availableSniffers[], ItemCount maxAvailableSniffers, ItemCount *actualAvailableSniffers);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

This function ignores duplicate text encoding specifications.If you used the  [`TECCountAvailableSniffers`](./api-1571795-teccountavailablesniffers.md) function to determine the size of the `TECGetAvailableSniffers` array,the number of available encodings may be fewer than the number ofarray elements, because `TECCountAvailableSniffers` includesduplicate text encoding specifications in its count. 

## Parameters

- `availableSniffers`: On return, an array of text encoding specifications that the available sniffers currently support. You should use the [`TECCountAvailableSniffers`](./api-1571795-teccountavailablesniffers.md) function to determine what size array to allocate. 
- `maxAvailableSniffers`: The number of text encoding specifications the `availableSniffers` array can contain. 
- `actualAvailableSniffers`: On return, a pointer to the number of text encodings in the `availableSniffers` array.

## See Also

### Using Sniffers to Investigate Encodings
- [TECCreateSniffer](./api-1571832-teccreatesniffer.md)
  Creates a sniffer object and returns a reference to it. 
- [TECClearSnifferContextInfo](./api-1571850-tecclearsniffercontextinfo.md)
  Resets a sniffer object to its initial settings so youcan reuse it.
- [TECDisposeSniffer](./api-1571854-tecdisposesniffer.md)
  Disposes of a sniffer object.
- [TECCountAvailableSniffers](./api-1571795-teccountavailablesniffers.md)
  Counts and returns the number of sniffers available inall installed plug-ins.
- [TECSniffTextEncoding](./api-1571836-tecsnifftextencoding.md)
  Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571841-tecgetavailablesniffers)*