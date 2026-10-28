# cmLong8ColorPacking

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
cmLong8ColorPacking = 0x0800
```

## Discussion

The color values for three or four 8-bit color channels are stored consecutively in a 32-bit long. For three channels, this constant is combined with either `cmAlphaFirstPacking` or `cmAlphaLastPacking` to indicate whether the unused eight bits are located at the beginning or end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmlong8colorpacking)*