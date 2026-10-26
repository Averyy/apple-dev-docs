# AppleScript Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for AppleScript.

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
- [gestaltAppleScriptAttr](./api-1472032-applescript_attribute_selectors/gestaltapplescriptattr.md)
- [gestaltAppleScriptPresent](./api-1472032-applescript_attribute_selectors/gestaltapplescriptpresent.md)
  A `Gestalt` attribute constant. If the bit specified by this constant is set in the `response` parameter value supplied by `Gestalt` for the `gestaltAppleScriptAttr` selector, AppleScript is present.
- [gestaltAppleScriptPowerPCSupport](./api-1472032-applescript_attribute_selectors/gestaltapplescriptpowerpcsupport.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472032-applescript_attribute_selectors)*