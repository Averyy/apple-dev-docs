# AddEntry_FWAddress

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Append an offset leaf

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*AddEntry_FWAddress)(IOFireWireLibLocalUnitDirectoryRef self, int key, const FWAddress *value, CFStringRef inDesc);
```

## Discussion

Appends an offset leaf to a unit directory. The address passed in value should be an address in initial unit space of the local config ROM.

## Parameters

- `self`: The local unit directory interface to use.
- `key`: The config ROM key for the data to be added.
- `value`: A pointer to a FireWire address.
- `inDesc`: Reserved; set to NULL.

## See Also

### Miscellaneous
- [AddEntry_Ptr](./api-1555944-addentry_ptr.md)
  Append a data leaf
- [AddEntry_UInt32](./api-1555917-addentry_uint32.md)
  Append an immediate leaf
- [Publish](./api-1555590-publish.md)
  Causes a constructed or updated unit directory to appear in the local machine's config ROM. Note that this call will cause a bus reset, after which the unit directory will be visible to devices on the bus.
- [Unpublish](./api-1555668-unpublish.md)
  Has the opposite effect from Publish(). This call removes a unit directory from the local machine's config ROM. Note that this call will cause a bus reset, after which the unit directory will no longer appear to devices on the bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalunitdirectoryinterface/1555793-addentry_fwaddress)*