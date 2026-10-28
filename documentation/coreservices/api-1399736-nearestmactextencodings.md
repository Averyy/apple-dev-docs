# NearestMacTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the best and alternate Mac text encoding.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus NearestMacTextEncodings(TextEncoding generalEncoding, TextEncoding *bestMacEncoding, TextEncoding *alternateMacEncoding);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Parameters

- `generalEncoding`: The text encoding for which you want to obtain a Mac text encoding. 
- `bestMacEncoding`: On return, the Mac text encoding that best matches the encoding specified by the `generalEncoding` parameter. 
- `alternateMacEncoding`: On return, the Mac text encoding that is the second best match for the encoding specified by the `generalEncoding` parameter.

## See Also

### Obtaining Information About Available Text Encodings
- [TECCountAvailableTextEncodings](./api-1571853-teccountavailabletextencodings.md)
  Counts and returns the number of text encodings currentlyconfigured in the Text Encoding Converter.
- [TECCountSubTextEncodings](./api-1571820-teccountsubtextencodings.md)
  Counts and returns the number of subencodings a text encodingsupports.
- [TECGetAvailableTextEncodings](./api-1571819-tecgetavailabletextencodings.md)
  Returns the text encoding specifications currently configuredin the Text Encoding Converter.
- [TECGetSubTextEncodings](./api-1571796-tecgetsubtextencodings.md)
  Returns the text encoding specifications for the subencodingsthe encoding scheme supports. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399736-nearestmactextencodings)*