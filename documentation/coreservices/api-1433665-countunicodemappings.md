# CountUnicodeMappings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts available mappings that meet the specified matchingcriteria.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus CountUnicodeMappings(OptionBits iFilter, ConstUnicodeMappingPtr iFindMapping, ItemCount *oActualCount);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You can filter on any of the three text encoding subfieldsof the Unicode mapping structure’s `unicodeEncoding` specificationand on any of the three text encoding subfields of the structure’s `otherEncoding` specification.The `iFilter` parameterconsists of a set of six control flags that you set to identifywhich of the corresponding six subfields to include in the matchcount. No filtering is performed on fields for which you do notset the corresponding filter control flag.  

## Parameters

- `iFilter`: Filter control flags representing the six subfields of the Unicode mapping structure that this function uses to match against in determining which mappings on the system to return to your application. The filter control enumeration, described in [Unicode Matching Masks](./api-1433554-unicode_matching_masks.md), define the constants for the subfield’s flags and their masks. You can include in the search criteria any of the three text encoding subfields for both the Unicode encoding and the other specified encoding. For any flag not turned on, the subfield value is ignored and the function does not check the corresponding subfield of the mappings on the system. 
- `iFindMapping`: A structure of type [`UnicodeMapping`](./unicodemapping.md) containing the text encodings whose field values are to be matched. 
- `oActualCount`: On return, a pointer to the number of matching mappings found. 

## See Also

### Obtaining Unicode Mapping Information 
- [QueryUnicodeMappings](./api-1433630-queryunicodemappings.md)
  Returns a list of the conversion mappings available onthe system that meet specified matching criteria and returns thenumber of mappings found. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433665-countunicodemappings)*