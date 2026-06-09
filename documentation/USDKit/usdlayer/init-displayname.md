# init(displayName:)

**Framework**: USDKit  
**Kind**: init

Creates an anonymous, in-memory layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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