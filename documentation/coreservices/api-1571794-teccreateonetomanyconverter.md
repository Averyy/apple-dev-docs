# TECCreateOneToManyConverter

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Determines a conversion path for the source encoding anddestinations encodings you specify, creates a text encoding converterobject, and returns a reference to it. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCreateOneToManyConverter(TECObjectRef *newEncodingConverter, TextEncoding inputEncoding, ItemCount numOutputEncodings, const TextEncoding outputEncodings[]);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You use this converter object reference with conversion functionssuch as  [`TECConvertTextToMultipleEncodings`](./api-1571849-tecconverttexttomultipleencoding.md).The converter object describes the source, destination, and intermediateencodings; state information; and references to required plug-ins.

To remove a converter object, you must call the function  [`TECDisposeConverter`](./api-1571839-tecdisposeconverter.md). 

## Parameters

- `newEncodingConverter`: A pointer to a converter object. On return, this points to a newly created one-to-many converter object. 
- `inputEncoding`: The text encoding specification for the source text encoding. 
- `numOutputEncodings`: The number of text encoding specifications in the `outputEncoding` array. 
- `outputEncodings`: An ordered array of text encoding specifications for the destination text encodings.

## See Also

### Converting to Multiple Encoding Runs
- [TECConvertTextToMultipleEncodings](./api-1571849-tecconverttexttomultipleencoding.md)
  Converts text in the source encoding to runs of text inmultiple destination encodings. It uses the conversion path specifiedin the converter object you supply.
- [TECFlushMultipleEncodings](./api-1571842-tecflushmultipleencodings.md)
  Flushes out any encodings that may be stored in a converterobject’s temporary buffers and shifts encodings back to theirdefault state, if any.
- [TECGetEncodingList](./api-1571830-tecgetencodinglist.md)
  Gets the list of destination encodings from a converterobject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571794-teccreateonetomanyconverter)*