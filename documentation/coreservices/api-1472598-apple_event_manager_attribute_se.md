# Apple Event Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Apple Event Manager.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltAppleEventsAttr](./api-1472598-apple_event_manager_attribute_se/gestaltappleeventsattr.md)
- [gestaltAppleEventsPresent](./api-1472598-apple_event_manager_attribute_se/gestaltappleeventspresent.md)
  A `Gestalt` attribute constant. If the bit specified by this constant is set in the `response` parameter value supplied by `Gestalt` for the `gestaltAppleEventsAttr` selector, the Apple Event Manager is present and installed in the system.
- [gestaltScriptingSupport](./api-1472598-apple_event_manager_attribute_se/gestaltscriptingsupport.md)
- [gestaltOSLInSystem](./api-1472598-apple_event_manager_attribute_se/gestaltoslinsystem.md)
  A `Gestalt` attribute constant. If the bit specified by this constant is set in the `response` parameter value supplied by `Gestalt` for the `gestaltAppleEventsAttr` selector, the Object Support Library (OSL) is part of the system. 
- [gestaltSupportsApplicationURL](./api-1472598-apple_event_manager_attribute_se/gestaltsupportsapplicationurl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472598-apple_event_manager_attribute_se)*