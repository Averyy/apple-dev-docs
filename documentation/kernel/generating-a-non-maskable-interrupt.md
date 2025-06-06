# Generating a Non-Maskable Interrupt

**Framework**: Kernel

Interrupt the kernel on a target Mac and attach a remote debugger to it.

#### Overview

Debugging many types of kernel-level problems requires a second Mac computer to run the debugger. On your target Mac, configure the `debug` boot arg with the options you need to support non-maskable interrupts (NMIs). The `DB_NMI` (`0x4`) flag causes the kernel on the target Mac to wait for a debuger to attach when an NMI occurs; add other flags as needed. After an NMI occurs, use the debugger on your second Mac to examine the system and diagnose any issues.

For information about how to configure your Mac to debug kernel processes, sign in and download the Kernel Debug Kit from [`https://developer.apple.com/download/more/`](https://developer.apple.comhttps://developer.apple.com/download/more/). 

##### 3624910

The following table lists the keys you press to trigger an NMI on different types of Mac. 

| Mac | Key presses |
| --- | --- |
| Apple silicon | Command (Left) + Command (Right) + Delete |
| Intel-based Mac (with Apple T2 Security Chip) | Command (Left) + Command (Right) + Delete |
| Intel-based Mac (without Apple T2 Security Chip) | Command (Left) + Command (Right) + Power Button |

For information about which Intel-based Mac computers have the Apple T2 Security Chip, see [`About the Apple T2 Security Chip`](https://developer.apple.comhttps://support.apple.com/en-us/HT208862).

##### 3624911

To trigger an NMI manually using only the target Mac’s power button, add the `DB_NMI_BTN_ENA` (`0x8000`) flag to the `debug` boot arg. Using only the power button makes it possible to trigger an NMI early in the Mac’s boot sequence. For example, you can trigger an NMI before the system loads the USB keyboard driver, or trigger one on systems with no keyboard at all. Combine this flag with the `DB_NMI` flag and set the boot args on your target Mac as shown in the following example:

```other
sudo nvram boot-args="<current settings> debug=0x8004"
```

When you set one or more debug flags, the target Mac retains the designated capabilities until you remove the flags using the `nvram` tool. To remove all boot args, run the `nvram` tool with the `-d` option, as shown in the following example:

```other
sudo nvram -d boot-args
```

> ❗ **Important**: Adding the `DB_NMI_BTN_ENA` flag prevents you from pressing your Mac’s power button to display the UI to shutdown, restart, or sleep the computer. Similarly, you cannot press the button to wake the computer while it’s asleep. You may still press and hold the button for eight to ten seconds to shut down the Mac. 

Adding the `DB_NMI_BTN_ENA` flag prevents you from pressing your Mac’s power button to display the UI to shutdown, restart, or sleep the computer. Similarly, you cannot press the button to wake the computer while it’s asleep. You may still press and hold the button for eight to ten seconds to shut down the Mac. 

## See Also

- [Implementing drivers, system extensions, and kexts](implementing_drivers_system_extensions_and_kexts.md)
  Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks. 
- [Installing a custom kernel extension](../apple-silicon/installing-a-custom-kernel-extension.md)
  Install kernel extensions using a custom installer package, and help users understand the installation process.
- [Debugging a custom kernel extension](../apple-silicon/debugging-a-custom-kernel-extension.md)
  Configure your system to enable the debugging of custom kernel extensions from a second Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/generating_a_non-maskable_interrupt)*