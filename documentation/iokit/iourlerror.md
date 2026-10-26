# IOURLError

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct IOURLError
```

```c
typedef enum IOURLError : int {
    ...
} IOURLError;
```

## Topics

### Initializers
- [init(Int32)](./iourlerror/api-1514691-init.md)
- [init(rawValue: Int32)](./iourlerror/api-1514762-init.md)
### Instance Properties
- [var rawValue: Int32](./iourlerror/api-1514452-rawvalue.md)
### Constants
- [kIOURLImproperArgumentsError](./iourlerror/kiourlimproperargumentserror.md)
- [kIOURLPropertyKeyUnavailableError](./iourlerror/kiourlpropertykeyunavailableerror.md)
- [kIOURLRemoteHostUnavailableError](./iourlerror/kiourlremotehostunavailableerror.md)
- [kIOURLResourceAccessViolationError](./iourlerror/kiourlresourceaccessviolationerror.md)
- [kIOURLResourceNotFoundError](./iourlerror/kiourlresourcenotfounderror.md)
- [kIOURLTimeoutError](./iourlerror/kiourltimeouterror.md)
- [kIOURLUnknownError](./iourlerror/kiourlunknownerror.md)
- [kIOURLUnknownPropertyKeyError](./iourlerror/kiourlunknownpropertykeyerror.md)
- [kIOURLUnknownSchemeError](./iourlerror/kiourlunknownschemeerror.md)

## Relationships

### Conforms To
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iourlerror)*