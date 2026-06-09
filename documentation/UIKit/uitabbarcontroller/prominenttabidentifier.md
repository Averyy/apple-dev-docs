# prominentTabIdentifier

**Framework**: UIKit  
**Kind**: property

The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var prominentTabIdentifier: String? { get set }
```

#### Discussion

Default is nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/prominenttabidentifier)*