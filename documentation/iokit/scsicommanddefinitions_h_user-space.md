# SCSICommandDefinitions.h User-Space

**Framework**: IOKit  
**Role**: API Collection

## Overview

This file contains all the definitions for types and constants that are used by the command set classes for building CDBs. The field type definitions are used for the parameters passed to a method that builds and sends any SCSI defined command to clearly identify the type of value expected for a parameter.

The command methods will then use the appropriate mask to verify that the value passed into a parameter is of the specified type.

Currently only types and masks are defined for 8 bytes and smaller fields. If a command is defined that uses a larger field, these should be expanded to include those sizes.

### Included Headers

- <IOKit/IOTypes.h>
- <CoreFoundation/CoreFoundation.h>

## Topics

### Data Types
- [SCSICmdField10Bit](./scsicmdfield10bit.md)
- [SCSICmdField11Bit](./scsicmdfield11bit.md)
- [SCSICmdField12Bit](./scsicmdfield12bit.md)
- [SCSICmdField13Bit](./scsicmdfield13bit.md)
- [SCSICmdField14Bit](./scsicmdfield14bit.md)
- [SCSICmdField15Bit](./scsicmdfield15bit.md)
- [SCSICmdField17Bit](./scsicmdfield17bit.md)
- [SCSICmdField18Bit](./scsicmdfield18bit.md)
- [SCSICmdField19Bit](./scsicmdfield19bit.md)
- [SCSICmdField1Bit](./scsicmdfield1bit.md)
- [SCSICmdField1Byte](./scsicmdfield1byte.md)
- [SCSICmdField20Bit](./scsicmdfield20bit.md)
- [SCSICmdField21Bit](./scsicmdfield21bit.md)
- [SCSICmdField22Bit](./scsicmdfield22bit.md)
- [SCSICmdField23Bit](./scsicmdfield23bit.md)
- [SCSICmdField25Bit](./scsicmdfield25bit.md)
- [SCSICmdField26Bit](./scsicmdfield26bit.md)
- [SCSICmdField27Bit](./scsicmdfield27bit.md)
- [SCSICmdField28Bit](./scsicmdfield28bit.md)
- [SCSICmdField29Bit](./scsicmdfield29bit.md)
- [SCSICmdField2Bit](./scsicmdfield2bit.md)
- [SCSICmdField2Byte](./scsicmdfield2byte.md)
- [SCSICmdField30Bit](./scsicmdfield30bit.md)
- [SCSICmdField31Bit](./scsicmdfield31bit.md)
- [SCSICmdField33Bit](./scsicmdfield33bit.md)
- [SCSICmdField34Bit](./scsicmdfield34bit.md)
- [SCSICmdField35Bit](./scsicmdfield35bit.md)
- [SCSICmdField36Bit](./scsicmdfield36bit.md)
- [SCSICmdField37Bit](./scsicmdfield37bit.md)
- [SCSICmdField38Bit](./scsicmdfield38bit.md)
- [SCSICmdField39Bit](./scsicmdfield39bit.md)
- [SCSICmdField3Bit](./scsicmdfield3bit.md)
- [SCSICmdField3Byte](./scsicmdfield3byte.md)
- [SCSICmdField41Bit](./scsicmdfield41bit.md)
- [SCSICmdField42Bit](./scsicmdfield42bit.md)
- [SCSICmdField43Bit](./scsicmdfield43bit.md)
- [SCSICmdField44Bit](./scsicmdfield44bit.md)
- [SCSICmdField45Bit](./scsicmdfield45bit.md)
- [SCSICmdField46Bit](./scsicmdfield46bit.md)
- [SCSICmdField47Bit](./scsicmdfield47bit.md)
- [SCSICmdField49Bit](./scsicmdfield49bit.md)
- [SCSICmdField4Bit](./scsicmdfield4bit.md)
- [SCSICmdField4Byte](./scsicmdfield4byte.md)
- [SCSICmdField50Bit](./scsicmdfield50bit.md)
- [SCSICmdField51Bit](./scsicmdfield51bit.md)
- [SCSICmdField52Bit](./scsicmdfield52bit.md)
- [SCSICmdField53Bit](./scsicmdfield53bit.md)
- [SCSICmdField54Bit](./scsicmdfield54bit.md)
- [SCSICmdField55Bit](./scsicmdfield55bit.md)
- [SCSICmdField57Bit](./scsicmdfield57bit.md)
- [SCSICmdField58Bit](./scsicmdfield58bit.md)
- [SCSICmdField59Bit](./scsicmdfield59bit.md)
- [SCSICmdField5Bit](./scsicmdfield5bit.md)
- [SCSICmdField5Byte](./scsicmdfield5byte.md)
- [SCSICmdField60Bit](./scsicmdfield60bit.md)
- [SCSICmdField61Bit](./scsicmdfield61bit.md)
- [SCSICmdField62Bit](./scsicmdfield62bit.md)
- [SCSICmdField63Bit](./scsicmdfield63bit.md)
- [SCSICmdField6Bit](./scsicmdfield6bit.md)
- [SCSICmdField6Byte](./scsicmdfield6byte.md)
- [SCSICmdField7Bit](./scsicmdfield7bit.md)
- [SCSICmdField7Byte](./scsicmdfield7byte.md)
- [SCSICmdField8Byte](./scsicmdfield8byte.md)
- [SCSICmdField9Bit](./scsicmdfield9bit.md)
### Constants
- [Defines](./scsicommanddefinitions_h_user-space/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicommanddefinitions_h_user-space)*