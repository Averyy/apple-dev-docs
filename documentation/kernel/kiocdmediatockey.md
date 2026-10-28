# kIOCDMediaTOCKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

kIOCDMediaTOCKey is a property of IOCDMedia objects. It has an OSData value and a CDTOC structure.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOCDMediaTOCKey
```

## Discussion

The kIOCDMediaTOCKey property contains the CD's full table of contents, formatted as a CDTOC structure. The CDTOC structure is same as what is returned by a READ TOC command, format 0x02. All fields in the TOC are guaranteed to be binary-encoded (no BCD-encoded numbers are ever passed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiocdmediatockey)*