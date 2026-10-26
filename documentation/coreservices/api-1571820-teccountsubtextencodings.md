# TECCountSubTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts and returns the number of subencodings a text encodingsupports.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCountSubTextEncodings(TextEncoding inputEncoding, ItemCount *numberOfEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

Subencodings are text encodings that are embedded as partof a larger text encoding specification. For example, EUC-JP containsJIS Roman or ASCII, JIS X0208, JIS X0212, and half-width Katakanafrom JIS X0201. Not every encoding that can be broken into multiple encodingsnecessarily supports this routine. It’s up to the plug-in developerto decide which encodings might be useful to break up. Subencodingsare not the same as text encoding variants.

If an encoding can be converted to multiple runs of encodings(as indicated by a destination base encoding of `kTextEncodingMultiRun`),you can call the `TECGetSubTextEncodings` functionto get the list of output encodings. See the  [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md)  and  [`TECGetDestinationTextEncodings`](./api-1571808-tecgetdestinationtextencodings.md) functions for information. 

## Parameters

- `inputEncoding`: The text encoding specification that contains the subencodings. 
- `numberOfEncodings`: On return, a pointer to the number of currently supported subencodings. You use this value to determine the array size for a parameter of the [`TECGetSubTextEncodings`](./api-1571796-tecgetsubtextencodings.md) function. 

## See Also

### Obtaining Information About Available Text Encodings
- [TECCountAvailableTextEncodings](./api-1571853-teccountavailabletextencodings.md)
  Counts and returns the number of text encodings currentlyconfigured in the Text Encoding Converter.
- [TECGetAvailableTextEncodings](./api-1571819-tecgetavailabletextencodings.md)
  Returns the text encoding specifications currently configuredin the Text Encoding Converter.
- [TECGetSubTextEncodings](./api-1571796-tecgetsubtextencodings.md)
  Returns the text encoding specifications for the subencodingsthe encoding scheme supports. 
- [NearestMacTextEncodings](./api-1399736-nearestmactextencodings.md)
  Obtains the best and alternate Mac text encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571820-teccountsubtextencodings)*