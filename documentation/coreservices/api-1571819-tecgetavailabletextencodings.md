# TECGetAvailableTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the text encoding specifications currently configuredin the Text Encoding Converter.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetAvailableTextEncodings(TextEncoding availableEncodings[], ItemCount maxAvailableEncodings, ItemCount *actualAvailableEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

This function ignores duplicate text encoding specifications.If you used the  [`TECCountAvailableTextEncodings`](./api-1571853-teccountavailabletextencodings.md) function to determine the size of the `availableEncodings ` []array, the number of encodings may be fewer than the number of arrayelements, because `TECCountAvailableTextEncodings` includesduplicate text encodings in its count.  

## Parameters

- `availableEncodings`: On return, an array of text encoding specifications. You should use the [`TECCountAvailableTextEncodings`](./api-1571853-teccountavailabletextencodings.md) function to determine what size array to allocate. 
- `maxAvailableEncodings`: The number of text encoding specifications the `availableEncodings` array can contain. 
- `actualAvailableEncodings`: On return, a pointer to the number of text encodings returned in the `availableEncodings` array.

## See Also

### Obtaining Information About Available Text Encodings
- [TECCountAvailableTextEncodings](./api-1571853-teccountavailabletextencodings.md)
  Counts and returns the number of text encodings currentlyconfigured in the Text Encoding Converter.
- [TECCountSubTextEncodings](./api-1571820-teccountsubtextencodings.md)
  Counts and returns the number of subencodings a text encodingsupports.
- [TECGetSubTextEncodings](./api-1571796-tecgetsubtextencodings.md)
  Returns the text encoding specifications for the subencodingsthe encoding scheme supports. 
- [NearestMacTextEncodings](./api-1399736-nearestmactextencodings.md)
  Obtains the best and alternate Mac text encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571819-tecgetavailabletextencodings)*