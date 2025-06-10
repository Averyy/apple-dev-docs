# showsSystemScreenTimeBlockingView

**Framework**: WebKit  
**Kind**: property

Indicates whether the webpage should use the system Screen Time blocking view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+

## Declaration

```swift
@MainActor
var showsSystemScreenTimeBlockingView: Bool { get set }
```

#### Discussion

The default value is `true`. If `true`, the system Screen Time blocking view is shown when blocked by Screen Time. If `false`, a blurred view of the web content is shown instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/showssystemscreentimeblockingview)*