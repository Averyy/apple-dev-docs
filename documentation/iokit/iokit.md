# IOKit

**Framework**: IOKit  
**Role**: Framework

Access hardware devices and drivers from your apps and services.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 1.0+

## Overview

The IOKit framework implements nonkernel access to IOKit objects such drivers and nubs through the device-interface mechanism.

> ❗ **Important**: Devices supported on macOS 11 and later require [DriverKit](../DriverKit/DriverKit.md). Use IOKit in your apps and services to discover and use devices. 

## Topics

### Serial Ports
- [Communicating with a Modem on a Serial Port](./communicating_with_a_modem_on_a_serial_port.md)
  Find and connect to a modem attached to a serial port using IOKit.
### Reference
- [IODataQueueClient.h](./iodataqueueclient_h.md)
- [IOKitLib.h](./iokitlib_h.md)
- [IOTypes.h User-Space](./iotypes_h_user-space.md)
- [IOKit Structures](./iokit_structures.md)
- [IOKit Enumerations](./iokit_enumerations.md)
- [IOKit Constants](./iokit_constants.md)
- [IOKit Functions](./iokit_functions.md)
- [IOKit Data Types](./iokit_data_types.md)
- [ATASMARTLib.h](./atasmartlib_h.md)
  ATASMARTLib implements non-kernel task access to ATA SMART data.
- [IOAudioDefines.h User-Space](./ioaudiodefines_h_user-space.md)
- [IOAudioLib.h](./ioaudiolib_h.md)
  C interface to IOAudio functions
- [IOAudioTypes.h User-Space](./ioaudiotypes_h_user-space.md)
- [IOBDBlockStorageDevice.h User-Space](./iobdblockstoragedevice_h_user-space.md)
  This header contains the IOBDBlockStorageDevice class definition.
- [IOBDMedia.h User-Space](./iobdmedia_h_user-space.md)
  This header contains the IOBDMedia class definition.
- [IOBlockStorageDevice.h User-Space](./ioblockstoragedevice_h_user-space.md)
  This header contains the IOBlockStorageDevice class definition.
- [IOBlockStorageDriver.h User-Space](./ioblockstoragedriver_h_user-space.md)
  This header contains the IOBlockStorageDriver class definition.
- [IOCDBlockStorageDevice.h User-Space](./iocdblockstoragedevice_h_user-space.md)
  This header contains the IOCDBlockStorageDevice class definition.
- [IOCDMedia.h User-Space](./iocdmedia_h_user-space.md)
  This header contains the IOCDMedia class definition.
- [IODVDBlockStorageDevice.h User-Space](./iodvdblockstoragedevice_h_user-space.md)
  This header contains the IODVDBlockStorageDevice class definition.
- [IODVDMedia.h User-Space](./iodvdmedia_h_user-space.md)
  This header contains the IODVDMedia class definition.
- [IODataQueueShared.h User-Space](./iodataqueueshared_h_user-space.md)
- [IOEthernetController.h User-Space](./ioethernetcontroller_h_user-space.md)
- [IOEthernetInterface.h User-Space](./ioethernetinterface_h_user-space.md)
- [IOEthernetStats.h User-Space](./ioethernetstats_h_user-space.md)
  Ethernet statistics.
- [IOFilterScheme.h User-Space](./iofilterscheme_h_user-space.md)
  This header contains the IOFilterScheme class definition.
- [IOFireWireAVCLib.h](./iofirewireavclib_h.md)
- [IOFireWireFamilyCommon.h User-Space](./iofirewirefamilycommon_h_user-space.md)
  This file contains useful definitions for working with FireWire in the kernel and in user space
- [IOFireWireLib.h](./iofirewirelib_h.md)
- [IOFireWireSBP2Lib.h](./iofirewiresbp2lib_h.md)
- [IOFireWireStorageCharacteristics.h User-Space](./iofirewirestoragecharacteristics_h_user-space.md)
- [IOFramebufferShared.h User-Space](./ioframebuffershared_h_user-space.md)
- [IOGraphicsLib.h](./iographicslib_h.md)
- [IOGraphicsTypes.h User-Space](./iographicstypes_h_user-space.md)
- [IOHIDBase.h](./iohidbase_h.md)
- [IOHIDDevice.h User-Space](./iohiddevice_h_user-space.md)
- [IOHIDDevicePlugIn.h](./iohiddeviceplugin_h.md)
- [IOHIDElement.h](./iohidelement_h.md)
- [IOHIDKeys.h User-Space](./iohidkeys_h_user-space.md)
- [IOHIDLibObsolete.h](./iohidlibobsolete_h.md)
- [IOHIDManager.h](./iohidmanager_h.md)
- [IOHIDQueue.h](./iohidqueue_h.md)
- [IOHIDTransaction.h](./iohidtransaction_h.md)
- [IOHIDValue.h](./iohidvalue_h.md)
- [IOI2CInterface.h User-Space](./ioi2cinterface_h_user-space.md)
- [IOKitServer.h User-Space](./iokitserver_h_user-space.md)
- [IOMedia.h User-Space](./iomedia_h_user-space.md)
  This header contains the IOMedia class definition.
