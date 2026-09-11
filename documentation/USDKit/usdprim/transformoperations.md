# transformOperations

**Framework**: USDKit  
**Kind**: property

The transform operations on this prim, in evaluation order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var transformOperations: [USDTransformOperation] { get }
```

#### Discussion

Returns an empty array if no transform operations are authored on the prim or if the prim does not conform to the Xformable schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/transformoperations)*