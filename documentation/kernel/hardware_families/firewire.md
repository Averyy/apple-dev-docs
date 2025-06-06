# FireWire

**Framework**: Kernel

Implement a driver that supports FireWire devices. 

## Topics

### Interfaces
- [IOFireWireSerialBusProtocolTransport](iofirewireserialbusprotocoltransport.md)
  SCSI Protocol Driver Family for FireWire SBP2 Devices.
- [IOFireWireSBP2Target](iofirewiresbp2target.md)
  Serves as bridge between IOFireWireUnit and IOFireWireLUN.
- [IOFireWireController](iofirewirecontroller.md)
- [IOFireWireBus](iofirewirebus.md)
  IOFireWireBus is a public class the provides access to general FireWire functionality...
### Nubs
- [IOFireWireLocalNode](iofirewirelocalnode.md)
- [IOFireWireSBP2LUN](iofirewiresbp2lun.md)
  Provider for most drivers.
- [IOFireWireAVCSubUnit](iofirewireavcsubunit.md)
  nub for sub unit of AVC devices. Just for matching, calls the AVC unit for all functions.
- [IOFireWireAVCUnit](iofirewireavcunit.md)
  nub for AVC devices
- [IOFireWireAVCNub](iofirewireavcnub.md)
  nub for AVC devices
- [IOFireWireUnit](iofirewireunit.md)
- [IOFireWireNub](iofirewirenub.md)
### Devices
- [IOFireWireDevice](iofirewiredevice.md)
  Represents a FireWire device.
### Auxilliary Units
- [IOFireWireControllerAux](iofirewirecontrolleraux.md)
- [IOFireWireLocalNodeAux](iofirewirelocalnodeaux.md)
- [IOFireWireBusAux](iofirewirebusaux.md)
- [IOFireWireDeviceAux](iofirewiredeviceaux.md)
- [IOFireWireUnitAux](iofirewireunitaux.md)
- [IOFireWireNubAux](iofirewirenubaux.md)
### User-Space Access
- [IOFireWireSBP2UserClient](iofirewiresbp2userclient.md)
### AVC Support
- [IOFireWireAVCAsynchronousCommand](iofirewireavcasynchronouscommand.md)
- [IOFireWireAVCTargetSpace](iofirewireavctargetspace.md)
  object to centralize the AVC Target mode support
- [IOFireWireAVCCommand](iofirewireavccommand.md)
- [AVCCommandHandlerInfo](avccommandhandlerinfo.md)
- [AVCConnectionRecord](avcconnectionrecord.md)
- [AVCSubunitInfo](avcsubunitinfo.md)
- [AVCConnectTargetPlugsInParams](avcconnecttargetplugsinparams.md)
- [AVCConnectTargetPlugsOutParams](avcconnecttargetplugsoutparams.md)
- [AVCGetTargetPlugConnectionInParams](avcgettargetplugconnectioninparams.md)
- [AVCGetTargetPlugConnectionOutParams](avcgettargetplugconnectionoutparams.md)
- [AVCSubunitPlugRecord](avcsubunitplugrecord.md)
- [AVCUnitPlugRecord](avcunitplugrecord.md)
- [AVCUnitPlugs](avcunitplugs.md)
### DCL Support
- [IODCLProgram](iodclprogram.md)
- [IODCLTranslateListen](iodcltranslatelisten.md)
- [IODCLTranslateTalk](iodcltranslatetalk.md)
- [IODCLTranslator](iodcltranslator.md)
- [IOFWReceiveDCL](iofwreceivedcl.md)
- [IOFWSendDCL](iofwsenddcl.md)
- [IOFWSkipCycleDCL](iofwskipcycledcl.md)
- [IOFWDCL](iofwdcl.md)
- [DCLCallCommandProc](dclcallcommandproc.md)
- [DCLCallCommandProcPtr](dclcallcommandprocptr.md)
- [DCLCallProc](dclcallproc.md)
- [DCLCallProcDataType](dclcallprocdatatype.md)
- [DCLCallProcPtr](dclcallprocptr.md)
- [DCLCommand](dclcommand.md)
- [DCLCommandPtr](dclcommandptr.md)
- [DCLCompilerDataType](dclcompilerdatatype.md)
- [DCLJump](dcljump.md)
- [DCLJumpPtr](dcljumpptr.md)
- [DCLLabel](dcllabel.md)
- [DCLLabelPtr](dcllabelptr.md)
- [DCLNuDCLLeader](dclnudclleader.md)
- [DCLPtrTimeStamp](dclptrtimestamp.md)
- [DCLPtrTimeStampPtr](dclptrtimestampptr.md)
- [DCLSetTagSyncBits](dclsettagsyncbits.md)
- [DCLSetTagSyncBitsPtr](dclsettagsyncbitsptr.md)
- [DCLTimeStamp](dcltimestamp.md)
- [DCLTimeStampPtr](dcltimestampptr.md)
- [DCLTransferBuffer](dcltransferbuffer.md)
- [DCLTransferBufferPtr](dcltransferbufferptr.md)
- [DCLTransferPacket](dcltransferpacket.md)
- [DCLTransferPacketPtr](dcltransferpacketptr.md)
- [DCLUpdateDCLList](dclupdatedcllist.md)
- [DCLUpdateDCLListPtr](dclupdatedcllistptr.md)
### Serial Bus Protocol 2
- [IOFireWireSBP2Login](iofirewiresbp2login.md)
  Supplies the login maintenance and Normal Command ORB execution portions of the API.
