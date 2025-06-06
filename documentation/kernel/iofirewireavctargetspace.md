# IOFireWireAVCTargetSpace

**Framework**: Kernel  
**Kind**: cl

object to centralize the AVC Target mode support

**Availability**:
- macOS 10.3+

## Declaration

```swift
class IOFireWireAVCTargetSpace : IOFWPseudoAddressSpace
```

#### Overview

## Topics

### Miscellaneous
- [getAVCTargetSpace](iofirewireavctargetspace/1813826-getavctargetspace.md)
  returns the IOFireWireAVCTargetSpace object for the given FireWire bus
- [init](iofirewireavctargetspace/1813830-init.md)
  initializes the IOFireWireAVCTargetSpace object
- [publishAVCUnitDirectory](iofirewireavctargetspace/1813834-publishavcunitdirectory.md)
  Creates a local AVC Unit directory if it doesn't already exist
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iofirewireavctargetspace/reserved.md)
### Instance Methods
- [- activateWithUserClient](iofirewireavctargetspace/1571597-activatewithuserclient.md)
- [- addSubunit](iofirewireavctargetspace/1571586-addsubunit.md)
- [- canConnectDestPlug](iofirewireavctargetspace/1571631-canconnectdestplug.md)
- [- connectTargetPlugs](iofirewireavctargetspace/1571629-connecttargetplugs.md)
- [- deactivateWithUserClient](iofirewireavctargetspace/1571613-deactivatewithuserclient.md)
- [- disconnectTargetPlugs](iofirewireavctargetspace/1571625-disconnecttargetplugs.md)
- [- doWrite](iofirewireavctargetspace/1571609-dowrite.md)
- [- findAVCRequestHandler](iofirewireavctargetspace/1571598-findavcrequesthandler.md)
- [- getMetaClass](iofirewireavctargetspace/1571595-getmetaclass.md)
- [- getSubunitInfo](iofirewireavctargetspace/1571601-getsubunitinfo.md)
- [- getSubunitPlugSignalFormat](iofirewireavctargetspace/1571599-getsubunitplugsignalformat.md)
- [- getTargetPlugConnection](iofirewireavctargetspace/1571600-gettargetplugconnection.md)
- [- handleConnectCommand](iofirewireavctargetspace/1571604-handleconnectcommand.md)
- [- handleConnectionsCommand](iofirewireavctargetspace/1571591-handleconnectionscommand.md)
- [- handleDisconnectCommand](iofirewireavctargetspace/1571634-handledisconnectcommand.md)
- [- handleInputPlugSignalFormatCommand](iofirewireavctargetspace/1571626-handleinputplugsignalformatcomma.md)
- [- handleOutputPlugSignalFormatCommand](iofirewireavctargetspace/1571616-handleoutputplugsignalformatcomm.md)
- [- handlePlugInfoCommand](iofirewireavctargetspace/1571618-handlepluginfocommand.md)
- [- handlePowerCommand](iofirewireavctargetspace/1571632-handlepowercommand.md)
- [- handleSignalSourceCommand](iofirewireavctargetspace/1571617-handlesignalsourcecommand.md)
- [- handleSubUnitInfoCommand](iofirewireavctargetspace/1571638-handlesubunitinfocommand.md)
- [- handleUnitInfoCommand](iofirewireavctargetspace/1571641-handleunitinfocommand.md)
- [- init](iofirewireavctargetspace/1571614-init.md)
- [- installAVCCommandHandler](iofirewireavctargetspace/1571622-installavccommandhandler.md)
- [- pcrModified](iofirewireavctargetspace/1571636-pcrmodified.md)
- [- publishAVCUnitDirectory](iofirewireavctargetspace/1571592-publishavcunitdirectory.md)
- [- setSubunitPlugSignalFormat](iofirewireavctargetspace/1571583-setsubunitplugsignalformat.md)
- [- subUnitOfTypeCount](iofirewireavctargetspace/1571587-subunitoftypecount.md)
- [- targetSendAVCResponse](iofirewireavctargetspace/1571588-targetsendavcresponse.md)
### Type Methods
- [+ getAVCTargetSpace](iofirewireavctargetspace/1571633-getavctargetspace.md)

## Relationships

### Inherits From
- [IOFWPseudoAddressSpace](iofwpseudoaddressspace.md)

## See Also

- [IOFireWireAVCAsynchronousCommand](iofirewireavcasynchronouscommand.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavctargetspace)*