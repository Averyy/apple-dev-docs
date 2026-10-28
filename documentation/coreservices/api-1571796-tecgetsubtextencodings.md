# TECGetSubTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the text encoding specifications for the subencodingsthe encoding scheme supports. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetSubTextEncodings(TextEncoding inputEncoding, TextEncoding subEncodings[], ItemCount maxSubEncodings, ItemCount *actualSubEncodings);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

Subencodings are text encodings that are embedded as partof a larger text encoding specification. For example, EUC-JP containsJIS Roman or ASCII, JIS X0208, JIS X0212, and half-width Katakanafrom JIS X0201. Not every encoding that can be broken into multiple encodingsnecessarily supports this routine. It’s up to the plug-in developerto decide which encodings might be useful to break up. Subencodingsare not the same as text encoding variants

If an encoding can be converted to multiple runs of encodings(as indicated by a destination base encoding of `kTextEncodingMultiRun)`,you can call the  [`TECGetSubTextEncodings`](./api-1571796-tecgetsubtextencodings.md) function to get the list of output encodings. See the  [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md) and  [`TECGetDestinationTextEncodings`](./api-1571808-tecgetdestinationtextencodings.md) functions for information about multiple output encoding run conversions. 

## Parameters

- `inputEncoding`: A text encoding specification. 
- `subEncodings`: On return, the array contains the specifications for the subencodings of the `inputEncoding` parameter. You should use the function [`TECCountSubTextEncodings`](./api-1571820-teccountsubtextencodings.md) function to determine what size an array to allocate.
- `maxSubEncodings`: The number of text encoding specifications the `subEncodings` array can contain. 
- `actualSubEncodings`: On return, a pointer to number of subencodings in the `subEncodings` array.

## See Also

### Obtaining Information About Available Text Encodings
- [TECCountAvailableTextEncodings](./api-1571853-teccountavailabletextencodings.md)
  Counts and returns the number of text encodings currentlyconfigured in the Text Encoding Converter.
- [TECCountSubTextEncodings](./api-1571820-teccountsubtextencodings.md)
  Counts and returns the number of subencodings a text encodingsupports.
- [TECGetAvailableTextEncodings](./api-1571819-tecgetavailabletextencodings.md)
  Returns the text encoding specifications currently configuredin the Text Encoding Converter.
- [NearestMacTextEncodings](./api-1399736-nearestmactextencodings.md)
  Obtains the best and alternate Mac text encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571796-tecgetsubtextencodings)*