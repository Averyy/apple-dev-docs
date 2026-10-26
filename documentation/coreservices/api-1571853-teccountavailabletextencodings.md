# TECCountAvailableTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts and returns the number of text encodings currentlyconfigured in the Text Encoding Converter.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCountAvailableTextEncodings(ItemCount *numberEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

The number of text encodings includes every instance of atext encoding. If different conversion plug-ins support the sametext encoding, the text encoding will be counted more than once.For example, the Japanese Encodings plug-in supports Mac OS Japanese, andso does the Unicode Encodings plug-in. Since the `TECGetAvailableTextEncodings` functionignores duplicate text encoding specifications, `TECCountAvailableTextEncodings` mayreturn a number greater than the number of array elements neededfor the `availableEncodings ` []parameter.  

## Parameters

- `numberEncodings`: On return, a pointer to the number of currently supported text encodings. You use this value to determine the array size for a parameter of the [`TECGetAvailableTextEncodings`](./api-1571819-tecgetavailabletextencodings.md) function. 

## See Also

### Obtaining Information About Available Text Encodings
- [TECCountSubTextEncodings](./api-1571820-teccountsubtextencodings.md)
  Counts and returns the number of subencodings a text encodingsupports.
- [TECGetAvailableTextEncodings](./api-1571819-tecgetavailabletextencodings.md)
  Returns the text encoding specifications currently configuredin the Text Encoding Converter.
- [TECGetSubTextEncodings](./api-1571796-tecgetsubtextencodings.md)
  Returns the text encoding specifications for the subencodingsthe encoding scheme supports. 
- [NearestMacTextEncodings](./api-1399736-nearestmactextencodings.md)
  Obtains the best and alternate Mac text encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571853-teccountavailabletextencodings)*