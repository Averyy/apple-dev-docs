# TECCreateConverterFromPath

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a converter object for a specific conversion path—froma source encoding through intermediate encodings to a destinationencoding—and returns a pointer to it. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCreateConverterFromPath(TECObjectRef *newEncodingConverter, const TextEncoding inPath[], ItemCount inEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

This function is faster than the function  [`TECCreateConverter`](./api-1571815-teccreateconverter.md)  since it does notneed to search for a conversion path. You can use the  [`TECGetDestinationTextEncodings`](./api-1571808-tecgetdestinationtextencodings.md) function to determine each step in the sequence from the sourceto the destination encoding.

To remove a converter object, you must call the function  [`TECDisposeConverter`](./api-1571839-tecdisposeconverter.md). 

## Parameters

- `newEncodingConverter`: A pointer to a converter object reference. On return, the reference points to a newly created text converter object. 
- `inPath`: An ordered array of text encoding specifications, beginning with the source encoding specification and ending with the destination encoding specification. Each adjacent pair of text encodings must represent a conversion that is supported by the Text Encoding Converter. 
- `inEncodings`: The number of text encoding specifications in the `inPath` array. 

## See Also

### Creating and Deleting Converter Objects
- [TECCreateConverter](./api-1571815-teccreateconverter.md)
  Determines a conversion path for a source and destinationencoding, then creates a text encoding converter object and returnsa pointer to it. 
- [TECClearConverterContextInfo](./api-1571844-tecclearconvertercontextinfo.md)
  Resets a converter object to its initial state so youcan reuse it. 
- [TECDisposeConverter](./api-1571839-tecdisposeconverter.md)
  Disposes of a converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571829-teccreateconverterfrompath)*