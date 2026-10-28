# IOFireWireAVCTargetSpace

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

object to centralize the AVC Target mode support

**Availability**:
- macOS 10.3+

## Declaration

```cpp
class IOFireWireAVCTargetSpace : IOFWPseudoAddressSpace
```

## Overview

## Topics

### Miscellaneous
- [getAVCTargetSpace](./iofirewireavctargetspace/api-1813826-getavctargetspace.md)
  returns the IOFireWireAVCTargetSpace object for the given FireWire bus
- [init](./iofirewireavctargetspace/api-1813830-init.md)
  initializes the IOFireWireAVCTargetSpace object
- [publishAVCUnitDirectory](./iofirewireavctargetspace/api-1813834-publishavcunitdirectory.md)
  Creates a local AVC Unit directory if it doesn't already exist
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./iofirewireavctargetspace/reserved.md)
### Instance Methods
- [- activateWithUserClient](./iofirewireavctargetspace/api-1571597-activatewithuserclient.md)
- [- addSubunit](./iofirewireavctargetspace/api-1571586-addsubunit.md)
- [- canConnectDestPlug](./iofirewireavctargetspace/api-1571631-canconnectdestplug.md)
- [- connectTargetPlugs](./iofirewireavctargetspace/api-1571629-connecttargetplugs.md)
- [- deactivateWithUserClient](./iofirewireavctargetspace/api-1571613-deactivatewithuserclient.md)
- [- disconnectTargetPlugs](./iofirewireavctargetspace/api-1571625-disconnecttargetplugs.md)
- [- doWrite](./iofirewireavctargetspace/api-1571609-dowrite.md)
- [- findAVCRequestHandler](./iofirewireavctargetspace/api-1571598-findavcrequesthandler.md)
- [- getMetaClass](./iofirewireavctargetspace/api-1571595-getmetaclass.md)
- [- getSubunitInfo](./iofirewireavctargetspace/api-1571601-getsubunitinfo.md)
- [- getSubunitPlugSignalFormat](./iofirewireavctargetspace/api-1571599-getsubunitplugsignalformat.md)
- [- getTargetPlugConnection](./iofirewireavctargetspace/api-1571600-gettargetplugconnection.md)
- [- handleConnectCommand](./iofirewireavctargetspace/api-1571604-handleconnectcommand.md)
- [- handleConnectionsCommand](./iofirewireavctargetspace/api-1571591-handleconnectionscommand.md)
- [- handleDisconnectCommand](./iofirewireavctargetspace/api-1571634-handledisconnectcommand.md)
- [- handleInputPlugSignalFormatCommand](./iofirewireavctargetspace/api-1571626-handleinputplugsignalformatcomma.md)
- [- handleOutputPlugSignalFormatCommand](./iofirewireavctargetspace/api-1571616-handleoutputplugsignalformatcomm.md)
- [- handlePlugInfoCommand](./iofirewireavctargetspace/api-1571618-handlepluginfocommand.md)
- [- handlePowerCommand](./iofirewireavctargetspace/api-1571632-handlepowercommand.md)
- [- handleSignalSourceCommand](./iofirewireavctargetspace/api-1571617-handlesignalsourcecommand.md)
- [- handleSubUnitInfoCommand](./iofirewireavctargetspace/api-1571638-handlesubunitinfocommand.md)
- [- handleUnitInfoCommand](./iofirewireavctargetspace/api-1571641-handleunitinfocommand.md)
- [- init](./iofirewireavctargetspace/api-1571614-init.md)
- [- installAVCCommandHandler](./iofirewireavctargetspace/api-1571622-installavccommandhandler.md)
- [- pcrModified](./iofirewireavctargetspace/api-1571636-pcrmodified.md)
- [- publishAVCUnitDirectory](./iofirewireavctargetspace/api-1571592-publishavcunitdirectory.md)
- [- setSubunitPlugSignalFormat](./iofirewireavctargetspace/api-1571583-setsubunitplugsignalformat.md)
- [- subUnitOfTypeCount](./iofirewireavctargetspace/api-1571587-subunitoftypecount.md)
- [- targetSendAVCResponse](./iofirewireavctargetspace/api-1571588-targetsendavcresponse.md)
### Type Methods
- [+ getAVCTargetSpace](./iofirewireavctargetspace/api-1571633-getavctargetspace.md)

## Relationships

### Inherits From
- [IOFWPseudoAddressSpace](./iofwpseudoaddressspace.md)

## See Also

### AVC Support
- [IOFireWireAVCAsynchronousCommand](./iofirewireavcasynchronouscommand.md)
- [IOFireWireAVCCommand](./iofirewireavccommand.md)
- [AVCCommandHandlerInfo](./avccommandhandlerinfo.md)
- [AVCConnectionRecord](./avcconnectionrecord.md)
- [AVCSubunitInfo](./avcsubunitinfo.md)
- [AVCConnectTargetPlugsInParams](./avcconnecttargetplugsinparams.md)
- [AVCConnectTargetPlugsOutParams](./avcconnecttargetplugsoutparams.md)
- [AVCGetTargetPlugConnectionInParams](./avcgettargetplugconnectioninparams.md)
- [AVCGetTargetPlugConnectionOutParams](./avcgettargetplugconnectionoutparams.md)
- [AVCSubunitPlugRecord](./avcsubunitplugrecord.md)
- [AVCUnitPlugRecord](./avcunitplugrecord.md)
- [AVCUnitPlugs](./avcunitplugs.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavctargetspace)*