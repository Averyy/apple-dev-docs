# role

**Framework**: USDKit  
**Kind**: property

The name of this type’s role, if it has one.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var role: USDToken { get }
```

#### Discussion

Roles clarify the semantic purpose of a type. For example, the type `point3f` stores the same data as its base type `float3`, but it also has the role “Point”, which means that it stores 3D positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/valuetype/role)*