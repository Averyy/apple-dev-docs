# LSAcceptanceFlags

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

The specification that determines whether an app can accept (open) an item.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSAcceptanceFlags
```

```c
typedef enum LSAcceptanceFlags : OptionBits {
    ...
} LSAcceptanceFlags;
```

#### Overview

These flags are passed to the functions `LSCanRefAcceptItem` and `LSCanURLAcceptURL`.

## Topics

### Creating Acceptance Flags
- [init(rawValue: OptionBits)](./lsacceptanceflags/api-1443753-init.md)
  Creates a new acceptance flag from the given raw value.
### Constants
- [static var acceptDefault: LSAcceptanceFlags](./lsacceptanceflags/api-1447965-acceptdefault.md)
  Requests the default behavior that does not require the user interface to log in be presented.
- [static var acceptAllowLoginUI: LSAcceptanceFlags](./lsacceptanceflags/api-1443098-acceptallowloginui.md)
  Requests that the user interface to log in be presented.
- [kLSAcceptDefault](./lsacceptanceflags/klsacceptdefault.md)
  Requests the default behavior that does not require the user interface to log in be presented.
- [kLSAcceptAllowLoginUI](./lsacceptanceflags/klsacceptallowloginui.md)
  Requests that the user interface to log in be presented.

## Relationships

### Conforms To
- [OptionSet](../Swift/optionset.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsacceptanceflags)*