# kIOFWMustHaveGap63

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIOFWMustHaveGap63 = (1 << 7)
```

#### Discussion

Attempt to ensure the gap count is 63, when this device is on the bus. Gap 63 reduces bus performance significantly, so this flag should be used only when absolutely necessary. There is no guarentee Mac OS will succeed in forcing the gap count to 63.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645951-anonymous/kiofwmusthavegap63)*