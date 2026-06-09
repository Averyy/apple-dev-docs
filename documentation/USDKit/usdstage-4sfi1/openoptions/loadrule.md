# loadRule(_:)

**Framework**: USDKit  
**Kind**: method

Specifies the rule used to determine if referenced payloads are loaded.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func loadRule(_ rule: USDStage.InitialLoadRule) -> USDStage.OpenOptions
```

#### Discussion

The default is `.all`, so all loadable prims will be automatically loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/openoptions/loadrule(_:))*