- [IOMessage.h User-Space](./iomessage_h_user-space.md)
  Defines message type constants for several IOKit messaging API's.
- [IONetworkController.h User-Space](./ionetworkcontroller_h_user-space.md)
- [IONetworkData.h User-Space](./ionetworkdata_h_user-space.md)
- [IONetworkInterface.h User-Space](./ionetworkinterface_h_user-space.md)
- [IONetworkLib.h](./ionetworklib_h.md)
- [IONetworkMedium.h User-Space](./ionetworkmedium_h_user-space.md)
- [IONetworkStats.h User-Space](./ionetworkstats_h_user-space.md)
  Generic network statistics.
- [IOPM.h User-Space](./iopm_h_user-space.md)
  Defines power management constants and keys used by both in-kernel and user space power management.
- [IOPMKeys.h](./iopmkeys_h.md)
  IOPMKeys.h defines C strings for use accessing power management data. Note that all of these C strings must be converted to CFStrings before use. You can wrap them with the CFSTR() macro, or create a CFStringRef (that you must later CFRelease()) using CFStringCreateWithCString()
- [IOPMLib.h](./iopmlib_h.md)
  IOPMLib provides access to common power management facilities, like initiating system sleep, getting current idle timer values, registering for sleep/wake notifications, and preventing system sleep.
- [IOPSKeys.h](./iopskeys_h.md)
  IOPSKeys.h defines C strings for use accessing power source data in IOPowerSource CFDictionaries, as returned by [`IOPSGetPowerSourceDescription`](./api-1523867-iopsgetpowersourcedescription.md) Note that all of these C strings must be converted to CFStrings before use. You can wrap them with the CFSTR() macro, or create a CFStringRef (that you must later CFRelease()) using CFStringCreateWithCString().
- [IOPartitionScheme.h User-Space](./iopartitionscheme_h_user-space.md)
  This header contains the IOPartitionScheme class definition.
- [IOPowerSources.h](./iopowersources_h.md)
- [IOStorage.h User-Space](./iostorage_h_user-space.md)
  This header contains the IOStorage class definition.
- [IOStorageCardCharacteristics.h User-Space](./iostoragecardcharacteristics_h_user-space.md)
- [IOStorageDeviceCharacteristics.h User-Space](./iostoragedevicecharacteristics_h_user-space.md)
- [IOStorageProtocolCharacteristics.h User-Space](./iostorageprotocolcharacteristics_h_user-space.md)
- [IOStreamLib.h](./iostreamlib_h.md)
  IOCFPlugin library for using IOStream objects.
- [IOStreamShared.h User-Space](./iostreamshared_h_user-space.md)
  IOStream definitions shared between kernel and user space.
- [IOUPSPlugIn.h](./ioupsplugin_h.md)
- [IOUSBLib.h](./iousblib_h.md)
- [IOVideoDeviceLib.h User-Space](./iovideodevicelib_h_user-space.md)
- [IOVideoDeviceShared.h User-Space](./iovideodeviceshared_h_user-space.md)
  IOVideoDevice definitions shared between kernel and user space.
- [IOVideoDeviceUserClient.h User-Space](./iovideodeviceuserclient_h_user-space.md)
- [IOVideoTypes.h User-Space](./iovideotypes_h_user-space.md)
- [KextManager.h](./kextmanager_h.md)
  The KextManager API provides a simple interface for applications to load kernel extensions (kexts) via RPC to kextd, and to look up the URLs for kexts by bundle identifier.
- [SCSICmds_INQUIRY_Definitions.h User-Space](./scsicmds_inquiry_definitions_h_user-space.md)
  This file contains all definitions for the data returned from the INQUIRY (0x12) command.
- [SCSICmds_MODE_Definitions.h User-Space](./scsicmds_mode_definitions_h_user-space.md)
  This file contains all definitions for the data returned from the MODE_SENSE_6 and MODE_SENSE_10 commands.
- [SCSICmds_READ_CAPACITY_Definitions.h User-Space](./scsicmds_read_capacity_definitions_h_user-space.md)
  This file contains all definitions for the data returned from the READ CAPACITY 10 (0x25) and READ CAPACITY 16 (0x9E) commands.
- [SCSICmds_REPORT_LUNS_Definitions.h User-Space](./scsicmds_report_luns_definitions_h_user-space.md)
  This file contains all definitions for the data returned from the REPORT_LUNS (0xA0) command.