- [IOFireWireSBP2ManagementORB](iofirewiresbp2managementorb.md)
  Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LUN interface.
- [IOFireWireSBP2ORB](iofirewiresbp2orb.md)
  Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2Login.
- [FWSBP2FetchAgentWriteCallback](fwsbp2fetchagentwritecallback.md)
- [FWSBP2LoginCallback](fwsbp2logincallback.md)
- [FWSBP2LoginCompleteParams](fwsbp2logincompleteparams.md)
- [FWSBP2LoginCompleteParamsPtr](fwsbp2logincompleteparamsptr.md)
- [FWSBP2LoginResponse](fwsbp2loginresponse.md)
- [FWSBP2LoginResponsePtr](fwsbp2loginresponseptr.md)
- [FWSBP2LogoutCallback](fwsbp2logoutcallback.md)
- [FWSBP2LogoutCompleteParams](fwsbp2logoutcompleteparams.md)
- [FWSBP2LogoutCompleteParamsPtr](fwsbp2logoutcompleteparamsptr.md)
- [FWSBP2ManagementCallback](fwsbp2managementcallback.md)
- [FWSBP2NotifyCallback](fwsbp2notifycallback.md)
- [FWSBP2NotifyParams](fwsbp2notifyparams.md)
- [FWSBP2NotifyParamsPtr](fwsbp2notifyparamsptr.md)
- [FWSBP2ReconnectParams](fwsbp2reconnectparams.md)
- [FWSBP2ReconnectParamsPtr](fwsbp2reconnectparamsptr.md)
- [FWSBP2StatusBlock](fwsbp2statusblock.md)
- [FWSBP2StatusCallback](fwsbp2statuscallback.md)
### Address Spaces
- [IOFWAddressSpaceAux](iofwaddressspaceaux.md)
- [IOFWPhysicalAddressSpaceAux](iofwphysicaladdressspaceaux.md)
- [IOFWPseudoAddressSpaceAux](iofwpseudoaddressspaceaux.md)
- [IOFWSimpleContiguousPhysicalAddressSpace](iofwsimplecontiguousphysicaladdressspace.md)
- [IOFireWirePCRSpace](iofirewirepcrspace.md)
  object to multiplex users of the PCR plug registers
- [IOFWPseudoAddressSpace](iofwpseudoaddressspace.md)
- [IOFWSimplePhysicalAddressSpace](iofwsimplephysicaladdressspace.md)
- [IOFWPhysicalAddressSpace](iofwphysicaladdressspace.md)
- [IOFWAddressSpace](iofwaddressspace.md)
### Commands
- [IOFWCompareAndSwapCommand](iofwcompareandswapcommand.md)
- [IOFWAsyncCommand](iofwasynccommand.md)
  Send an async request to a device
