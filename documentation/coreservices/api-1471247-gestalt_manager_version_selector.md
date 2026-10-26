# Gestalt Manager Version Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify Gestalt Manager version information. 

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
- [gestaltVersion](./api-1471247-gestalt_manager_version_selector/gestaltversion.md)
  The selector you pass to the function [`Gestalt`](./api-1471624-gestalt.md) to determine the version of the Gestalt Manager. The function passes back the version in the low-order word of the response. 
- [gestaltValueImplementedVers](./api-1471247-gestalt_manager_version_selector/gestaltvalueimplementedvers.md)
  The first version of the Gestalt Manager that implements this selector. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471247-gestalt_manager_version_selector)*