# gestaltATSUFeatures

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltATSUFeatures = 'uisf'
```

#### Discussion

Specifies the ATSUI features available on the user’s system. You pass this selector to the `Gestalt` function. On return, the `Gestalt` function passes back a value that represents the features available in the version of ATSUI installed on the user’s system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471588-atsui_attribute_selectors/gestaltatsufeatures)*