- [IOFWAsyncPHYCommand](iofwasyncphycommand.md)
  Send an async PHY packet
- [IOFWAsyncStreamCommand](iofwasyncstreamcommand.md)
  Send an async stream packet
- [IOFWBusCommand](iofwbuscommand.md)
  Bus control commands
- [IOFWCommand](iofwcommand.md)
  Base class for FireWire commands
- [IOFWDelayCommand](iofwdelaycommand.md)
  Command to execute some code after a specified delay (in microseconds) All it does is timeout after the specified delay, hence calling the completion callback.
- [IOFWReadCommand](iofwreadcommand.md)
- [IOFWReadQuadCommand](iofwreadquadcommand.md)
  An easier to use version of IOFWReadCommand for use when the data to be transferred is an integer number of quads. Note that block read requests will be used for transfers greater than one quad unless setMaxPacket(4) is called.
- [IOFWWriteCommand](iofwwritecommand.md)
- [IOFWWriteQuadCommand](iofwwritequadcommand.md)
  An easier to use version of IOFWWriteCommand for use when the data to be transferred is small and an integer number of quads. Note that block read requests will be used for transfers greater than one quad unless setMaxPacket(4) is called. kMaxWriteQuads is the largest legal number of quads that this object can be asked to transfer (the data is copied into an internal buffer in init() and reinit()).
### Utilities
- [SubtractFWCycleTimeFromFWCycleTime](1589090-subtractfwcycletimefromfwcycleti.md)
- [AddFWCycleTimeToFWCycleTime](1589089-addfwcycletimetofwcycletime.md)
- [IOFWGetAbsoluteTime](1589086-iofwgetabsolutetime.md)
- [FWComputeCRC16](1589088-fwcomputecrc16.md)
- [FWUpdateCRC16](1589087-fwupdatecrc16.md)
### Types
- [IOFWDuplicateGUIDRec](iofwduplicateguidrec.md)
- [IOFWARxReqIntCompleteHandler](iofwarxreqintcompletehandler.md)
- [IOFWAVCAsyncCommandState](iofwavcasynccommandstate.md)
- [IOFWAVCPlugTypes](iofwavcplugtypes.md)
- [IOFWAVCProtocolUserClientAsyncCommandCodes](iofwavcprotocoluserclientasynccommandcodes.md)
- [IOFWAVCProtocolUserClientCommandCodes](iofwavcprotocoluserclientcommandcodes.md)
- [IOFWAVCSubunitPlugMessages](iofwavcsubunitplugmessages.md)
- [IOFWAVCUserClientAsyncCommandCodes](iofwavcuserclientasynccommandcodes.md)
- [IOFWAVCUserClientCommandCodes](iofwavcuserclientcommandcodes.md)
- [IOFWCmdQ](iofwcmdq.md)
  Structure for head of a queue of IOFWCommands
- [IOFWDCLNotificationType](iofwdclnotificationtype.md)
- [IOFWIsochPortOptions](iofwisochportoptions.md)
- [IOFWIsochResourceFlags](iofwisochresourceflags.md)
- [IOFWNodeScan](iofwnodescan.md)
- [IOFWPhysicalAccessMode](iofwphysicalaccessmode.md)
- [IOFWReadFlags](iofwreadflags.md)
- [IOFWRequestRefCon](iofwrequestrefcon.md)
- [IOFWSBP2UserClientCommandCodes](iofwsbp2userclientcommandcodes.md)
- [IOFWSecurityMode](iofwsecuritymode.md)
- [IOFWSpeed](iofwspeed.md)
- [IOFWWriteFlags](iofwwriteflags.md)
- [IOFireWireAVCAsynchronousCommandCallback](iofirewireavcasynchronouscommandcallback.md)
- [IOFireWireAVCSubunitPlugHandlerCallback](iofirewireavcsubunitplughandlercallback.md)
- [IOFireWireAVCTargetCommandHandlerCallback](iofirewireavctargetcommandhandlercallback.md)
- [IOFireWirePCRCallback](iofirewirepcrcallback.md)
  Callback called after a successful lock transaction to a plug.
