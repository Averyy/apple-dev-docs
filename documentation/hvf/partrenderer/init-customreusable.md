# init(custom:reusable:)

**Framework**: hvf  
**Kind**: init

Use a custom, client-defined loader Setting reusable to true preserves the input parameter values when rendering; otherwise they are destroyed by rendering

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
init(custom: @escaping CustomPartLoader, reusable: Bool = false)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/init(custom:reusable:))*