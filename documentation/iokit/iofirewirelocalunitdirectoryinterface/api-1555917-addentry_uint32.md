# AddEntry_UInt32

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Append an immediate leaf

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*AddEntry_UInt32)(IOFireWireLibLocalUnitDirectoryRef self, int key, UInt32 value, CFStringRef inDesc);
```

## Discussion

Appends an immediate leaf to a unit directory. Note that only the lower 3 bytes of the passed in value can appear in the unit directory.

## Parameters

- `self`: The local unit directory interface to use.
- `key`: The config ROM key for the data to be added.
- `value`: The value to be added.
- `inDesc`: Reserved; set to NULL.

## See Also

### Miscellaneous
- [AddEntry_FWAddress](./api-1555793-addentry_fwaddress.md)
  Append an offset leaf
- [AddEntry_Ptr](./api-1555944-addentry_ptr.md)
  Append a data leaf
- [Publish](./api-1555590-publish.md)
  Causes a constructed or updated unit directory to appear in the local machine's config ROM. Note that this call will cause a bus reset, after which the unit directory will be visible to devices on the bus.
- [Unpublish](./api-1555668-unpublish.md)
  Has the opposite effect from Publish(). This call removes a unit directory from the local machine's config ROM. Note that this call will cause a bus reset, after which the unit directory will no longer appear to devices on the bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalunitdirectoryinterface/1555917-addentry_uint32)*