# TECCountDirectTextEncodingConversions

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts and returns the number of direct conversions currentlyconfigured in the Text Encoding Converter.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCountDirectTextEncodingConversions(ItemCount *numberOfEncodings);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

The number of direct conversions includes every instance ofa conversion. If different conversion plug-ins support the samedirect conversion, the direct conversion is counted more than once.

Since the  [`TECGetDirectTextEncodingConversions`](./api-1571834-tecgetdirecttextencodingconversi.md) function ignores duplicate direct conversions, `TECCountDirectTextEncodingConversions` mayreturn a number greater than the number of array elements neededfor the `directConversions` parameter. 

## Parameters

- `numberOfEncodings`: On return, a pointer to the number of direct conversions. You should use this value to determine the array size for a parameter of the [`TECGetDirectTextEncodingConversions`](./api-1571834-tecgetdirecttextencodingconversi.md) function. 

## See Also

### Identifying Direct Encoding Conversions 
- [TECGetDirectTextEncodingConversions](./api-1571834-tecgetdirecttextencodingconversi.md)
  Returns the types of direct conversions currently configuredin the Text Encoding Converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571822-teccountdirecttextencodingconver)*