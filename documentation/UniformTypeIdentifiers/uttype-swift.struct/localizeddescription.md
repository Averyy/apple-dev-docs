# localizedDescription

**Framework**: Uniform Type Identifiers  
**Kind**: property

A localized description of the type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var localizedDescription: String? { get }
```

#### Discussion

If the type doesn’t provide a description, the system searches its supertypes. A dynamic type doesn’t have localized description, even if its supertypes do.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/localizeddescription)*