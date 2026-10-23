# HomeAccessoryTroubleshooting.SupportsAccessory

**Framework**: HomeExtensions  
**Kind**: typealias  
**Role**: Type Alias

A closure that determines whether troubleshooting content applies to an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
typealias SupportsAccessory = @isolated(any) @Sendable (HMAccessory) -> Bool
```

## See Also

### Creating troubleshooting content
- [init(content: () -> some View, filter: HomeAccessoryTroubleshooting.SupportsAccessory)](./init%28content,filter%29.md)
  Creates troubleshooting content with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytroubleshooting/supportsaccessory)*