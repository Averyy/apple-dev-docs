# Acquiring operating system symbol information

**Framework**: Xcode

Download symbols for Apple system frameworks using Xcode or Terminal.

#### Overview

To make symbols from the operating system frameworks identifiable in a crash report, you need to collect them from a device using Xcode, or by using the command line in Terminal. These symbols are specific to the operating system release, and the model and the CPU architecture of the device. For example, the symbols for an iPhone running iOS 26 aren’t the same as the symbols for the same iPhone running iOS 26.2.

After you collect the symbols, the system saves them in `~/Library/Developer/Xcode/<iOS|watchOS|tvOS|visionOS> DeviceSupport`.

#### Collect System Framework Symbols From a Device

For iOS, iPadOS, tvOS, visionOS, and watchOS apps, Xcode automatically copies operating system binaries that contain symbols from each device you connect to your Mac.

> **Note**: For macOS and Mac Catalyst apps, symbolicate the crash log by using Xcode on a version of macOS that matches the macOS version in the crash report.

Alternatively, you can acquire operating system symbols from an unlocked and attached device in Terminal with the `xcodebuild -prepareDeviceSupport` command. To fetch the system binaries that contain symbols from a device, add the `-destination` option to the command. The option takes the UDID, identifier, or name of the device as an argument.

```None
% xcodebuild -prepareDeviceSupport -destination "id=device-UDID" | "id=device-identifier" | "name=device-name"

```

For example, the following command collects the symbols using the UDID of the device. Enter `devicectl list devices` with the `--columns` option and the UDID in Terminal.

```None
% devicectl list devices --columns 'UDID'
```

The command prints the default data columns and the specified UDID column, as in the following example:

```None
% devicectl list devices --columns 'UDID'
Name          Hostname                      Identifier                  State                 UDID 
----   ---------------------   ------------------------------------   --------- ... -------------------------
Work   Work.coredevice.local   09C6E78B-1024-568C-869F-68A0B772907E   available     00008103-000D585C36D0801E

```

Next, run `xcodebuild -prepareDeviceSupport` with the `-destination` option set to the gathered UDID. If the system finds the device with the specified UDID, the command collects the symbols from the device and prints a message.

```None
% xcodebuild -prepareDeviceSupport -destination "id=00008103-000D585C36D0801E"
Starting Device Support Preparation
-----------------------------------
Searching for 60.0 seconds with ["id": "00008103-000D585C36D0801E"]
Located Work 00008103-000D585C36D0801E
[Work ] Copying ....30%..44%..47%..49%....100%
[Work] Extracting ...20%..30%...40%..50%....90%
[Work] Finished
```

#### Download System Framework Symbols for Watchos in Terminal

You can download operating system symbols specific to a watchOS release from the command line without pairing an Apple Watch to your Mac. Enter `xcodebuild -prepareDeviceSupport` with the `-platform`, `-osVersion`, and `-buildVersion` in Terminal.

```None
% xcodebuild -prepareDeviceSupport -platform watchOS -osVersion <version> -buildVersion <version>
```

> **Note**: To find the watchOS version and build version, choose Settings > General > About on your Apple Watch, and look for the watchOS Version field. The field displays the OS version followed by the build version in parentheses, such as 26.3 (23S618).

The following command downloads symbols for watchOS 26.3 (23S618):

```None
% xcodebuild -prepareDeviceSupport -platform watchOS -osVersion 26.3 -buildVersion 23S618
Starting Device Support Preparation
-----------------------------------
Platform: watchos
OSVersion: 26.3
BuildVersion: 23S618
ModelCode: 
Arch:
Downloading Symbols for watchOS 26.3 (23S618): Done.
Created '/Users/ravipatel/Library/Developer/Xcode/watchOS DeviceSupport/26.3 (23S618) universal/Symbols' caching completed successfully

```

In watchOS 11 and later, the command downloads universal symbols you can use to symbolicate crash reports from all models of Apple Watch. If you require symbols for an earlier version of watchOS, like watchOS 10.6, specify the model of Apple Watch to download them using the `-modelCode` option.

> **Note**: For information about finding the model code value, see `Hardware Model` in [`Examining the fields in a crash report`](examining-the-fields-in-a-crash-report.md).

The following command downloads symbols for an Apple Watch Ultra 2 with watchOS 10.6 (21U577):

```None
% xcodebuild -prepareDeviceSupport -platform watchOS -osVersion 10.6 -buildVersion 21U577 -modelCode "Watch7,5"
Starting Device Support Preparation
-----------------------------------
Platform: watchos
OSVersion: 10.6
BuildVersion: 21U577
ModelCode: Watch7,5
Arch:
Downloading Symbols for watchOS 10.6 (21U577): Done.
Created '/Users/ravipatel/Library/Developer/Xcode/watchOS DeviceSupport/10.6 (21U577) universal/Symbols' caching completed successfully

```

## See Also

- [Locating a missing debug symbol file](locating-a-missing-debug-symbol-file.md)
  Find the debug symbol file (`.dSYM`) required to decode the hexadecimal address from a crash report.
- [Resetting access to protected resources in macOS](resetting-access-to-protected-resources-in-macos.md)
  Use Terminal to remove your app’s authorization access to protected resources during testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/acquiring-operating-system-symbol-information)*