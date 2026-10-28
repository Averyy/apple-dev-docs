# TECGetTextEncodingInternetName

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the Internet encoding name that corresponds toa Mac OS text encoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetTextEncodingInternetName(TextEncoding textEncoding, Str255 encodingName);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Parameters

- `textEncoding`: A Mac OS text encoding specification. 
- `encodingName`: On return, the Internet encoding name, in 7-bit US ASCII. If there are several Internet encoding names for the same text encoding, the `encodingName` parameter contains the preferred name. 

## See Also

### Getting Information About Internet and Regional Text Encoding Names
- [TECCountMailTextEncodings](./api-1571826-teccountmailtextencodings.md)
  Counts and returns the number of currently supported e-mailencodings for a specified region.
- [TECCountWebTextEncodings](./api-1571837-teccountwebtextencodings.md)
  Counts and returns the number of currently supported textencodings for a region code. 
- [TECGetMailTextEncodings](./api-1571845-tecgetmailtextencodings.md)
  Returns the currently supported mail encoding specificationsfor a region code. 
- [TECGetTextEncodingFromInternetName](./api-1571825-tecgettextencodingfrominternetna.md)
  Returns the Mac OS text encoding specification that correspondsto an Internet encoding name.
- [TECGetWebTextEncodings](./api-1571798-tecgetwebtextencodings.md)
  Returns the currently supported text encoding specificationsfor a region code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571851-tecgettextencodinginternetname)*