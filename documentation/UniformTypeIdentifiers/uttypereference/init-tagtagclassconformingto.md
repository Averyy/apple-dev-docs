# init(tag:tagClass:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: init

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
convenience init?(tag: String, tagClass: String, conformingTo supertype: UTType?)
```

#### Return Value

A type. If no types are known to the system with the specified tag but the inputs were otherwise valid, a dynamic type may be provided. If the inputs were not valid, returns \c nil.

#### Discussion

Create a type given a type tag.

## Parameters

- `tag`: The tag, such as the path extension, for which a type is desired.
- `tagClass`: The class of the tag, such as \c UTTagClassFilenameExtension.
- `supertype`: Another type that the resulting type must conform to. If \c nil, no conformance is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(tag:tagclass:conformingto:))*