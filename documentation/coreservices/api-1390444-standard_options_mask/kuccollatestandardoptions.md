# kUCCollateStandardOptions

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kUCCollateStandardOptions = kUCCollateComposeInsensitiveMask | kUCCollateWidthInsensitiveMask
```

## Discussion

If the `kUCCollateComposeInsensitiveMask` and `kUCCollateWidthInsensitiveMask` bits are set, then (1) precomposed and decomposed representations of the same text element will be treated as equivalent, and (2) fullwidth and halfwidth compatibility forms will be treated as equivalent to the corresponding non-compatibility characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390444-standard_options_mask/kuccollatestandardoptions)*