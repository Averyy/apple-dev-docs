# gestaltHardwareAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltHardwareAttr = 'hdwr'
```

#### Discussion

The selector you pass to the Gestalt function to determine low-level hardware configuration attributes.

Never infer the existence of certain hardware or software features from the responses that `Gestalt` returns when you pass it this selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472318-hardware_attribute_attribute_sel/gestalthardwareattr)*