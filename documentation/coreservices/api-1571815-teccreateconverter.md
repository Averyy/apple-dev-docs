# TECCreateConverter

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Determines a conversion path for a source and destinationencoding, then creates a text encoding converter object and returnsa pointer to it. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCreateConverter(TECObjectRef *newEncodingConverter, TextEncoding inputEncoding, TextEncoding outputEncoding);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You use this converter object reference with conversion functionssuch as  [`TECConvertText`](./api-1571824-tecconverttext.md)  toconvert text. This converter object describes the source, destination,and intermediate encodings; state information; and references torequired plug-ins.

If the function does not find a direct conversion path, itcreates an indirect conversion path. You can use the function  [`TECCreateConverterFromPath`](./api-1571829-teccreateconverterfrompath.md) to specify an explicit conversion path. 

You must use the  [`TECDisposeConverter`](./api-1571839-tecdisposeconverter.md) function to remove a converter object. 

## Parameters

- `newEncodingConverter`: A pointer to a converter object. On return, this reference points to a newly created text converter object. 
- `inputEncoding`: The text encoding specification for the source text encoding. 
- `outputEncoding`: The text encoding specification for the destination text encoding.

## See Also

### Creating and Deleting Converter Objects
- [TECCreateConverterFromPath](./api-1571829-teccreateconverterfrompath.md)
  Creates a converter object for a specific conversion path—froma source encoding through intermediate encodings to a destinationencoding—and returns a pointer to it. 
- [TECClearConverterContextInfo](./api-1571844-tecclearconvertercontextinfo.md)
  Resets a converter object to its initial state so youcan reuse it. 
- [TECDisposeConverter](./api-1571839-tecdisposeconverter.md)
  Disposes of a converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571815-teccreateconverter)*