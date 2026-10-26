# Callback Constants for the AEResolve Function

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify supported callback features to the `AEResolve` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kAEIDoMinimum](./api-1572741-callback_constants_for_the_aeres/kaeidominimum.md)
  The application does not handle whose tests or provide marking callbacks.
- [kAEIDoWhose](./api-1572741-callback_constants_for_the_aeres/kaeidowhose.md)
  The application supports whose tests (supports key form `formWhose`).
- [kAEIDoMarking](./api-1572741-callback_constants_for_the_aeres/kaeidomarking.md)
  The application provides marking callback functions. Marking callback functions are described in [Apple Event Manager](../applicationservices/apple_event_manager.md).
- [kAEHandleSimpleRanges](./api-1572741-callback_constants_for_the_aeres/kaehandlesimpleranges.md)
- [kAEPassSubDescs](./api-1572741-callback_constants_for_the_aeres/kaepasssubdescs.md)
- [kAEResolveNestedLists](./api-1572741-callback_constants_for_the_aeres/kaeresolvenestedlists.md)
- [kAEUseRelativeIterators](./api-1572741-callback_constants_for_the_aeres/kaeuserelativeiterators.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1572741-callback_constants_for_the_aeres)*