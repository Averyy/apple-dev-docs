# HomeAccessoryHelpGuide.SupportsAccessory

**Framework**: HomeExtensions  
**Kind**: typealias  
**Role**: Type Alias

A closure that determines whether a help guide applies to an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
typealias SupportsAccessory = @isolated(any) @Sendable (HMAccessory) -> Bool
```

## See Also

### Creating a help guide
- [init(id: HomeContentID, content: () -> some View, filter: HomeAccessoryHelpGuide.SupportsAccessory)](./init%28id,content,filter%29.md)
  Creates a help guide with an identifier and a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryhelpguide/supportsaccessory)*