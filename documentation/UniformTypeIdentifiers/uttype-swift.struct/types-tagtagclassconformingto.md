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
static func types(tag: String, tagClass: UTTagClass, conformingTo supertype: UTType?) -> [UTType]
```

#### Discussion

If the system doesn’t find any types with the provided tag but the inputs were otherwise valid, it may provide a dynamic type. The initializer returns an empty array if the inputs aren’t valid.

## Parameters

- `tag`: The tag, such as a filename extension.
- `tagClass`: The tag class, such as  .
- `supertype`: Another type to which resulting types must conform. A value of   indicates that conformance isn’t required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/types(tag:tagclass:conformingto:))*