# CMProfileIterateData

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains a callback routine with a description of a profile that is during an iteration through the available profiles.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMProfileIterateData {
    ...
} CMProfileIterateData;
```

#### Overview

The ColorSync Manager defines the `CMProfileIterateData` structure to provide your [`CMProfileIterateProcPtr`](./cmprofileiterateprocptr.md) callback routine with a description of a profile during an iteration through the available profiles that takes place when you call [CMIterateColorSyncFolder](./colorsync_manager/api-1804904-cmiteratecolorsyncfolder.md).

## Topics

### Fields
- [TPLDEV_TYPE_WPS_SPEED](./cmprofileiteratedata/api-1806175-tpldev_type_wps_speed.md)
- [deviceData](./cmprofileiteratedata/api-1806179-devicedata.md)
### Instance Properties
- [asciiName](./cmprofileiteratedata/api-1560309-asciiname.md)
- [code](./cmprofileiteratedata/api-1560666-code.md)
  A script code identifying the script system used for the profile description. The `ScriptCode` data type is defined in the MacTypes.h header file.
- [dataVersion](./cmprofileiteratedata/api-1560194-dataversion.md)
  A value identifying the version of the structure. Currently set to `cmProfileIterateDataVersion1`.
- [digest](./cmprofileiteratedata/api-1560403-digest.md)
- [header](./cmprofileiteratedata/api-1560694-header.md)
  A ColorSync version 2.x profile header structure of type [`CM2Header`](./cm2header.md), containing information such as the profile size, type, version, and so on. 
- [location](./cmprofileiteratedata/api-1560465-location.md)
  A structure specifying the profile location. With ColorSync 2.5, the location is always file-based, but that may not be true for future versions. Your code should always verify that the location structure contains a file specification before attempting to use it. 
- [makeAndModel](./cmprofileiteratedata/api-1560138-makeandmodel.md)
- [name](./cmprofileiteratedata/api-1560168-name.md)
  The profile name, stored as a Pascal-type string (with length byte first) of up to 255 characters.
- [uniCodeName](./cmprofileiteratedata/api-1560310-unicodename.md)
- [uniCodeNameCount](./cmprofileiteratedata/api-1560523-unicodenamecount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedata)*