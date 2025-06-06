# types(tag:tagClass:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: method

Returns an array of types from the provided tag and tag class.

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
class func types(tag: String, tagClass: String, conformingTo supertype: UTType?) -> [UTType]
```

## Parameters

- `tag`: The desired tag, such as a filename extension.
- `tagClass`: The tag class, such as  .
- `supertype`: Another type that the resulting type must conform to; for example,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/types(tag:tagclass:conformingto:))*