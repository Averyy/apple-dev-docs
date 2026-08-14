# About the Rosetta translation environment

**Framework**: Apple silicon

Learn how Rosetta translates executables, and understand what Rosetta can’t translate.

#### Overview

> ❗ **Important**: Rosetta was designed to make the transition to Apple silicon easier, and will be available through macOS 27 — as a general-purpose tool for Intel apps to help developers complete the migration of their apps. Beyond this timeframe, we will keep a subset of Rosetta functionality aimed at supporting older unmaintained gaming titles, that rely on Intel-based frameworks. macOS 27 directly integrates support for Intel binary translation, without needing to install Rosetta. This enables support for Intel Linux binaries running in ARM virtual machines (VMs) as well as Intel Linux containers. For more on information on Intel machine code translation and Linux VMs, see [`Running Intel Binaries in Linux VMs`](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms).

Rosetta is a translation process that allows users to run Mac apps that contain x86_64 instructions on Apple silicon. Rosetta was designed to ease the transition for Mac apps to Apple silicon, giving you time to transition your app to a native Apple silicon binary.

To someone using a Mac, Rosetta is mostly transparent. If a macOS binary contains only Intel instructions, macOS automatically launches Rosetta and begins the translation process. When translation finishes, the system launches the translated executable in place of the original. However, the translation process takes time, so a person might perceive that translated apps launch or run more slowly at times.

The system prefers to execute a Mac app’s `arm64` instructions on Apple silicon. If a binary includes both `arm64` and `x86_64` instructions, a person can tell the system to launch the app using Rosetta translation from the app’s Get Info window in the Finder. For example, someone might enable Rosetta translation to allow the app to run older plug-ins that don’t yet support the `arm64` architecture

![A screen that highlights the Open using Rosetta option in the Get Info window for Mail.](/images/com.apple.Apple-Silicon/about-the-rosetta-translation-environment-1@2x.png)

> ❗ **Important**: The system prevents you from mixing `arm64` code and `x86_64` code in the same process. Rosetta translation applies to an entire process, including all code modules that the process loads dynamically. For information on how to determine when your app is running under Rosetta translation, see [`Determine whether your app is running as a translated binary`](about-the-rosetta-translation-environment#Determine-whether-your-app-is-running-as-a-translated-binary.md).

##### Learn What Rosetta Cant Translate

Rosetta can translate most Intel-based apps, including apps that contain just-in-time (JIT) compilers. However, Rosetta doesn’t translate the following executables:

- Kernel extensions
- Virtual Machine apps that virtualize x86_64 computer platforms

Rosetta translates all `x86_64` instructions, including ones from the AVX and AVX2  instruction set, but it doesn’t support the execution of AVX512 vector instructions. If you include these unsupported instructions in your code, run them only after verifying that they’re available. For example, to determine if AVX512 vector instructions are available, use the [`sysctlbyname`](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname) function to check the `hw.optional.avx512f` attribute.

##### Determine Whether Your App Is Running As a Translated Binary

On Apple silicon, a universal binary may run either natively or as a translated binary. The system runs the native version whenever possible, but the user might opt to run the code using Rosetta to support older plug-ins.

To programmatically determine when a process is running under Rosetta translation, call the [`sysctlbyname`](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname) function with the `sysctl.proc_translated` flag, as shown in the following example.

The example function returns the value `0` for a native process, `1` for a translated process, and `-1` when an error occurs.

```occ
int processIsTranslated() {
   int ret = 0;
   size_t size = sizeof(ret);
   if (sysctlbyname("sysctl.proc_translated", &ret, &size, NULL, 0) == -1) 
   {
      if (errno == ENOENT)
         return 0;
      return -1;
   }
   return ret;
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)*