- [IOFireWireSessionRef](iofirewiresessionref.md)
- [IOAVCCommandResponse](ioavccommandresponse.md)
- [IOAVCFrameFields](ioavcframefields.md)
- [IOAVCOpcodes](ioavcopcodes.md)
- [IOAVCUnitTypes](ioavcunittypes.md)
- [FWAddress](fwaddress.md)
- [FWAddressPtr](fwaddressptr.md)
- [FWAsyncPHYCallback](fwasyncphycallback.md)
- [FWAsyncStreamCallback](fwasyncstreamcallback.md)
- [FWAsyncStreamReceiveCallback](fwasyncstreamreceivecallback.md)
- [FWBusCallback](fwbuscallback.md)
- [FWClientCommandID](fwclientcommandid.md)
- [FWDeviceCallback](fwdevicecallback.md)
- [FWIsochChannelForceStopNotificationProc](fwisochchannelforcestopnotificationproc.md)
- [FWIsochChannelForceStopNotificationProcPtr](fwisochchannelforcestopnotificationprocptr.md)
- [FWMultiIsochReceiveListenerCallback](fwmultiisochreceivelistenercallback.md)
- [FWPHYPacketCallback](fwphypacketcallback.md)
- [FWReadCallback](fwreadcallback.md)
  Callback called when a read request packet is received for a 'virtual' firewire address.
- [FWSegment](fwsegment.md)
- [FWWriteCallback](fwwritecallback.md)
  Callback called when a write request packet is received for a 'virtual' firewire address.
### Global IDs
- [gFireWireModel_ID](gfirewiremodel_id.md)
- [gFireWireNodeID](gfirewirenodeid.md)
- [gFireWireProduct_Name](gfirewireproduct_name.md)
- [gFireWireROM](gfirewirerom.md)
- [gFireWireSelfIDs](gfirewireselfids.md)
- [gFireWireSpeed](gfirewirespeed.md)
- [gFireWireTDM](gfirewiretdm.md)
- [gFireWireUnit_SW_Version](gfirewireunit_sw_version.md)
- [gFireWireUnit_Spec_ID](gfirewireunit_spec_id.md)
- [gFireWireVendor_ID](gfirewirevendor_id.md)
- [gFireWireVendor_Name](gfirewirevendor_name.md)
- [gFireWire_GUID](gfirewire_guid.md)
### FireWire Types
- [UCInfo](ucinfo.md)
- [IOLocalConfigDirectory](iolocalconfigdirectory.md)
- [IOConfigDirectory](ioconfigdirectory.md)
- [IOFireWireDuplicateGUIDList](iofirewireduplicateguidlist.md)
- [IOFireWireIRMAllocation](iofirewireirmallocation.md)
- [IOFireWireMultiIsochReceiveListener](iofirewiremultiisochreceivelistener.md)
- [IOFWPHYPacketListener](iofwphypacketlistener.md)
- [IOFireWireMultiIsochReceivePacket](iofirewiremultiisochreceivepacket.md)
- [IOFireWirePowerManager](iofirewirepowermanager.md)
- [IOFWIsochChannel](iofwisochchannel.md)
- [IOFWIsochPort](iofwisochport.md)
- [IOFWLocalIsochPort](iofwlocalisochport.md)
- [IOFWSyncer](iofwsyncer.md)
- [IOFWUserObjectExporter](iofwuserobjectexporter.md)

## See Also

- [ATA](hardware_families/ata.md)
  Implement a driver that supports Advanced Technology Attachment (ATA) devices.
- [Bluetooth](hardware_families/bluetooth.md)
  Implement a driver that supports Bluetooth devices.
- [PCI](hardware_families/pci.md)
  Implement a driver that supports Thunderbolt devices or PCI cards.
- [USB](hardware_families/usb.md)
  Implement a driver that supports Universal Serial Bus (USB) devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/firewire)*