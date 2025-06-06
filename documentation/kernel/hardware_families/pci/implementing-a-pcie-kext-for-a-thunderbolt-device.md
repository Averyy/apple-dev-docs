# Implementing a PCIe Kext for a Thunderbolt Device

**Framework**: Kernel

Create an IOKit driver to support Thunderbolt devices that implement features not supported in PCIDriverKit, such as wireless networking or audio. 

#### Overview

If you manufacture Thunderbolt devices, create a custom driver only when your device contains unique features that require additional support. Apple supplies drivers for many standard protocols and device types, alleviating the need for you to create custom drivers in some cases. However, if your Thunderbolt device contains PCIe endpoints that require additional support, create a custom PCIe driver to support those endpoints. 

Create the PCIe driver for your Thunderbolt device using PCIDriverKit whenever possible. DriverKit extensions run in user space and require less effort to develop, debug, and deploy. However, PCIDriverKit may not be an option in all cases. If your device supports wireless networking or audio, or if it requires specific kernel resources, you must create your driver as an IOKit kernel extension.  

Kernel extensions run in the kernel process space of the target Mac computer using the native architecture. To support both Apple silicon and Intel-based Mac computers, build your driver as a universal binary. For the most part, your driver code is identical on both Apple silicon and Intel-based Macs. However, if you’re updating a driver you previously built only for Intel-based Macs, you may need to update your code to correctly handle:

- Pointer authentication
- Memory architecture differences between Apple silicon and Intel-based Macs
- Kernel integrity protection (KIP) restrictions

