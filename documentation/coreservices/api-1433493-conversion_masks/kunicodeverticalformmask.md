# kUnicodeVerticalFormMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeVerticalFormMask = 1L << kUnicodeVerticalFormBit
```

#### Discussion

A mask for setting the vertical form control flag. The vertical form control flag tells the Unicode Converter how to map text elements for which there are both abstract and vertical presentation forms in the destination encoding. 

If set, the converter maps these text elements to their vertical forms, if they are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodeverticalformmask)*