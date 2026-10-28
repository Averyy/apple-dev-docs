# kUnicodeDefaultDirectionMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeDefaultDirectionMask = kUnicodeDefaultDirection << kUnicodeDirectionalityBits
```

## Discussion

A mask for setting the global, or base, line direction for the text being converted. The value `kUnicodeDefaultDirectionMask` tells the converter to use the value of the first strong direction character in the string. This determines which direction the converter should use for resolution of neutral coded characters, such as spaces that occur between sets of coded characters having different directions—for example, between Latin and Arabic characters—rendering ambiguous the direction of the space character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433620-directionality_masks/kunicodedefaultdirectionmask)*