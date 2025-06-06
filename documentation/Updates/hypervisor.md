# Hypervisor updates

**Framework**: Updates

Learn about important changes to Hypervisor.

#### Overview

Browse notable changes in [`Hypervisor`](https://developer.apple.com/documentation/Hypervisor).

#### June 2024

- Build your own virtual machine solutions with added support for nested virtualization in Apple silicon chips, and enable a hypervisor to run inside another virtual machine. Nested virtualization capabilities on a Mac with Apple silicon use a new exception level (EL), EL2, which the framework enables though several new methods, including [`hv_vm_config_set_el2_enabled(_:_:)`](https://developer.apple.com/documentation/hypervisor/4359587-hv_vm_config_set_el2_enabled), and a number of enumeration constants that describe ARM system registers.
- Add support for virtualized ARM Generic Interrupt Controller (GIC) devices and provide an efficient mechanism to manage interrupt delivery to a virtual machine. Providing a GIC device reduces the custom code you need to write to emulate an interrupt controller.
- Add support for GIC hypervisor control system registers that GIC devices provide for nested virtualization support. Support for these registers allows hypervisors running in a virtual machine to inject interrupts to their guests.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/hypervisor)*