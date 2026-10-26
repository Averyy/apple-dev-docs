# LSHandlerOptions

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

The specification that controls the selection of handlers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
struct LSHandlerOptions
```

```c
typedef enum LSHandlerOptions : OptionBits {
    ...
} LSHandlerOptions;
```

## Topics

### Creating Content Handler Options
- [init(rawValue: OptionBits)](./lshandleroptions/api-1442692-init.md)
### Constants
- [static var ignoreCreator: LSHandlerOptions](./lshandleroptions/api-1445418-ignorecreator.md)
  When set, causes Launch Services to ignorethe content item’s creator when selecting a role handler for thespecified content type.
- [kLSHandlerOptionsDefault](./lshandleroptions/klshandleroptionsdefault.md)
  When set, causes Launch Services to use a contentitem’s creator (when available) to select a handler. This is thedefault setting.
- [kLSHandlerOptionsIgnoreCreator](./lshandleroptions/klshandleroptionsignorecreator.md)
  When set, causes Launch Services to ignorethe content item’s creator when selecting a role handler for thespecified content type.

## Relationships

### Conforms To
- [OptionSet](../Swift/optionset.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lshandleroptions)*