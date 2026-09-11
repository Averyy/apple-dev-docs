# loadRule(_:)

**Framework**: USDKit  
**Kind**: method

Specifies the rule used to determine if referenced payloads are loaded.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func loadRule(_ rule: USDStage.InitialLoadRule) -> USDStage.OpenOptions
```

#### Discussion

The default is `.all`, so all loadable prims will be automatically loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/openoptions/loadrule(_:))*