# TECClearConverterContextInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Resets a converter object to its initial state so youcan reuse it. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECClearConverterContextInfo(TECObjectRef encodingConverter);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

It is more efficient to reuse an existing converter objectthan to create a new one that contains the same conversion information.This function clears the text string, but does not alter the sourceand destination encodings. 

If you are converting multiple segments of a text string,you should not clear the converter object until you have convertedall the text segments.  

## Parameters

- `encodingConverter`: A reference to the text encoding converter object you want to reset. It can be a reference returned by the [`TECCreateConverter`](./api-1571815-teccreateconverter.md), [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md), or [`TECCreateConverterFromPath`](./api-1571829-teccreateconverterfrompath.md) functions. 

## See Also

### Creating and Deleting Converter Objects
- [TECCreateConverter](./api-1571815-teccreateconverter.md)
  Determines a conversion path for a source and destinationencoding, then creates a text encoding converter object and returnsa pointer to it. 
- [TECCreateConverterFromPath](./api-1571829-teccreateconverterfrompath.md)
  Creates a converter object for a specific conversion path—froma source encoding through intermediate encodings to a destinationencoding—and returns a pointer to it. 
- [TECDisposeConverter](./api-1571839-tecdisposeconverter.md)
  Disposes of a converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571844-tecclearconvertercontextinfo)*