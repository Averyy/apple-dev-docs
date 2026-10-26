# PowerPC Toolbox Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for the PowerPC Toolbox.

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
- [gestaltPPCToolboxAttr](./api-1471990-powerpc_toolbox_attribute_select/gestaltppctoolboxattr.md)
  The selector you pass to the Gestalt function to determine the Program-to-Program Communication (PPC) Toolbox attributes. Note that these constants are defined as masks, not bit numbers.
- [gestaltPPCToolboxPresent](./api-1471990-powerpc_toolbox_attribute_select/gestaltppctoolboxpresent.md)
- [gestaltPPCSupportsRealTime](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsrealtime.md)
- [gestaltPPCSupportsIncoming](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsincoming.md)
- [gestaltPPCSupportsOutGoing](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsoutgoing.md)
- [gestaltPPCSupportsTCP_IP](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportstcp_ip.md)
- [gestaltPPCSupportsIncomingAppleTalk](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsincomingappletalk.md)
- [gestaltPPCSupportsIncomingTCP_IP](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsincomingtcp_ip.md)
- [gestaltPPCSupportsOutgoingAppleTalk](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsoutgoingappletalk.md)
- [gestaltPPCSupportsOutgoingTCP_IP](./api-1471990-powerpc_toolbox_attribute_select/gestaltppcsupportsoutgoingtcp_ip.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471990-powerpc_toolbox_attribute_select)*