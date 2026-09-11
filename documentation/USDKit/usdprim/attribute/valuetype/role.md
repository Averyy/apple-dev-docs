# role

**Framework**: USDKit  
**Kind**: property

The name of this type’s role, if it has one.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var role: USDToken { get }
```

#### Discussion

Roles clarify the semantic purpose of a type. For example, the type `point3f` stores the same data as its base type `float3`, but it also has the role “Point”, which means that it stores 3D positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/valuetype/role)*