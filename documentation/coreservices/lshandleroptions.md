# LSHandlerOptions

**Framework**: Core Services  
**Kind**: struct

The specification that controls the selection of handlers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
struct LSHandlerOptions
```

## Topics

### Creating Content Handler Options
- [init(rawValue: OptionBits)](lshandleroptions/1442692-init.md)
### Constants
- [static var ignoreCreator: LSHandlerOptions](lshandleroptions/1445418-ignorecreator.md)
  When set, causes Launch Services to ignorethe content item’s creator when selecting a role handler for thespecified content type.

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lshandleroptions)*