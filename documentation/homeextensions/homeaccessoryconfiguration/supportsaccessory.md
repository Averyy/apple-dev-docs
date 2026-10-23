# HomeAccessoryConfiguration.SupportsAccessory

**Framework**: HomeExtensions  
**Kind**: typealias  
**Role**: Type Alias

A closure that determines whether content applies to an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
typealias SupportsAccessory = @isolated(any) @Sendable (HMAccessory) -> Bool
```

## See Also

### Creating an accessory configuration
- [init(id: HomeContentID, content: () -> some View, filter: HomeAccessoryConfiguration.SupportsAccessory)](./init%28id,content,filter%29.md)
  Creates a configuration with an identifier and a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryconfiguration/supportsaccessory)*