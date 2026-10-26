# TECGetMailTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the currently supported mail encoding specificationsfor a region code. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetMailTextEncodings(RegionCode locale, TextEncoding availableEncodings[], ItemCount maxAvailableEncodings, ItemCount *actualAvailableEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

This function ignores duplicate text encoding specifications.If you used the  [`TECCountMailTextEncodings`](./api-1571826-teccountmailtextencodings.md) function to determine the size of the `availableEncodings[]` arraythe number of available encodings may be fewer than the number ofarray elements, because `TECCountMailTextEncodings` includesduplicate text encoding specifications in its count. 

## Parameters

- `locale`: A Mac OS region code. A region code designates a combination of language, writing system, and geographic region;the region may not correspond to a particular country (for example, Swiss French or Arabic). 
- `availableEncodings`: An array of text encoding specifications. On return, the array contains specifications for the e-mail text encodings for a region code. You should use the function [`TECCountMailTextEncodings`](./api-1571826-teccountmailtextencodings.md) function to determine what size array to allocate. 
- `maxAvailableEncodings`: The number of text encoding specifications the `availableEncodings` array can contain. 
- `actualAvailableEncodings`: On return, a pointer to the number of text encodings in the `availableEncodings` array.

## See Also

### Getting Information About Internet and Regional Text Encoding Names
- [TECCountMailTextEncodings](./api-1571826-teccountmailtextencodings.md)
  Counts and returns the number of currently supported e-mailencodings for a specified region.
- [TECCountWebTextEncodings](./api-1571837-teccountwebtextencodings.md)
  Counts and returns the number of currently supported textencodings for a region code. 
- [TECGetTextEncodingFromInternetName](./api-1571825-tecgettextencodingfrominternetna.md)
  Returns the Mac OS text encoding specification that correspondsto an Internet encoding name.
- [TECGetTextEncodingInternetName](./api-1571851-tecgettextencodinginternetname.md)
  Returns the Internet encoding name that corresponds toa Mac OS text encoding. 
- [TECGetWebTextEncodings](./api-1571798-tecgetwebtextencodings.md)
  Returns the currently supported text encoding specificationsfor a region code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571845-tecgetmailtextencodings)*