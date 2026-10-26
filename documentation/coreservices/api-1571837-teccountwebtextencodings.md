# TECCountWebTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts and returns the number of currently supported textencodings for a region code. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCountWebTextEncodings(RegionCode locale, ItemCount *numberEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

This function counts every instance of the same encoding.That is, if different conversion plug-ins support the same textencoding for a conversion process, the text encoding is countedmore than once. Since the `TECGetWebTextEncodings` functionignores duplicate text encoding specifications, `TECCountWebTextEncodings` mayreturn a number greater than the number of array elements neededfor the `availableEncodings[]` parameter. 

## Parameters

- `locale`: A Mac OS region code indicating the locale for which you want to count encodings. A region code designates a combination of language, writing system, and geographic region;the region may not correspond to a particular country (for example, Swiss French or Arabic). 
- `numberEncodings`: On return, a pointer to the number of currently supported text encodings for a region code. You should use this number to determine how large to make the array you pass to the [`TECGetWebTextEncodings`](./api-1571798-tecgetwebtextencodings.md) function. 

## See Also

### Getting Information About Internet and Regional Text Encoding Names
- [TECCountMailTextEncodings](./api-1571826-teccountmailtextencodings.md)
  Counts and returns the number of currently supported e-mailencodings for a specified region.
- [TECGetMailTextEncodings](./api-1571845-tecgetmailtextencodings.md)
  Returns the currently supported mail encoding specificationsfor a region code. 
- [TECGetTextEncodingFromInternetName](./api-1571825-tecgettextencodingfrominternetna.md)
  Returns the Mac OS text encoding specification that correspondsto an Internet encoding name.
- [TECGetTextEncodingInternetName](./api-1571851-tecgettextencodinginternetname.md)
  Returns the Internet encoding name that corresponds toa Mac OS text encoding. 
- [TECGetWebTextEncodings](./api-1571798-tecgetwebtextencodings.md)
  Returns the currently supported text encoding specificationsfor a region code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571837-teccountwebtextencodings)*