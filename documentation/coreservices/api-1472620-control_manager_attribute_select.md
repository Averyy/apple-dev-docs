# Control Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Control Manager.

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
- [gestaltControlMgrAttr](./api-1472620-control_manager_attribute_select/gestaltcontrolmgrattr.md)
- [gestaltControlMgrPresent](./api-1472620-control_manager_attribute_select/gestaltcontrolmgrpresent.md)
  If the bit specified by this mask is set, the Control Manager functionality for Appearance Manager 1.1 is available. This bit is set for Mac OS 8.5 and later.
- [gestaltControlMgrPresentBit](./api-1472620-control_manager_attribute_select/gestaltcontrolmgrpresentbit.md)
- [gestaltControlMsgPresentMask](./api-1472620-control_manager_attribute_select/gestaltcontrolmsgpresentmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472620-control_manager_attribute_select)*