- [SCSICmds_REQUEST_SENSE_Defs.h User-Space](./scsicmds_request_sense_defs_h_user-space.md)
  This file contains all definitions for the data returned from the REQUEST SENSE (0x03) command and from auto sense on protocols that support it.
- [SCSICommandDefinitions.h User-Space](./scsicommanddefinitions_h_user-space.md)
- [SCSITask.h User-Space](./scsitask_h_user-space.md)
- [SCSITaskLib.h](./scsitasklib_h.md)
  SCSITaskLib implements non-kernel task access to specific IOKit object types, namely any SCSI Peripheral Device for which there isn't an in-kernel driver and for authoring devices such as CD-R/W and DVD-R/W drives.
- [USB.h User-Space](./usb_h_user-space.md)
- [USBSpec.h User-Space](./usbspec_h_user-space.md)
### COM Interfaces
- [IOATASMARTInterface](./ioatasmartinterface.md)
  Self-Monitoring, Analysis, and Reporting Technology Interface.
- [IOFireWireAsyncStreamCommandInterface](./iofirewireasyncstreamcommandinterface.md)
- [IOFireWireAVCLibConsumerInterface](./iofirewireavclibconsumerinterface.md)
  Interface for an asynchronous connection consumer.
- [IOFireWireAVCLibProtocolInterface](./iofirewireavclibprotocolinterface.md)
  Initial interface discovered for all AVC protocol drivers.
- [IOFireWireAVCLibUnitInterface](./iofirewireavclibunitinterface.md)
  Initial interface discovered for all AVC Unit drivers.
- [IOFireWireCommandInterface](./iofirewirecommandinterface.md)
  IOFireWireLib command object.
- [IOFireWireCompareSwapCommandInterface](./iofirewirecompareswapcommandinterface.md)
- [IOFireWireCompareSwapCommandInterface_v3](./iofirewirecompareswapcommandinterface_v3.md)
- [IOFireWireConfigDirectoryInterface](./iofirewireconfigdirectoryinterface.md)
  IOFireWireLib device config ROM browsing interface
- [IOFireWireDCLCommandPoolInterface](./iofirewiredclcommandpoolinterface.md)
- [IOFireWireDeviceInterface](./iofirewiredeviceinterface.md)
  IOFireWireDeviceInterface is your primary gateway to the functionality contained in IOFireWireLib.
- [IOFireWireIsochChannelInterface](./iofirewireisochchannelinterface.md)
  FireWire user client isochronous channel object.
- [IOFireWireIsochPortInterface](./iofirewireisochportinterface.md)
  FireWire user client isochronous port interface
- [IOFireWireLibIRMAllocationInterface](./iofirewirelibirmallocationinterface.md)
- [IOFireWireLibPHYPacketListenerInterface](./iofirewirelibphypacketlistenerinterface.md)
  Represents and provides management functions for a phy packet listener object.
- [IOFireWireLibVectorCommandInterface](./iofirewirelibvectorcommandinterface.md)
  IOFireWireLib command object for grouping commands execution.
- [IOFireWireLocalIsochPortInterface](./iofirewirelocalisochportinterface.md)
  FireWire user client local isochronous port object.
- [IOFireWireLocalUnitDirectoryInterface](./iofirewirelocalunitdirectoryinterface.md)
- [IOFireWireNubInterface](./iofirewirenubinterface-ajp.md)
  IOFireWireDeviceInterface is your primary gateway to the functionality contained in IOFireWireLib.
- [IOFireWireNuDCLPoolInterface](./iofirewirenudclpoolinterface.md)
  Use this interface to build NuDCL-based DCL programs.
- [IOFireWirePHYCommandInterface](./iofirewirephycommandinterface.md)
- [IOFireWirePhysicalAddressSpaceInterface](./iofirewirephysicaladdressspaceinterface.md)
  IOFireWireLib physical address space object. ( interface name: IOFireWirePhysicalAddressSpaceInterface )
- [IOFireWirePseudoAddressSpaceInterface](./iofirewirepseudoaddressspaceinterface.md)
- [IOFireWireReadCommandInterface](./iofirewirereadcommandinterface.md)
  IOFireWireLib block read command object.
- [IOFireWireReadQuadletCommandInterface](./iofirewirereadquadletcommandinterface.md)
  IOFireWireReadQuadletCommandInterface -- IOFireWireLib quadlet read command object.
- [IOFireWireRemoteIsochPortInterface](./iofirewireremoteisochportinterface.md)
- [IOFireWireSBP2LibLoginInterface](./iofirewiresbp2liblogininterface.md)
  Supplies the login maintenance and Normal Command ORB execution portions of the API.
- [IOFireWireSBP2LibLUNInterface](./iofirewiresbp2libluninterface.md)
  Initial interface disovered for all drivers.
