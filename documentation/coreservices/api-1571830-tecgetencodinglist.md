# TECGetEncodingList

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the list of destination encodings from a converterobject.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetEncodingList(TECObjectRef encodingConverter, ItemCount *numEncodings, Handle *encodingList);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

The `TECDisposeConverter` functionautomatically disposes of the pointer for you. This means you shouldnot reference the pointer after you have disposed of the converter object. 

Plug-ins that perform one-to-many conversions use the `TECGetEncodingList` functionto get the output encoding list from the converter object reference. 

## Parameters

- `encodingConverter`: A reference to the text encoding conversion object returned by the [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md) function. 
- `numEncodings`: On return, a pointer to the number of encodings specified by the `encodingList` handle. 
- `encodingList`: A handle to an array of text encoding specifications. On return, it contains an array of text encoding specifications to which the converter object can convert. The memory for the array is allocated automatically by the Text Encoding Converter. 

## See Also

### Converting to Multiple Encoding Runs
- [TECConvertTextToMultipleEncodings](./api-1571849-tecconverttexttomultipleencoding.md)
  Converts text in the source encoding to runs of text inmultiple destination encodings. It uses the conversion path specifiedin the converter object you supply.
- [TECCreateOneToManyConverter](./api-1571794-teccreateonetomanyconverter.md)
  Determines a conversion path for the source encoding anddestinations encodings you specify, creates a text encoding converterobject, and returns a reference to it. 
- [TECFlushMultipleEncodings](./api-1571842-tecflushmultipleencodings.md)
  Flushes out any encodings that may be stored in a converterobject’s temporary buffers and shifts encodings back to theirdefault state, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571830-tecgetencodinglist)*