# ignoresViewportScaleLimits

**Framework**: WebKit  
**Kind**: property

Determines whether a webpage allows scaling of the webpage.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var ignoresViewportScaleLimits: Bool
```

#### Discussion

When set to `true`, this property overrides the user-scalable HTML property in a webpage, and lets the webpage scale its view’s content regardless of the author’s intent.

The default value of this property is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/ignoresviewportscalelimits)*