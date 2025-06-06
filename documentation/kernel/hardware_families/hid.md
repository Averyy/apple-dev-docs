# HID

**Framework**: Kernel

Implement a driver that interacts with human interface devices, such as mice and keyboards.

#### Overview

The use of kernel extensions for HID drivers is deprecated. Instead, create a DriverKit extension using [`HIDDriverKit`](https://developer.apple.com/documentation/hiddriverkit).

## Topics

### Reports
- [IOHIDReportType](iohidreporttype.md)
  Describes different type of HID reports.
- [HIDReportCommandType](hidreportcommandtype.md)
- [IOHIDCompletion](iohidcompletion.md)
  Struct specifying action to perform when set/get report completes.
- [IOHIDCompletionAction](iohidcompletionaction.md)
  Function called when set/get report completes
### Event Types
- [IOHIDBiometricEventType](iohidbiometriceventtype.md)
- [IOHIDPointerEventOptions](iohidpointereventoptions.md)
- [IOHIDOptionsType](iohidoptionstype.md)
  Options for opening a device via IOHIDLib.
- [IOHIDStandardType](iohidstandardtype.md)
  Type to define what industrial standard the device is referencing.
- [IOHIDValueScaleType](iohidvaluescaletype.md)
  Describes different types of scaling that can be performed on element values.
- [IOHIDKeyboardEventOptions](iohidkeyboardeventoptions.md)
- [IOHIDScrollEventOptions](iohidscrolleventoptions.md)
- [IOHIDEventType](iohideventtype.md)
### HID Elements
- [IOHIDElementCollectionType](iohidelementcollectiontype.md)
  Describes different types of HID collections.
- [IOHIDElementCommitDirection](iohidelementcommitdirection.md)
- [IOHIDElementCookie](iohidelementcookie.md)
  Abstract data type used as a unique identifier for an element.
- [IOHIDElementFlags](iohidelementflags.md)
- [IOHIDElementType](iohidelementtype.md)
  Describes different types of HID elements.
- [IOHIDValueOptions](iohidvalueoptions.md)
  Describes options for gathering element values.
### HID Types
- [IOHIDButtonModes](iohidbuttonmodes.md)
- [IOHIDDigitizerStylusData](iohiddigitizerstylusdata.md)
- [IOHIDDigitizerTouchData](iohiddigitizertouchdata.md)
- [IOHIDQueueOptionsType](iohidqueueoptionstype.md)
  Options for creating a queue via IOHIDLib.
- [NXByteOrder](nxbyteorder.md)
- [NXEQElement](nxeqelement.md)
- [NXEvent](nxevent.md)
- [NXEventData](nxeventdata.md)
- [NXEventExt](nxeventext.md)
- [NXEventExtension](nxeventextension.md)
- [NXEventPtr](nxeventptr.md)
- [NXEventSystemDevice](nxeventsystemdevice.md)
- [NXEventSystemDeviceList](nxeventsystemdevicelist.md)
- [NXEventSystemInfoData](nxeventsysteminfodata.md)
- [NXEventSystemInfoType](nxeventsysteminfotype.md)
- [NXKeyMapping](nxkeymapping.md)
- [NXMouseButton](nxmousebutton.md)
- [NXMouseScaling](nxmousescaling.md)
- [NXParsedKeyMapping](nxparsedkeymapping.md)
- [NXSwappedDouble](nxswappeddouble.md)
- [NXSwappedFloat](nxswappedfloat.md)
- [NXTabletPointData](nxtabletpointdata.md)
- [NXTabletPointDataPtr](nxtabletpointdataptr.md)
- [NXTabletProximityData](nxtabletproximitydata.md)
- [NXTabletProximityDataPtr](nxtabletproximitydataptr.md)

## See Also

- [Audio](hardware_families/audio.md)
  Implement a driver that interacts with audio hardware. 
- [Graphics and Displays](hardware_families/graphics_and_displays.md)
  Implement a driver that interacts with graphics and video hardware. 
- [Network](hardware_families/network.md)
  Implement a driver that interacts with network interfaces such as Ethernet adaptors. 
- [SCSI](hardware_families/scsi.md)
  Implement a driver that supports Small Computer System Interface (SCSI) protocols.
- [Mass Storage](hardware_families/mass_storage.md)
  Implement a driver that communicates with CD, DVD, or other mass storage devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/hid)*