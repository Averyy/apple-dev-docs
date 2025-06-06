# cmLong8ColorPacking

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmLong8ColorPacking: Int { get }
```

#### Discussion

The color values for three or four 8-bit color channels are stored consecutively in a 32-bit long. For three channels, this constant is combined with either `cmAlphaFirstPacking` or `cmAlphaLastPacking` to indicate whether the unused eight bits are located at the beginning or end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmlong8colorpacking)*