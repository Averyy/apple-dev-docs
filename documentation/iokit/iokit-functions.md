# IOKit Functions

**Framework**: IOKit

## Topics

### Functions
- [func IOCFSerialize(CFTypeRef!, CFOptionFlags) -> CFData!](1403329-iocfserialize.md)
- [func IOCFUnserialize(UnsafePointer<CChar>!, CFAllocator!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!](1514265-iocfunserialize.md)
- [func IOCFUnserializeBinary(UnsafePointer<CChar>!, Int, CFAllocator!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!](1514876-iocfunserializebinary.md)
- [func IOCFUnserializeWithSize(UnsafePointer<CChar>!, Int, CFAllocator!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!](1514745-iocfunserializewithsize.md)
- [func IOCatalogueGetData(mach_port_t, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>!, UnsafeMutablePointer<UInt32>!) -> kern_return_t](1514233-iocataloguegetdata.md)
- [func IOCatalogueModuleLoaded(mach_port_t, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514886-iocataloguemoduleloaded.md)
- [func IOCatalogueReset(mach_port_t, UInt32) -> kern_return_t](1514702-iocataloguereset.md)
- [func IOCatalogueSendData(mach_port_t, UInt32, UnsafePointer<CChar>!, UInt32) -> kern_return_t](1514405-iocataloguesenddata.md)
- [func IOCatalogueTerminate(mach_port_t, UInt32, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514665-iocatalogueterminate.md)
- [func IOConnectCallAsyncMethod(mach_port_t, UInt32, mach_port_t, UnsafeMutablePointer<UInt64>!, UInt32, UnsafePointer<UInt64>!, UInt32, UnsafeRawPointer!, Int, UnsafeMutablePointer<UInt64>!, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Int>!) -> kern_return_t](1514418-ioconnectcallasyncmethod.md)
- [func IOConnectCallAsyncScalarMethod(mach_port_t, UInt32, mach_port_t, UnsafeMutablePointer<UInt64>!, UInt32, UnsafePointer<UInt64>!, UInt32, UnsafeMutablePointer<UInt64>!, UnsafeMutablePointer<UInt32>!) -> kern_return_t](1514884-ioconnectcallasyncscalarmethod.md)
- [func IOConnectCallAsyncStructMethod(mach_port_t, UInt32, mach_port_t, UnsafeMutablePointer<UInt64>!, UInt32, UnsafeRawPointer!, Int, UnsafeMutableRawPointer!, UnsafeMutablePointer<Int>!) -> kern_return_t](1514403-ioconnectcallasyncstructmethod.md)
- [func IOConnectCallMethod(mach_port_t, UInt32, UnsafePointer<UInt64>!, UInt32, UnsafeRawPointer!, Int, UnsafeMutablePointer<UInt64>!, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Int>!) -> kern_return_t](1514240-ioconnectcallmethod.md)
- [func IOConnectCallScalarMethod(mach_port_t, UInt32, UnsafePointer<UInt64>!, UInt32, UnsafeMutablePointer<UInt64>!, UnsafeMutablePointer<UInt32>!) -> kern_return_t](1514793-ioconnectcallscalarmethod.md)
- [func IOConnectCallStructMethod(mach_port_t, UInt32, UnsafeRawPointer!, Int, UnsafeMutableRawPointer!, UnsafeMutablePointer<Int>!) -> kern_return_t](1514274-ioconnectcallstructmethod.md)
- [func IOConnectTrap0(io_connect_t, UInt32) -> kern_return_t](1514674-ioconnecttrap0.md)
- [func IOConnectTrap1(io_connect_t, UInt32, UInt) -> kern_return_t](1514816-ioconnecttrap1.md)
- [func IOConnectTrap2(io_connect_t, UInt32, UInt, UInt) -> kern_return_t](1514354-ioconnecttrap2.md)
- [func IOConnectTrap3(io_connect_t, UInt32, UInt, UInt, UInt) -> kern_return_t](1514833-ioconnecttrap3.md)
- [func IOConnectTrap4(io_connect_t, UInt32, UInt, UInt, UInt, UInt) -> kern_return_t](1514410-ioconnecttrap4.md)
- [func IOConnectTrap5(io_connect_t, UInt32, UInt, UInt, UInt, UInt, UInt) -> kern_return_t](1514346-ioconnecttrap5.md)
- [func IOConnectTrap6(io_connect_t, UInt32, UInt, UInt, UInt, UInt, UInt, UInt) -> kern_return_t](1514493-ioconnecttrap6.md)
- [func IOCreatePlugInInterfaceForService(io_service_t, CFUUID!, CFUUID!, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>?>!, UnsafeMutablePointer<Int32>!) -> kern_return_t](1412429-iocreateplugininterfaceforservic.md)
- [func IODestroyPlugInInterface(UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>!) -> kern_return_t](1412425-iodestroyplugininterface.md)
- [func IOOpenFirmwarePathMatching(mach_port_t, UInt32, UnsafePointer<CChar>!) -> Unmanaged<CFMutableDictionary>!](1514715-ioopenfirmwarepathmatching.md)
- [func IORegistryEntryCopyFromPath(mach_port_t, CFString!) -> io_registry_entry_t](1514248-ioregistryentrycopyfrompath.md)
- [func IORegistryEntryCopyPath(io_registry_entry_t, UnsafePointer<CChar>!) -> Unmanaged<CFString>!](1514853-ioregistryentrycopypath.md)
- [func IORegistryEntryGetProperty(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<CChar>!, UnsafeMutablePointer<UInt32>!) -> kern_return_t](1514254-ioregistryentrygetproperty.md)
- [func IOServiceAddNotification(mach_port_t, UnsafePointer<CChar>!, CFDictionary!, mach_port_t, UInt, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514382-ioserviceaddnotification.md)
- [func IOServiceAuthorize(io_service_t, UInt32) -> kern_return_t](1514533-ioserviceauthorize.md)
- [func IOServiceOFPathToBSDName(mach_port_t, UnsafePointer<CChar>!, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514661-ioserviceofpathtobsdname.md)
- [func IOServiceOpenAsFileDescriptor(io_service_t, Int32) -> Int32](1514879-ioserviceopenasfiledescriptor.md)
- [func IOURLCreateDataAndPropertiesFromResource(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, CFArray!, UnsafeMutablePointer<Int32>!) -> Bool](1514836-iourlcreatedataandpropertiesfrom.md)
- [func IOURLCreatePropertyFromResource(CFAllocator!, CFURL!, CFString!, UnsafeMutablePointer<Int32>!) -> Unmanaged<CFTypeRef>!](1514499-iourlcreatepropertyfromresource.md)
- [func IOURLWriteDataAndPropertiesToResource(CFURL!, CFData!, CFDictionary!, UnsafeMutablePointer<Int32>!) -> Bool](1514272-iourlwritedataandpropertiestores.md)
- [func OSGetNotificationFromMessage(UnsafeMutablePointer<mach_msg_header_t>!, UInt32, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt>!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!, UnsafeMutablePointer<vm_size_t>!) -> kern_return_t](1514263-osgetnotificationfrommessage.md)
- [func IOMainPort(mach_port_t, UnsafeMutablePointer<mach_port_t>!) -> kern_return_t](3753260-iomainport.md)
- [func IONotificationPortSetImportanceReceiver(IONotificationPortRef!) -> kern_return_t](2870065-ionotificationportsetimportancer.md)
- [func IORPCMessageFromMach(UnsafeMutablePointer<IORPCMessageMach>!, Bool) -> UnsafeMutablePointer<IORPCMessage>!](3325691-iorpcmessagefrommach.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iokit_functions)*