# ColorSync Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the ColorSync Manager.

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
- [gestaltColorMatchingAttr](./api-1473015-colorsync_manager_attribute_sele/gestaltcolormatchingattr.md)
  The selector for obtaining version information. Use when calling the `Gestalt` function to check for particular ColorSync Manager features.
- [gestaltHighLevelMatching](./api-1473015-colorsync_manager_attribute_sele/gestalthighlevelmatching.md)
  This constant is provided for backward compatibility only. Bit 0 of the `Gestalt` response value is always set if ColorSync is present.
- [gestaltColorMatchingLibLoaded](./api-1473015-colorsync_manager_attribute_sele/gestaltcolormatchinglibloaded.md)
  This constant is provided for backward compatibility only. Bit 1 of the `Gestalt` response value is always set on a Power Macintosh machine if ColorSync is present. It is always cleared on a 68K machine if ColorSync is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473015-colorsync_manager_attribute_sele)*