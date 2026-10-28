# QueryUnicodeMappings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns a list of the conversion mappings available onthe system that meet specified matching criteria and returns thenumber of mappings found. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus QueryUnicodeMappings(OptionBits iFilter, ConstUnicodeMappingPtr iFindMapping, ItemCount iMaxCount, ItemCount *oActualCount, UnicodeMapping oReturnedMappings[]);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). If the function returnsa `noErr` result code,the value retuned in the `oActualCount` parameteris less than or equal to the value returned in the `iMaxCount` parameterand the `oReturnedMappings` parametercontains all of the matching mappings found. If the function returnsa `kTECArrayFullErr`, thefunction found more mappings than your `oReturnedMappings` arraycould accommodate.

## Discussion

You can use the `QueryUnicodeMappings` functionto obtain all mappings on the system up to the number allowed byyour `oReturnedMappings` arrayby specifying a value of zero for the `iFilter` field. 

You can use the function to obtain very specific mappingsby setting individual filter control flags. You can filter on anyof the three text encoding subfields of the Unicode mapping structure’s `unicodeEncoding` specificationand on any of the three text encoding subfields of the mapping’s `otherEncoding` specification.The `iFilter` parameterconsists of a set of six control flags that you set to identifywhich of the corresponding six subfields to include in the match.The list provided in the `oReturnedMappings` parameterwill contain only mappings that match the fields of the Unicodemapping structure whose text encodings subfields you identify inthe filter control flags. No filtering is performed on subfieldsfor which you do not set the corresponding filter control flag. 

For example, to obtain a list of all mappings in which oneof the encodings is the default variant and default format of theUnicode 1.1 base encoding and the other encoding is the defaultvariant and default format of a base encoding other than Unicode,you would set up the `iFilter` and `iFindMappings` parameteras follows. To set up these parameters, you use the constants definedfor the text encoding bases, the text encoding default variants, thetext encoding default formats, and the filter control flag bitmasks.In this example, the text encoding base field of the Unicode mappingstructure’s `otherEncoding` fieldis ignored, so you can specify any value for it. When you call `QueryUnicodeMappings`,passing it these parameters, the function will return a list ofmappings between the Unicode encoding you specified and every otheravailable encoding in which each non-Unicode base encoding showsup once because you specified its default variant and default format. 

```occ
iFindMapping.unicodeMapping = CreateTextEncoding(
kTextEncodingUnicodeV1_1,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat);
iFindMapping.otherEncoding = CreateTextEncoding(
kTextEncodingMacRoman,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat);
iFilter = kUnicodeMatchUnicodeBaseMask |
kUnicodeMatchUnicodeVariantMask |
kUnicodeMatchUnicodeFormatMask |
kUnicodeMatchOtherVariantMask |
kUnicodeMatchOtherFormatMask;
```

## Parameters

- `iFilter`: Filter control flags representing the six values given in the Unicode mapping structure that this function uses to match against in determining which mappings on the system to return to your application. The filter control flag enumerations, described in [Unicode Matching Masks](./api-1433554-unicode_matching_masks.md), define the constants for the flags and their masks. You can include in the search criteria any of the three text encoding values—base, variant, and format—for both the Unicode encoding and the other specified encoding. For any flag not turned on, the value is ignored the function does not check the corresponding value of the mapping tables on the system. 
- `iFindMapping`: A structure of type [`UnicodeMapping`](./unicodemapping.md) containing the text encodings whose values are to be matched. 
- `iMaxCount`: The maximum number of mappings that can be returned. You provide this value to identify the number of elements in the array pointed to by the `oReturnedMappings` parameter that your application allocated. If the function identifies more matching mappings than the array can hold, it returns as many of them as fit. The function also returns a `kTECArrayFullErr` in this case. 
- `oActualCount`: On return, a pointer to the number of matching mappings found. This number may be greater than the number of mappings specified by `iMaxCount` if more matching mappings are found than can fit in the `oReturnedMappings` array.
- `oReturnedMappings`: A pointer to an array of structures of type [`UnicodeMapping`](./unicodemapping.md). On input, this pointer refers to an array for the matching mappings returned by the function. To allocate sufficient elements for the array, you can use the function [`CountUnicodeMappings`](./api-1433665-countunicodemappings.md) to determine the number of mappings returned for given values of the `iFilter` and `iFindMapping` parameters. On return, a pointer to an array that holds the matching mappings. If there are more matches than the array can hold, the function returns as many of them as will fit and a `kTECBufferBelowMinimumSizeErr` error result. The `oActualCount` parameter identifies the number of matching mappings actually found, which may be greater than the number returned. 

## See Also

### Obtaining Unicode Mapping Information 
- [CountUnicodeMappings](./api-1433665-countunicodemappings.md)
  Counts available mappings that meet the specified matchingcriteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433630-queryunicodemappings)*