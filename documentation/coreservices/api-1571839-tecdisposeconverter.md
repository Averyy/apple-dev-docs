# TECDisposeConverter

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes of a converter object.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECDisposeConverter(TECObjectRef newEncodingConverter);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

If you want to reuse the converter object for a differenttext stream with the same source and destination encoding, you shouldclear the converter object using the  [`TECClearConverterContextInfo`](./api-1571844-tecclearconvertercontextinfo.md)  functionrather than disposing of it and then creating a new converter object. 

## Parameters

- `newEncodingConverter`: A reference to the text encoding converter object you want to remove. This can be the reference returned by the [`TECCreateConverter`](./api-1571815-teccreateconverter.md), [`TECCreateConverterFromPath`](./api-1571829-teccreateconverterfrompath.md), or [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md) functions. 

## See Also

### Creating and Deleting Converter Objects
- [TECCreateConverter](./api-1571815-teccreateconverter.md)
  Determines a conversion path for a source and destinationencoding, then creates a text encoding converter object and returnsa pointer to it. 
- [TECCreateConverterFromPath](./api-1571829-teccreateconverterfrompath.md)
  Creates a converter object for a specific conversion path—froma source encoding through intermediate encodings to a destinationencoding—and returns a pointer to it. 
- [TECClearConverterContextInfo](./api-1571844-tecclearconvertercontextinfo.md)
  Resets a converter object to its initial state so youcan reuse it. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571839-tecdisposeconverter)*