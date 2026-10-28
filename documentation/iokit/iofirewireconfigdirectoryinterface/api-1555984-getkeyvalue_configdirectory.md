# GetKeyValue_ConfigDirectory

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*GetKeyValue_ConfigDirectory)(IOFireWireLibConfigDirectoryRef self, int inKey, IOFireWireLibConfigDirectoryRef *outValue, REFIID iid, CFStringRef *outText);
```

## Discussion

Description forthcoming

## See Also

### Miscellaneous
- [GetIndexEntry](./api-1556035-getindexentry.md)
- [GetIndexKey](./api-1555943-getindexkey.md)
- [GetIndexOffset_FWAddress](./api-1555606-getindexoffset_fwaddress.md)
- [GetIndexOffset_UInt32](./api-1556063-getindexoffset_uint32.md)
- [GetIndexType](./api-1555964-getindextype.md)
- [GetIndexValue_ConfigDirectory](./api-1556050-getindexvalue_configdirectory.md)
- [GetIndexValue_Data](./api-1555603-getindexvalue_data.md)
- [GetIndexValue_String](./api-1555859-getindexvalue_string.md)
- [GetIndexValue_UInt32](./api-1555598-getindexvalue_uint32.md)
- [GetKeyOffset_FWAddress](./api-1555952-getkeyoffset_fwaddress.md)
- [GetKeySubdirectories](./api-1555612-getkeysubdirectories.md)
- [GetKeyType](./api-1556099-getkeytype.md)
- [GetKeyValue_Data](./api-1555838-getkeyvalue_data.md)
- [GetKeyValue_UInt32](./api-1555586-getkeyvalue_uint32.md)
- [GetNumEntries](./api-1555899-getnumentries.md)
- [GetSubdirectories](./api-1555633-getsubdirectories.md)
- [GetType](./api-1556044-gettype.md)
- [Update](./api-1555972-update.md)
  Causes the ROM data to be updated through the specified byte offset. This function should not be called in normal usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireconfigdirectoryinterface/1555984-getkeyvalue_configdirectory)*