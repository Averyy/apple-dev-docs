# preferredDynamicRange

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

Specifies the preferred dynamic range behavior of the tone mapping. The value should be kCIDynamicRangeStandard, kCIDynamicRangeConstrainedHigh, kCIDynamicRangeHigh or nil.  If nil then it will behave as kCIDynamicRangeHigh.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var preferredDynamicRange: CIDynamicRangeOption? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisystemtonemap/preferreddynamicrange)*