- [IOFireWireSBP2LibMgmtORBInterface](./iofirewiresbp2libmgmtorbinterface.md)
  Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LibLUNInterface.
- [IOFireWireSBP2LibORBInterface](./iofirewiresbp2liborbinterface.md)
  Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2LibLoginInterface.
- [IOFireWireUnitInterface](./iofirewireunitinterface-apt.md)
  IOFireWireDeviceInterface is your primary gateway to the functionality contained in IOFireWireLib.
- [IOFireWireWriteCommandInterface](./iofirewirewritecommandinterface.md)
  IOFireWireLib block read command object.
- [IOFireWireWriteQuadletCommandInterface](./iofirewirewritequadletcommandinterface.md)
  IOFireWireLib quadlet read command object.
- [IOFWAsyncStreamListenerInterface](./iofwasyncstreamlistenerinterface.md)
  Represents and provides management functions for a asyn stream listener object.
- [IOHIDDeviceDeviceInterface](./iohiddevicedeviceinterface.md)
  The object you use to access HID devices from user space, returned by version 1.5 of the IOHIDFamily.
- [IOHIDDeviceInterface](./iohiddeviceinterface.md)
  CFPlugin object subclass which provides the primary interface to HID devices.
- [IOHIDDeviceInterface121](./iohiddeviceinterface121.md)
  CFPlugin object subclass which provides the primary interface to HID devices. This class is a subclass of IOHIDDeviceInterface.
- [IOHIDDeviceInterface122](./iohiddeviceinterface122.md)
  CFPlugin object subclass which provides the primary interface to HID devices. This class is a subclass of IOHIDDeviceInterface121.
- [IOHIDDeviceQueueInterface](./iohiddevicequeueinterface.md)
  The object you use to access a HID queue from user space, returned by version 1.5 of the IOHIDFamily.
- [IOHIDDeviceTransactionInterface](./iohiddevicetransactioninterface.md)
  The object you use to access a HID transaction from user space, returned by version 1.5 of the IOHIDFamily.
- [IOHIDOutputTransactionInterface](./iohidoutputtransactioninterface.md)
  CFPlugin object subclass which privides interface for output transactions to HID devices. Created by a IOHIDDeviceInterface object.
- [IOHIDQueueInterface](./iohidqueueinterface.md)
  CFPlugin object subclass which provides an interface for input queues from HID devices. Created by an IOHIDDeviceInterface object.
- [IOUPSPlugInInterface](./ioupsplugininterface.md)
  Represents and provides management functions for a UPS device.
- [IOUSBDeviceInterface](./iousbdeviceinterface.md)
  The object you use to access USB devices from user space, returned by all versions of the IOUSBFamily currently shipping.
- [IOUSBDeviceInterface182](./iousbdeviceinterface182.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 1.8.2 and above.
- [IOUSBDeviceInterface187](./iousbdeviceinterface187.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 10.8.7 and above.
- [IOUSBDeviceInterface197](./iousbdeviceinterface197.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 1.9.7 and above.
- [IOUSBDeviceInterface245](./iousbdeviceinterface245.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 2.4.5 and above.
- [IOUSBDeviceInterface300](./iousbdeviceinterface300.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.0.0 and above.
- [IOUSBDeviceInterface320](./iousbdeviceinterface320.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.
- [IOUSBDeviceInterface500](./iousbdeviceinterface500.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.
- [IOUSBInterfaceInterface](./iousbinterfaceinterface.md)
  The object you use to access a USB device interface from user space, returned by all versions of the IOUSBFamily currently shipping.
- [IOUSBInterfaceInterface182](./iousbinterfaceinterface182.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.2 and above.
- [IOUSBInterfaceInterface183](./iousbinterfaceinterface183.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.3 and above.
- [IOUSBInterfaceInterface190](./iousbinterfaceinterface190.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9 and above.
- [IOUSBInterfaceInterface192](./iousbinterfaceinterface192.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.2 and above.
- [IOUSBInterfaceInterface197](./iousbinterfaceinterface197.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.7 and above.
- [MMCDeviceInterface](./mmcdeviceinterface.md)
  Basic interface for an MMC-2 Compliant Device.
- [SCSITaskDeviceInterface](./scsitaskdeviceinterface.md)
  Basic interface for a SCSITask Device.
- [SCSITaskInterface](./scsitaskinterface.md)
  Basic interface for a SCSITask.
### Classes
- [IOVideoControlDictionary](./iovideocontroldictionary.md)
- [IOVideoStreamDictionary](./iovideostreamdictionary.md)
- [IOVideoStreamFormatDictionary](./iovideostreamformatdictionary.md)

## See Also

### Related Documentation
- [IOKit Fundamentals](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP0000011)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit)*