For basic information about building kernel extensions, see [`Kernel Extension Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIntro/introduction.html#//apple_ref/doc/uid/TP40001063). For information about how to develop drivers using PCIDriverKit, see [`Creating Custom PCIe Drivers for Thunderbolt Devices`](https://developer.apple.com/documentation/pcidriverkit/creating-custom-pcie-drivers-for-thunderbolt-devices). 

##### 3686769

The life cycle of a kernel extension in macOS 11 remains unchanged from previous versions of macOS. In particular, the system loads your custom [`IOService`](ioservice.md) subclass, and calls its [`init`](https://developer.apple.com/documentation/driverkit/ioservice/init) and [`Start`](https://developer.apple.com/documentation/driverkit/ioservice/start) methods. Use the [`init`](https://developer.apple.com/documentation/driverkit/ioservice/init) method to allocate your driver’s data structures. Use the [`Start`](https://developer.apple.com/documentation/driverkit/ioservice/start) method to configure your hardware, install event handlers, and prepare your driver to handle requests. When your driver is no longer needed, the system calls the corresponding [`Stop`](https://developer.apple.com/documentation/driverkit/ioservice/stop) and [`free`](https://developer.apple.com/documentation/driverkit/ioservice/free) methods to release any driver-related resources. 

For information about how to implement your driver life cycle, see [`IOKit Fundamentals`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP0000011).

##### 3686768

Thunderbolt devices access system memory through a system-provided I/O memory management unit (IOMMU). On Intel-based Mac computers, the system provides a single IOMMU and gives all devices a shared view of system memory. On Macs with Apple silicon, the system gives each device its own IOMMU. Always implement your driver as if it has its own IOMMU, and never assume you have a shared view of system memory. 

To transfer memory correctly on all types of Macs, use an [`IODMACommand`](iodmacommand.md) object configured with the [`kMapped`](iodmacommand/mappingoptions/kmapped.md) option. Typically, you create one or more of these objects at startup and reuse them multiple times. To create one, fetch the [`IOMapper`](iomapper.md) object associated with your driver’s provider object and pass it to the appropriate [`IODMACommand`](iodmacommand.md) creation function. For example, the following code creates a command object for 64-bit transfers with several standard transfer options.  

```occ
IOMapper *mapper = IOMapper::copyMapperForDevice(provider);
IODMACommand *dmaCommand = 
     IODMACommand::withSpecification(kIODMACommandOutputHost64, 
              64,      // 64-bit transfers
              0,       // Unlimited segment sizes
              (IODMACommand::MappingOptions)(IODMACommand::kMapped),
              0,       // No maximum transfer size
              1,       // 1-byte alignment
              mapper, 
              NULL);
```

When you are ready to transfer data to or from your device, create a new memory descriptor to handle the transferred data. Configure the descriptor with the [`kIODirectionIn`](1643339-anonymous/kiodirectionin.md) direction to read data from the device into memory, or configure it with the [`kIODirectionOut`](1643339-anonymous/kiodirectionout.md) direction to send data from memory out to the device. Assign the memory descriptor to your [`IODMACommand`](iodmacommand.md) object using its [`setMemoryDescriptor`](iodmacommand/1547727-setmemorydescriptor.md) method, the default options for which begin the transfer operation immediately. 

> **Note**: Calls to the [`getPhysicalSegment`](iomemorydescriptor/1442068-getphysicalsegment.md) method of [`IOMemoryDescriptor`](iomemorydescriptor.md) fail on Apple silicon. When updating older kernel extensions to support Apple silicon, replace all calls to that method with [`IODMACommand`](iodmacommand.md) objects. 

##### 3686966

When it detects new hardware, the system must find an appropriate set of drivers to manage that hardware. It does so by comparing the hardware details to information found in the `kIOKitPersonalitiesKey` key of each driver’s `Info.plist` file, and identifying the drivers that best match the hardware. For example, a driver might match only against devices from a specific manufacturer, or devices that support only a specific communication protocol. 

To indicate that your PCIe driver supports Thunderbolt, include the `IOPCITunnelCompatible` key in your driver’s personality dictionaries. Include this key only if the [`IOService`](ioservice.md) subclass in the `IOClass` key of that dictionary is able to communicate with your Thunderbolt device. The following example shows the presence of this key in a custom PCI driver.

```other
<key>MyDriverKitDriver</key>
<dict>
    <key>CFBundleIdentifier</key>
    <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
    <key>CFBundleIdentifierKernel</key>
    <string>com.apple.kpi.iokit</string>
    <key>IOClass</key>
    <string>IOUserService</string>
    <key>IOPCIPauseCompatible</key>
    <true/>
    <key>IOPCIPrimaryMatch</key>
    <string>0x0000ABCD&amp;0x0000FFFF</string>
    <key>IOPCITunnelCompatible</key>
    <true/>
    <key>IOProviderClass</key>
    <string>IOPCIDevice</string>
    <key>IOResourceMatch</key>
    <string>IOKit</string>
    <key>IOUserClass</key>
    <string>MyPCIDriverKitDriverClassName</string>
    <key>IOUserServerName</key>
    <string>com.apple.MyDriverKitDriver</string>
</dict>
```

When a device supports Thunderbolt, the system adds the `IOPCITunnelled` property to one of the drivers in the chain and sets the value of that property to true. If you need to know whether the device is a Thunderbolt device, search for this property in your driver code. For example, you might do so before enabling specific features in your code that require Thunderbolt. The following example searches all parent drivers in the global service plane for the property. If the property is present, the code checks its value to determine whether the device is a Thunderbolt device.

```occ
bool isThunderboltEnabled = false;
OSContainer* container = NULL;
if (SearchProperty("IOPCITunnelled", "IOService", kIOServiceSearchPropertyParents, &container) == kIOReturnSuccess)
{
   OSBoolean* boolVar = OSDynamicCast(OSBoolean, container);
   if (boolVar != NULL && boolVar == kOSBooleanTrue)
   {
      // The device supports Thunderbolt.
      isThunderboltEnabled = true;
   }
   OSSafeReleaseNULL(container);
}
```

##### 3686967

Users can disconnect most Thunderbolt devices at any time, but macOS doesn’t allow them to disconnect external storage devices without properly ejecting them. If your PCI driver presents the device as storage to the system, notify the system early in your driver’s [`start`](ioservice/1532606-start.md) method by setting the `Physical Interconnect Location` property to `External`, as shown in the following example.

```occ
// Add the Physical Interconnect Location property to the driver.
OSDictionary* dict = OSDictionary::withCapacity(1);
OSString* externalStr = OSString::withCString("External");
dict->setObject("Physical Interconnect Location", externalStr);
SetProperties(dict);
OSSafeReleaseNULL(externalStr);
OSSafeReleaseNULL(dict);
```

> ❗ **Important**: Always set the `Physical Interconnect Location` property early in your driver’s [`start`](ioservice/1532606-start.md) method. Don’t set it after you access the device. 

##### 3690960

The processors in recent Macs have low-power states that reduce the processor speed and voltage when the computer is idle. These low-power states decrease overall power consumption and heat generation on the system, and improve battery life. However, when a power-state transition occurs, the system temporarily stops all PCI bus traffic while it changes the power state of the processor cores. Halting PCI bus traffic can cause audio glitches and other side effects on devices that are sensitive to the added latency.

To mitigate the problems of any added latency, implement the PCIe latency tolerance reporting (LTR) extended capability in your devices according to the PCIe specifications. If your driver supports legacy devices, schedule your driver’s time-critical DMA operations so that occasional delays don’t affect your device. If you’re unable to adjust the schedule of your DMA operations, call the [`requireMaxBusStall`](ioservice/1532887-requiremaxbusstall.md) method of your [`IOService`](ioservice.md) subclass at the beginning and end of any time-critical transfers. Before a transfer, call this method with the constant that represents the maximum latency your driver can tolerate. For example, specify `kIOMaxBusStall20usec` to delay bus stalls for 20 microseconds. The system avoids entering low-power states for the specified amount of time. After a transfer, restore the default bus stall time by passing `kIOMaxBusStallNone` to the method. 

> ❗ **Important**: Call the [`requireMaxBusStall`](ioservice/1532887-requiremaxbusstall.md) method only if there is no other way to make your device and driver more tolerant of increased memory latency. The method prevents the system from transitioning to lower-power states, which can significantly impact battery life on portable systems. It may also increase system heat, and require device fans to run longer. Overuse of this API may also lead to kernel panics. 

Because audio transfers occur only when your audio engine is running, call the [`requireMaxBusStall`](ioservice/1532887-requiremaxbusstall.md) method in the [`performAudioEngineStart`](ioaudioengine/1561628-performaudioenginestart.md) and [`performAudioEngineStop`](ioaudioengine/1561589-performaudioenginestop.md) methods of [`IOAudioEngine`](ioaudioengine.md). The following example shows an implementation of these methods that prevents PCI bus stalls for 10 microseconds when a transfer begins, and restores the default bus stall time at the end of the transfer. 

```occ
/* Header file */
class MyAudioEngine : public IOAudioEngine
{
    /* virtual overrides, custom function, variables, etc... */
public:
    virtual IOReturn performAudioEngineStart();
    virtual IOReturn performAudioEngineStop();
}


/* Implementation file */
IOReturn MyAudioEngine::performAudioEngineStart()
{
    requireMaxBusStall(kIOMaxBusStall10usec);
    return IOAudioEngine::performAudioEngineStart();
}

IOReturn MyAudioEngine::performAudioEngineStop()
{
    // Zero means restore default bus stall time.
    // It's now safe to go into lowest-power states.
    requireMaxBusStall(kIOMaxBusStallNone);
    return IOAudioEngine::performAudioEngineStop();
}
```

##### 3686767

Build your kernel extension as a universal binary on macOS 11 and later. A universal binary supports both Apple silicon and Intel-based Mac computers. 

On Macs with Apple silicon, the kernel is built for the ARM64e architecture, so you must similarly build your kernel extensions for that architecture. The ARM64e architecture enables pointer authentication, a security feature that prevents the unexpected modification of pointers at runtime. For more information about how to support pointer authentication, see [`Preparing your app to work with pointer authentication`](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication). 

## See Also

- [IOPCIDevice](iopcidevice.md)
  An IOService class representing a PCI device.
- [IOAGPDevice](ioagpdevice.md)
  An IOService class representing an AGP primary device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device)*