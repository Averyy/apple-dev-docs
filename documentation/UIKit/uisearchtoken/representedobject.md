# representedObject

**Framework**: UIKit  
**Kind**: property

The object represented by the search token.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var representedObject: Any? { get set }
```

#### Discussion

Use this property to keep information required to restore a search from state restoration, paste a search token, or perform the user’s search.

## See Also

- [init(icon: UIImage?, text: String)](uisearchtoken/init(icon:text:).md)
  Creates a search token with the specified text and icon (if any).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtoken/representedobject)*