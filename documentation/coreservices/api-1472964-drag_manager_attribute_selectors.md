# Drag Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Drag Manager.

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
- [gestaltDragMgrAttr](./api-1472964-drag_manager_attribute_selectors/gestaltdragmgrattr.md)
  The Gestalt selector passed to determine what features of the Drag Manager are present. Passing the `gestaltDragMgrAttr` constant produces a 32-bit value whose bits you should test to determine what Drag Manager functionality is available.
- [gestaltDragMgrPresent](./api-1472964-drag_manager_attribute_selectors/gestaltdragmgrpresent.md)
  If the bit specified by this mask is set, the Drag Manager functions are available.
- [gestaltDragMgrFloatingWind](./api-1472964-drag_manager_attribute_selectors/gestaltdragmgrfloatingwind.md)
  If the bit specified by this mask is set, the Drag Manager floating window support functions are available.
- [gestaltPPCDragLibPresent](./api-1472964-drag_manager_attribute_selectors/gestaltppcdraglibpresent.md)
  If the bit specified by this mask is set, the Drag Manager PPC Drag Library functions are available.
- [gestaltDragMgrHasImageSupport](./api-1472964-drag_manager_attribute_selectors/gestaltdragmgrhasimagesupport.md)
  If the bit specified by this mask is set, the Drag Manager image support functions are available.
- [gestaltCanStartDragInFloatWindow](./api-1472964-drag_manager_attribute_selectors/gestaltcanstartdraginfloatwindow.md)
  If the bit specified by this mask is set, the Drag Manager can start a drag in a floating window.
- [gestaltSetDragImageUpdates](./api-1472964-drag_manager_attribute_selectors/gestaltsetdragimageupdates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472964-drag_manager_attribute_selectors)*