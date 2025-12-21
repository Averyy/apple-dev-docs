# showsSystemScreenTimeBlockingView

**Framework**: WebKit  
**Kind**: property

Indicates whether the webpage should use the system Screen Time blocking view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
@MainActor
var showsSystemScreenTimeBlockingView: Bool { get set }
```

#### Discussion

The default value is `true`. If `true`, the system Screen Time blocking view is shown when blocked by Screen Time. If `false`, a blurred view of the web content is shown instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/showssystemscreentimeblockingview)*