# transformOperations

**Framework**: USDKit  
**Kind**: property

The transform operations on this prim, in evaluation order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var transformOperations: [USDTransformOperation] { get }
```

#### Discussion

Returns an empty array if no transform operations are authored on the prim or if the prim does not conform to the Xformable schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/transformoperations)*