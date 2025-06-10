# About the Rosetta translation environment

**Framework**: Apple silicon

Learn how Rosetta translates executables, and understand what Rosetta can’t translate.

#### Overview

> ❗ **Important**: macOS Tahoe will be the last release for Intel-based Mac computers. Those systems will continue to receive security updates for 3 years. Rosetta was designed to make the transition to Apple silicon easier, and we plan to make it available for the next two major macOS releases – through macOS 27 – as a general-purpose tool for Intel apps to help developers complete the migration of their apps. Beyond this timeframe, we will keep a subset of Rosetta functionality aimed at supporting older unmaintained gaming titles, that rely on Intel-based frameworks.

Rosetta is a translation process that allows users to run apps that contain `x86_64` instructions on Apple silicon. Rosetta is meant to ease the transition to Apple silicon, giving you time to create a universal binary for your app. It is not a substitute for creating a native version of your app.

To the user, Rosetta is mostly transparent. If an executable contains only Intel instructions, macOS automatically launches Rosetta and begins the translation process. When translation finishes, the system launches the translated executable in place of the original. However, the translation process takes time, so users might perceive that translated apps launch or run more slowly at times.

The system prefers to execute an app’s `arm64` instructions on Apple silicon. If a binary includes both `arm64` and `x86_64` instructions, the user can tell the system to launch the app using Rosetta translation from the app’s Get Info window in the Finder. For example, a user might enable Rosetta translation to allow the app to run older plug-ins that don’t yet support the `arm64` architecture.

![A screen that highlights the Open using Rosetta option in the Get Info window for Mail.](https://docs-assets.developer.apple.com/published/3a4da06dd5005d3387eb9526c398f49f/about-the-rosetta-translation-environment-1%402x.png)

> ❗ **Important**: The system prevents you from mixing `arm64` code and `x86_64` code in the same process. Rosetta translation applies to an entire process, including all code modules that the process loads dynamically.

For information on how to determine when your app is running under Rosetta translation, see [`Determine Whether Your App Is Running as a Translated Binary`](about-the-rosetta-translation-environment#Determine-Whether-Your-App-Is-Running-as-a-Translated-Binary.md)..

##### What Cant Be Translated

Rosetta can translate most Intel-based apps, including apps that contain just-in-time (JIT) compilers. However, Rosetta doesn’t translate the following executables:

- Kernel extensions
- Virtual Machine apps that virtualize x86_64 computer platforms

Rosetta translates all `x86_64` instructions, but it doesn’t support the execution of some newer instruction sets and processor features, such as AVX, AVX2, and AVX512 vector instructions. If you include these newer instructions in your code, execute them only after verifying that they are available. For example, to determine if AVX512 vector instructions are available, use the [`sysctlbyname`](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname) function to check the `hw.optional.avx512f` attribute.

##### Determine Whether Your App Is Running As a Translated Binary

On Apple silicon, a universal binary may run either natively or as a translated binary. The system runs the native version whenever possible, but the user might opt to run the code using Rosetta to support older plug-ins.

To programmatically determine when a process is running under Rosetta translation, call the [`sysctlbyname`](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname) function with the `sysctl.proc_translated` flag, as shown in the following example. The example function returns the value `0` for a native process, `1` for a translated process, and `-1` when an error occurs.

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