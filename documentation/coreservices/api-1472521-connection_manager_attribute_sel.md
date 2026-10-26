# Connection Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Connection Manager.

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
- [gestaltConnMgrAttr](./api-1472521-connection_manager_attribute_sel/gestaltconnmgrattr.md)
- [gestaltConnMgrPresent](./api-1472521-connection_manager_attribute_sel/gestaltconnmgrpresent.md)
- [gestaltConnMgrCMSearchFix](./api-1472521-connection_manager_attribute_sel/gestaltconnmgrcmsearchfix.md)
  The `gestaltConnMgrCMSearchFix` bit flag indicates that the fix is present that allows the `CMAddSearch` function to work over the `mAttn` channel.
- [gestaltConnMgrErrorString](./api-1472521-connection_manager_attribute_sel/gestaltconnmgrerrorstring.md)
- [gestaltConnMgrMultiAsyncIO](./api-1472521-connection_manager_attribute_sel/gestaltconnmgrmultiasyncio.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472521-connection_manager_attribute_sel)*