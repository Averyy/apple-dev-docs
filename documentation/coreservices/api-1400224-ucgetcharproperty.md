# UCGetCharProperty

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the value associated with a property type forthe specified `UniChar` characters.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus UCGetCharProperty(const UniChar *charPtr, UniCharCount textLength, UCCharPropertyType propType, UCCharPropertyValue *propValue);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Parameters

- `charPtr`: A pointer to the Unicode text whose property value you want to obtain.
- `textLength`: The length of the text pointed to by `charPtr`.
- `propType`: The property type for the `UniChar` character whose value you want to obtain. See [`UCCharPropertyType`](./uccharpropertytype.md) for a list of the constants you can supply.
- `propValue`: On return, the value associated with the property type specified by the `propType` parameter. See [`UCCharPropertyValue`](./uccharpropertyvalue.md) for a list of the constants that can be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400224-ucgetcharproperty)*