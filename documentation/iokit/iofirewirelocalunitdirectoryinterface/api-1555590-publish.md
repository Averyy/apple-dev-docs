# Publish

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Causes a constructed or updated unit directory to appear in the local machine's config ROM. Note that this call will cause a bus reset, after which the unit directory will be visible to devices on the bus.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*Publish)(IOFireWireLibLocalUnitDirectoryRef self);
```

## Parameters

- `self`: The local unit directory interface to use.

## See Also

### Miscellaneous
- [AddEntry_FWAddress](./api-1555793-addentry_fwaddress.md)
  Append an offset leaf
- [AddEntry_Ptr](./api-1555944-addentry_ptr.md)
  Append a data leaf
- [AddEntry_UInt32](./api-1555917-addentry_uint32.md)
  Append an immediate leaf
- [Unpublish](./api-1555668-unpublish.md)
  Has the opposite effect from Publish(). This call removes a unit directory from the local machine's config ROM. Note that this call will cause a bus reset, after which the unit directory will no longer appear to devices on the bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalunitdirectoryinterface/1555590-publish)*