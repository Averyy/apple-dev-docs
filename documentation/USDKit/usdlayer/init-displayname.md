# init(displayName:)

**Framework**: USDKit  
**Kind**: init

Creates an anonymous, in-memory layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(displayName: String? = nil) throws
```

#### Discussion

Anonymous layers have no file backing.

> **Note**: An error if the layer cannot be created.

## Parameters

- `displayName`: A non-unique hint shown in debug output and logs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/init(displayname:))*