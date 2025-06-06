# cmQualityMask

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmQualityMask: Int { get }
```

#### Discussion

This mask provides access to bits 16 and 17 of the `flags` field, which specify the preferred quality and speed preferences for color matching. In general, the higher the quality the slower the speed. For example, best quality is slowest, but produces the highest quality result.

Bits 16 and 17 have the value 0 for normal quality, 1 for draft quality, and 2 for best quality. [`Quality Flag Values for Version 2.x Profiles`](colorsync_manager/1560115-quality_flag_values_for_version_.md) describes the constants ColorSync defines to test or set these bits.

This feature is provided by the ColorSync Manager; it is not defined by the ICC profile specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmqualitymask)*