# isHDREnabled

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
var isHDREnabled: Bool { get }
```

```objc
@property (readonly, getter=isHDREnabled) BOOL HDREnabled;
```

## Discussion

If high dynamic range (HDR) support is enabled for the display.

When YES, HDR content will be shown when the display’s first responder view is on a HDR capable display. Otherwise only standard dynamic range (SDR) content will be shown. Value is set by VZMacGraphicsDisplayConfiguration. Requires guest macOS 27.3 or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdisplay/ishdrenabled)*