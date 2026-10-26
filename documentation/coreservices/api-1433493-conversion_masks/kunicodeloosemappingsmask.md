# kUnicodeLooseMappingsMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeLooseMappingsMask = 1L << kUnicodeLooseMappingsBit
```

#### Discussion

A mask that determines whether the Unicode Converter should use the loose-mapping portion of a mapping table for character mapping if the strict mapping portion of the table does not include a destination encoding equivalent for the source text element. 

If you clear this flag, the converter will use only the strict equivalence portion. 

 If set this flag and a conversion for the source text element does not exist in the strict equivalence portion of the mapping table, then the converter uses the loose mapping section. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodeloosemappingsmask)*