# metadata

**Framework**: HomeExtensions  
**Kind**: property  
**Role**: Instance Property

Additional information that the Home app provides about the content it’s displaying.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final var metadata: [String : String] { get }
```

#### Discussion

You access values in this dictionary with the keys in [`HomeContext.MetadataKey`](./metadatakey.md).

## See Also

### Reading extension metadata
- [HomeContext.MetadataKey](./metadatakey.md)
  Keys for values in the context’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontext/metadata)*