# Kernel

**Framework**: Kernel

Develop kernel-resident device drivers and kernel extensions.

**Availability**:
- macOS 10.0+

#### Overview

The Kernel Framework provides the APIs and support for kernel-resident device drivers and other kernel extensions. It defines the base class for I/O Kit device drivers ([`IOService`](ioservice-5h.md)), several helper classes, and the families that support many types of devices.

## Topics

### Kernel Extensions
- [Implementing drivers, system extensions, and kexts](implementing_drivers_system_extensions_and_kexts.md)
  Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks. 
- [Installing a custom kernel extension](../apple-silicon/installing-a-custom-kernel-extension.md)
  Install kernel extensions using a custom installer package, and help users understand the installation process.
- [Debugging a custom kernel extension](../apple-silicon/debugging-a-custom-kernel-extension.md)
  Configure your system to enable the debugging of custom kernel extensions from a second Mac.
- [Generating a Non-Maskable Interrupt](generating_a_non-maskable_interrupt.md)
  Interrupt the kernel on a target Mac and attach a remote debugger to it.
### IOKit Drivers
- [IOKit Fundamentals](iokit_fundamentals.md)
  Implement a driver for your custom hardware using a third-party kernel extension. 
- [Hardware Families](hardware_families.md)
  Add support for specific hardware protocols such as USB, and for standard network, serial, audio, and graphics interfaces. 
- [Driver Support](driver_support.md)
  Explore the device registry and access power-management utilities and other shared driver features. 
- [libkern](libkern.md)
  Access the runtime support and base classes of the kernel library.
### BSD
- [architecture](architecture.md)
  Access machine-level and architectural information about the current platform.
- [bsm](bsm.md)
  Audit resource usage on the system.
- [hfs](hfs.md)
  Access HFS file-system data structures. 
- [kern](kern.md)
  Access kernel-level interfaces including clock, task, kernel extension, lock, and compression utilities.  
- [Math](math.md)
  Perform mathematical operations and manipulate integer, float, and double values.  
- [miscfs](miscfs.md)
  Access device nodes and other file-system entities.
- [net](net.md)
  Access network-related utilities.
- [Strings](strings.md)
  Compare, convert, and catenate strings and access the resulting content of those strings.
- [sys](sys.md)
  Access general system utilities for time, file systems, and system information.
- [vfs](vfs.md)
  Access the virtual file-system interfaces.
- [vm](vm.md)
  Interact with the virtual memory system.
### Mach
- [mach](mach.md)
  Access Mach interfaces including processor, memory, thread, and semaphore support. 
- [mach-o](mach-o.md)
  Access interfaces associated with the Mach-O runtime.
### Utilities
- [Debugging](debugging.md)
  Debug your kernel extensions using the kernel debugger, assertions, exceptions, backtraces, and logging.
- [AppleDSP](appledsp.md)
  Perform digital signal processing on data.
### Deprecated
- [Deprecated Symbols](deprecated_symbols.md)
  Review unsupported symbols and their replacements.
### Additional Reference
- [Kernel Functions](kernel_functions.md)
- [Kernel Structures](kernel_structures.md)
- [Kernel Data Types](kernel_data_types.md)
- [Kernel Enumerations](kernel_enumerations.md)
- [Kernel Constants](kernel_constants.md)
### Classes
- [IOCatalogue](iocatalogue.md)
  In-kernel database for IOKit driver personalities.
- [IOEventLink](ioeventlink.md)
- [IOEventLinkInterface](ioeventlinkinterface.md)
- [IOGuardPageMemoryDescriptor](ioguardpagememorydescriptor.md)
- [IOHIDTranslationService](iohidtranslationservice.md)
- [IOServiceStateNotificationDispatchSource](../driverkit/ioservicestatenotificationdispatchsource.md)
- [IOServiceStateNotificationDispatchSourceInterface](ioservicestatenotificationdispatchsourceinterface.md)
- [IOWorkGroup](ioworkgroup.md)
- [IOWorkGroupInterface](ioworkgroupinterface.md)
- [OSAction_IOHIDEventService__CopyEvent](osaction_iohideventservice_copyevent.md)
- [OSAction_IOHIDEventService__CopyEventInterface](osaction_iohideventservice_copyeventinterface.md)
- [OSAction_IOHIDEventService__SetLED](osaction_iohideventservice_setled.md)
- [OSAction_IOHIDEventService__SetLEDInterface](osaction_iohideventservice_setledinterface.md)
- [OSAction_IOHIDEventService__SetUserProperties](osaction_iohideventservice_setuserproperties.md)
- [OSAction_IOHIDEventService__SetUserPropertiesInterface](osaction_iohideventservice_setuserpropertiesinterface.md)

## See Also

- [IOKit Fundamentals](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP0000011)
- [About This Document](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/About/About.html#//apple_ref/doc/uid/TP30000905-CH204)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel)*