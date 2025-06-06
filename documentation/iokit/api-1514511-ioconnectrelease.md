# IOConnectRelease(_:)

**Framework**: IOKit  
**Kind**: func

Remove a reference to the connect handle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
func IOConnectRelease(_ connect: io_connect_t) -> kern_return_t
```

#### Return_value

A kern_return_t error code.

#### Discussion

Removes a reference to the connect handle. If the last reference is removed an implicit IOServiceClose is performed.

## Parameters

- `connect`: The connect handle created by IOServiceOpen.

## See Also

- [func IOBSDNameMatching(mach_port_t, UInt32, UnsafePointer<CChar>!) -> CFMutableDictionary!](1514486-iobsdnamematching.md)
  Create a matching dictionary that specifies an IOService match based on BSD device name.
- [func IOConnectAddClient(io_connect_t, io_connect_t) -> kern_return_t](1514609-ioconnectaddclient.md)
  Inform a connection of a second connection.
- [func IOConnectAddRef(io_connect_t) -> kern_return_t](1514739-ioconnectaddref.md)
  Adds a reference to the connect handle.
- [func IOConnectGetService(io_connect_t, UnsafeMutablePointer<io_service_t>!) -> kern_return_t](1514438-ioconnectgetservice.md)
  Returns the IOService a connect handle was opened on.
- [func IOConnectMapMemory(io_connect_t, UInt32, task_port_t, UnsafeMutablePointer<mach_vm_address_t>!, UnsafeMutablePointer<mach_vm_size_t>!, IOOptionBits) -> kern_return_t](1514377-ioconnectmapmemory.md)
  Map hardware or shared memory into the caller's task.
- [func IOConnectMapMemory64(io_connect_t, UInt32, task_port_t, UnsafeMutablePointer<mach_vm_address_t>!, UnsafeMutablePointer<mach_vm_size_t>!, IOOptionBits) -> kern_return_t](1514862-ioconnectmapmemory64.md)
  Map hardware or shared memory into the caller's task.
- [func IOConnectSetCFProperties(io_connect_t, CFTypeRef!) -> kern_return_t](1514713-ioconnectsetcfproperties.md)
  Set CF container based properties on a connection.
- [func IOConnectSetCFProperty(io_connect_t, CFString!, CFTypeRef!) -> kern_return_t](1514796-ioconnectsetcfproperty.md)
  Set a CF container based property on a connection.
- [func IOConnectSetNotificationPort(io_connect_t, UInt32, mach_port_t, UInt) -> kern_return_t](1514541-ioconnectsetnotificationport.md)
  Set a port to receive family specific notifications.
- [func IOConnectUnmapMemory(io_connect_t, UInt32, task_port_t, mach_vm_address_t) -> kern_return_t](1514527-ioconnectunmapmemory.md)
  Remove a mapping made with IOConnectMapMemory.
- [func IOConnectUnmapMemory64(io_connect_t, UInt32, task_port_t, mach_vm_address_t) -> kern_return_t](1514760-ioconnectunmapmemory64.md)
  Remove a mapping made with IOConnectMapMemory64.
- [func IOCreateReceivePort(UInt32, UnsafeMutablePointer<mach_port_t>!) -> kern_return_t](1514698-iocreatereceiveport.md)
  Creates and returns a mach port suitable for receiving IOKit messages of the specified type.
- [func IODispatchCalloutFromMessage(UnsafeMutableRawPointer!, UnsafeMutablePointer<mach_msg_header_t>!, UnsafeMutableRawPointer!)](1514775-iodispatchcalloutfrommessage.md)
  Dispatches callback notifications from a mach message.
- [func IOIteratorIsValid(io_iterator_t) -> boolean_t](1514556-ioiteratorisvalid.md)
  Checks an iterator is still valid.
- [func IOIteratorNext(io_iterator_t) -> io_object_t](1514741-ioiteratornext.md)
  Returns the next object in an iteration.
- [func IOIteratorReset(io_iterator_t)](1514379-ioiteratorreset.md)
  Resets an iteration back to the beginning.
- [func IOKitGetBusyState(mach_port_t, UnsafeMutablePointer<UInt32>!) -> kern_return_t](1514460-iokitgetbusystate.md)
  Returns the busyState of all IOServices.
- [func IOKitWaitQuiet(mach_port_t, UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t](1514440-iokitwaitquiet.md)
  Wait for a all IOServices' busyState to be zero.
- [func IOMasterPort(mach_port_t, UnsafeMutablePointer<mach_port_t>!) -> kern_return_t](1514652-iomasterport.md)
  Returns the mach port used to initiate communication with IOKit.
- [func IONotificationPortCreate(mach_port_t) -> IONotificationPortRef!](1514480-ionotificationportcreate.md)
  Creates and returns a notification object for receiving IOKit notifications of new devices or state changes.
- [func IONotificationPortDestroy(IONotificationPortRef!)](1514751-ionotificationportdestroy.md)
  Destroys a notification object created with IONotificationPortCreate. Also destroys any mach_port's or CFRunLoopSources obatined from [`IONotificationPortGetRunLoopSource(_:)`](1514599-ionotificationportgetrunloopsour.md) or [`IONotificationPortGetMachPort(_:)`](1514875-ionotificationportgetmachport.md)
- [func IONotificationPortGetMachPort(IONotificationPortRef!) -> mach_port_t](1514875-ionotificationportgetmachport.md)
  Returns a mach_port to be used to listen for notifications.
- [func IONotificationPortGetRunLoopSource(IONotificationPortRef!) -> Unmanaged<CFRunLoopSource>!](1514599-ionotificationportgetrunloopsour.md)
  Returns a CFRunLoopSource to be used to listen for notifications.
- [func IONotificationPortSetDispatchQueue(IONotificationPortRef!, dispatch_queue_t!)](1514596-ionotificationportsetdispatchque.md)
  Sets a dispatch queue to be used to listen for notifications.
- [func IOObjectConformsTo(io_object_t, UnsafePointer<CChar>!) -> boolean_t](1514505-ioobjectconformsto.md)
  Performs an OSDynamicCast operation on an IOKit object.
- [func IOObjectCopyBundleIdentifierForClass(CFString!) -> Unmanaged<CFString>!](1514375-ioobjectcopybundleidentifierforc.md)
  Return the bundle identifier of the given class.
- [func IOObjectCopyClass(io_object_t) -> Unmanaged<CFString>!](1514781-ioobjectcopyclass.md)
  Return the class name of an IOKit object.
- [func IOObjectCopySuperclassForClass(CFString!) -> Unmanaged<CFString>!](1514635-ioobjectcopysuperclassforclass.md)
  Return the superclass name of the given class.
- [func IOObjectGetClass(io_object_t, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514756-ioobjectgetclass.md)
  Return the class name of an IOKit object.
- [func IOObjectGetKernelRetainCount(io_object_t) -> UInt32](1514325-ioobjectgetkernelretaincount.md)
  Returns kernel retain count of an IOKit object.
- [func IOObjectGetRetainCount(io_object_t) -> UInt32](1514824-ioobjectgetretaincount.md)
  Returns kernel retain count of an IOKit object. Identical to IOObjectGetKernelRetainCount() but available prior to Mac OS 10.6.
- [func IOObjectGetUserRetainCount(io_object_t) -> UInt32](1514464-ioobjectgetuserretaincount.md)
  Returns the retain count for the current process of an IOKit object.
- [func IOObjectIsEqualTo(io_object_t, io_object_t) -> boolean_t](1514563-ioobjectisequalto.md)
  Checks two object handles to see if they represent the same kernel object.
- [func IOObjectRelease(io_object_t) -> kern_return_t](1514627-ioobjectrelease.md)
  Releases an object handle previously returned by IOKitLib.
- [func IOObjectRetain(io_object_t) -> kern_return_t](1514769-ioobjectretain.md)
  Retains an object handle previously returned by IOKitLib.
- [func IORegistryCreateIterator(mach_port_t, UnsafePointer<CChar>!, IOOptionBits, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514238-ioregistrycreateiterator.md)
  Create an iterator rooted at the registry root.
- [func IORegistryEntryCreateCFProperties(io_registry_entry_t, UnsafeMutablePointer<Unmanaged<CFMutableDictionary>?>!, CFAllocator!, IOOptionBits) -> kern_return_t](1514310-ioregistryentrycreatecfpropertie.md)
  Create a CF dictionary representation of a registry entry's property table.
- [func IORegistryEntryCreateCFProperty(io_registry_entry_t, CFString!, CFAllocator!, IOOptionBits) -> Unmanaged<CFTypeRef>!](1514293-ioregistryentrycreatecfproperty.md)
  Create a CF representation of a registry entry's property.
- [func IORegistryEntryCreateIterator(io_registry_entry_t, UnsafePointer<CChar>!, IOOptionBits, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514318-ioregistryentrycreateiterator.md)
  Create an iterator rooted at a given registry entry.
- [func IORegistryEntryFromPath(mach_port_t, UnsafePointer<CChar>!) -> io_registry_entry_t](1514802-ioregistryentryfrompath.md)
  Looks up a registry entry by path.
- [func IORegistryEntryGetChildEntry(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<io_registry_entry_t>!) -> kern_return_t](1514496-ioregistryentrygetchildentry.md)
  Returns the first child of a registry entry in a plane.
- [func IORegistryEntryGetChildIterator(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514703-ioregistryentrygetchilditerator.md)
  Returns an iterator over a registry entry’s child entries in a plane.
- [func IORegistryEntryGetLocationInPlane(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514340-ioregistryentrygetlocationinplan.md)
  Returns a C-string location assigned to a registry entry, in a specified plane.
- [func IORegistryEntryGetName(io_registry_entry_t, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514323-ioregistryentrygetname.md)
  Returns a C-string name assigned to a registry entry.
- [func IORegistryEntryGetNameInPlane(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514475-ioregistryentrygetnameinplane.md)
  Returns a C-string name assigned to a registry entry, in a specified plane.
- [func IORegistryEntryGetParentEntry(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<io_registry_entry_t>!) -> kern_return_t](1514454-ioregistryentrygetparententry.md)
  Returns the first parent of a registry entry in a plane.
- [func IORegistryEntryGetParentIterator(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514366-ioregistryentrygetparentiterator.md)
  Returns an iterator over a registry entry’s parent entries in a plane.
- [func IORegistryEntryGetPath(io_registry_entry_t, UnsafePointer<CChar>!, UnsafeMutablePointer<CChar>!) -> kern_return_t](1514229-ioregistryentrygetpath.md)
  Create a path for a registry entry.
- [func IORegistryEntryGetRegistryEntryID(io_registry_entry_t, UnsafeMutablePointer<UInt64>!) -> kern_return_t](1514719-ioregistryentrygetregistryentryi.md)
  Returns an ID for the registry entry that is global to all tasks.
- [func IORegistryEntryIDMatching(UInt64) -> CFMutableDictionary!](1514880-ioregistryentryidmatching.md)
  Create a matching dictionary that specifies an IOService match based on a registry entry ID.
- [func IORegistryEntryInPlane(io_registry_entry_t, UnsafePointer<CChar>!) -> boolean_t](1514668-ioregistryentryinplane.md)
  Determines if the registry entry is attached in a plane.
- [func IORegistryEntrySearchCFProperty(io_registry_entry_t, UnsafePointer<CChar>!, CFString!, CFAllocator!, IOOptionBits) -> CFTypeRef!](1514537-ioregistryentrysearchcfproperty.md)
  Create a CF representation of a registry entry's property.
- [func IORegistryEntrySetCFProperties(io_registry_entry_t, CFTypeRef!) -> kern_return_t](1514414-ioregistryentrysetcfproperties.md)
  Set CF container based properties in a registry entry.
- [func IORegistryEntrySetCFProperty(io_registry_entry_t, CFString!, CFTypeRef!) -> kern_return_t](1514882-ioregistryentrysetcfproperty.md)
  Set a CF container based property in a registry entry.
- [func IORegistryGetRootEntry(mach_port_t) -> io_registry_entry_t](1514878-ioregistrygetrootentry.md)
  Return a handle to the registry root.
- [func IORegistryIteratorEnterEntry(io_iterator_t) -> kern_return_t](1514822-ioregistryiteratorenterentry.md)
  Recurse into the current entry in the registry iteration.
- [func IORegistryIteratorExitEntry(io_iterator_t) -> kern_return_t](1514334-ioregistryiteratorexitentry.md)
  Exits a level of recursion, restoring the current entry.
- [func IOServiceAddInterestNotification(IONotificationPortRef!, io_service_t, UnsafePointer<CChar>!, IOServiceInterestCallback!, UnsafeMutableRawPointer!, UnsafeMutablePointer<io_object_t>!) -> kern_return_t](1514866-ioserviceaddinterestnotification.md)
  Register for notification of state changes in an IOService.
- [func IOServiceAddMatchingNotification(IONotificationPortRef!, UnsafePointer<CChar>!, CFDictionary!, IOServiceMatchingCallback!, UnsafeMutableRawPointer!, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514362-ioserviceaddmatchingnotification.md)
  Look up registered IOService objects that match a matching dictionary, and install a notification request of new IOServices that match.
- [func IOServiceClose(io_connect_t) -> kern_return_t](1514646-ioserviceclose.md)
  Close a connection to an IOService and destroy the connect handle.
- [func IOServiceGetBusyState(io_service_t, UnsafeMutablePointer<UInt32>!) -> kern_return_t](1514607-ioservicegetbusystate.md)
  Returns the busyState of an IOService.
- [func IOServiceGetMatchingService(mach_port_t, CFDictionary!) -> io_service_t](1514535-ioservicegetmatchingservice.md)
  Look up a registered IOService object that matches a matching dictionary.
- [func IOServiceGetMatchingServices(mach_port_t, CFDictionary!, UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](1514494-ioservicegetmatchingservices.md)
  Look up registered IOService objects that match a matching dictionary.
- [func IOServiceMatching(UnsafePointer<CChar>!) -> CFMutableDictionary!](1514687-ioservicematching.md)
  Create a matching dictionary that specifies an IOService class match.
- [func IOServiceMatchPropertyTable(io_service_t, CFDictionary!, UnsafeMutablePointer<boolean_t>!) -> kern_return_t](1514685-ioservicematchpropertytable.md)
  Match an IOService objects with matching dictionary.
- [func IOServiceNameMatching(UnsafePointer<CChar>!) -> CFMutableDictionary!](1514416-ioservicenamematching.md)
  Create a matching dictionary that specifies an IOService name match.
- [func IOServiceOpen(io_service_t, task_port_t, UInt32, UnsafeMutablePointer<io_connect_t>!) -> kern_return_t](1514515-ioserviceopen.md)
  A request to create a connection to an IOService.
- [func IOServiceRequestProbe(io_service_t, UInt32) -> kern_return_t](1514364-ioservicerequestprobe.md)
  A request to rescan a bus for device changes.
- [func IOServiceWaitQuiet(io_service_t, UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t](1514573-ioservicewaitquiet.md)
  Wait for an IOService's busyState to be zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514511-ioconnectrelease)*