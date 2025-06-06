# Interpreting the JSON format of a crash report

**Framework**: Xcode

Understand the structure and properties of the objects the system includes in the JSON of a crash report.

#### Overview

Starting with iOS 15 and macOS 12, apps that generate crash reports store the data as JSON in files with an `.ips` extension. Tools for viewing these files, such as Console, translate the JSON to make it easier to read and interpret. The translated content uses field names the article [`Examining the fields in a crash report`](examining-the-fields-in-a-crash-report.md) describes. Use the following information to understand the structure of the JSON the system uses for these crash reports and how the data maps to the field names found in the translated content.

Typical JSON parsers expect a single JSON object in the body of the file. The IPS file for a crash report contains two JSON objects: an object containing IPS metadata about the report incident and an object containing the crash report data. When parsing the file, extract the JSON for the metadata object from the first line. If the `bug_type` property of the metadata object is `309`, the log type for crash reports, you can extract the JSON for the crash report data from the remainder of the text.

The following example reads the contents of a crash report into a dictionary:

```swift
    do {
        let content = try String(contentsOfFile: filePath, encoding: String.Encoding.utf8)

        /// Read the first line, the metadata object, into a dictionary.
        let metadataRange = content.lineRange(for: ..<content.startIndex)
        let metadataJSON = content[metadataRange].data(using: .utf8)
        let metadata = try JSONSerialization.jsonObject(with: metadataJSON!) as! Dictionary<String, Any>

        /// Check the `bug_type` property of the metadata for type `309`, the log type for crash reports.
        let logType = "\(metadata["bug_type"] ?? "(unknown)")"
        guard logType == "309" else {
            // Handle the error.        
            fatalError("Log type \(logType) is not a crash report.")
        }

        /// Read the remainder of the file, the crash report object, into a dictionary.
        let reportRange = content.lineRange(for: metadataRange.upperBound..<content.endIndex)
        let reportJSON = content[reportRange].data(using: .utf8)
        let report = try JSONSerialization.jsonObject(with: reportJSON!) as! Dictionary<String, Any>

        return report
    } catch {
        // Handle the error.
        fatalError("*** An error occurred while reading the crash report: \(error.localizedDescription) ***")
    }
```

The crash report data is made up of additional objects pertaining to OS version, bundle, store, exception, termination, threads, frames, and binary images. The properties of all these objects are outlined below.

##### Ips Metadata

The IPS metadata object contains the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `name` | String | The name of the process the report applies to. Usually the process executable name. |
| `bug_type` | String | The identifier for the type of log captured by the report. Type `309` for the crash reports this article describes. You might encounter other types. Type `288`, for instance, is a stackshot. |
| `bundleID` | String | The bundle identifier of the process the report applies to; see [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier). |
| `build_version` | String | The bundle version string of the process the report applies to; see [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion). |
| `incident_id` | String | A unique identifier for the report. Two reports never share the same identifier. |
| `platform` | Number | A number identifying the platform the process was running on. For the meaning of these values, see [`Platforms`](interpreting-the-json-format-of-a-crash-report#Platforms.md). |
| `timestamp` | String | A date and time the log system generates for report tracking. Use the `procLaunch` and `captureTime` properties from the crash report object to determine launch and termination time for the process. |

##### Crash Report

The crash report object can contain the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `asi` | Dictionary | Additional application-specific logging. The properties of this object include an array of log strings. For more information, see [`Diagnostic messages`](examining-the-fields-in-a-crash-report#Diagnostic-messages.md). This appears in a translated report under Application Specific Information. |
| `bundleInfo` | Dictionary | Bundle information for the process that crashed. For a description of this object‘s properties, see [`Bundle info`](interpreting-the-json-format-of-a-crash-report#Bundle-info.md). |
| `captureTime` | String | The date and time of the crash. This appears in a translated report under Date/Time. |
| `coalitionID` | String | The ID of the coalition containing the process. Process coalitions track resource usage among groups of related processes, such as an operating system process supporting a specific API’s functionality in an app. Most processes, including app extensions, form their own coalition. This appears in a translated report under Coalition. |
| `coalitionName` | String | The name of the coalition containing the process. For more details, see the description above on `coalitionID`. |
| `cpuType` | String | The CPU architecture of the process that crashed. The value is one of ARM-64, ARM, X86-64, or X86. This appears in a translated report under Code Type. |
| `crashReporterKey` | String | An anonymized per-device identifier. Two reports from the same device contain identical values. This identifier is reset upon erasing the device. This appears in a translated report under CrashReporter Key. |
| `DTAppStoreToolsBuild` | String | The version of Xcode used to compile your app’s bitcode and to thin your app to device-specific variants. This appears in a translated report under AppStoreTools. |
| `exception` | Dictionary | Information about how the process terminated. For a description of this object‘s properties, see [`Exception`](interpreting-the-json-format-of-a-crash-report#Exception.md). |
| `faultingThread` | Number | The index of the thread that crashed. The object at this index in the `threads` array contains information about this thread, such as the state of its registers. For a description of this object‘s properties, see [`Threads`](interpreting-the-json-format-of-a-crash-report#Threads.md). |
| `incident` | String | A unique identifier for the report. Two reports never share the same identifier. This appears in a translated report under Incident Identifier. |
| `isCorpse` | Boolean | A Boolean with a `true` value if the crash didn’t originate from a hardware trap, either because the process was explicitly terminated by the operating system or the process called `abort()`. This appears in a translated report under Exception Note as EXC_CORPSE_NOTIFY. |
| `isNonFatal` | String | A Boolean with a `true` value if the process didn’t terminate, because the issue that created the crash report wasn’t fatal. This appears in a translated report under Exception Note as NON-FATAL CONDITION (this  a crash). |
| `isSimulated` | String | A Boolean with a `true` value if the process didn’t crash, but the operating system might have subsequently requested termination of the process. This appears in a translated report under Exception Note as SIMULATED (this  a crash). |
| `lastExceptionBacktrace` | String | Backtrace information for the crashed process documenting the code running on the thread where a language exception occurs. For a description of this object‘s properties, see [`Threads`](interpreting-the-json-format-of-a-crash-report#Threads.md). This appears in a translated report under Last Exception Backtrace. |
| `modelCode` | String | The specific device model the process was running on. This appears in a translated report under Hardware Model. |
| `osVersion` | Dictionary | Version information for the OS the process was running under. For a description of this object‘s properties, see [`OS version`](interpreting-the-json-format-of-a-crash-report#OS-version.md). This appears in a translated report under OS Version. |
| `parentPid` | Number | The identifier of the process that launched the crashed process. This appears in a translated report under Parent Process in square brackets after the process name. |
| `parentProc` | String | The name of the process that launched the crashed process. This appears in a translated report under Parent Process. |
| `pid` | Number | The identifier of the process that crashed. This appears in a translated report under Process as the text before the parenthesis. |
| `procLaunch` | String | The date and time the process launched. This appears in a translated report under Launch Time. |
| `procName` | String | The executable name of the process that crashed. This appears in a translated report under Process as the text before the parenthesis. |
| `procPath` | String | The location of the executable on disk. macOS replaces user-identifable path components with placeholder values to protect privacy. This appears in a translated report under Path. |
| `procRole` | String | The task role assigned to the process at the time of termination; see [`task_role_t`](https://developer.apple.com/documentation/kernel/task_role_t). This appears in a translated report under Role. |
| `storeInfo` | Dictionary | Store information about the process that crashed. For a description of this object‘s properties, see [`Store info`](interpreting-the-json-format-of-a-crash-report#Store-info.md). |
| `termination` | Dictionary | Information about the termination of a process by another. For a description of this object‘s properties, see [`Termination`](interpreting-the-json-format-of-a-crash-report#Termination.md). |
| `threads` | Dictionary | Backtrace information for the crashed process documenting the code running on each thread when the process terminated. For a description of this object‘s properties, see [`Threads`](interpreting-the-json-format-of-a-crash-report#Threads.md). The backtrace for each thread appears in its own section. |
| `translated` | Boolean | A Boolean with a `true` value for a process with X86-64 instructions running translated under Rosetta on Apple silicon. |
| `uptime` | Number | The time, in seconds, the system has been running since it booted. This appears in a translated report under Time Awake Since Boot. |
| `usedImages` | Array | Each dictionary entry in this array contains information about a binary image loaded in the process at the time of termination, such as the app executable and system frameworks. For a description of this object’s properties, see [`Binary images`](interpreting-the-json-format-of-a-crash-report#Binary-images.md). This appears in a translated report under Binary Images. |
| `version` | Number | Crash report schema version. |
| `vmSummary` | String | Summary of the virtual memory in use by the process. Similar to the output from executing `vmmap <pid> --summary`. This appears in a translated report under VM Region Summary. |
| `vmregioninfo` | String | Information about the virtual memory regions for terminations due to a memory access issue. This appears in a translated report under VM Region Info. |

##### Platforms

The numeric values for `platform` include:

- `1` for macOS
- `2` for iOS (includes iOS apps running under macOS on Apple silicon)
- `3` for tvOS
- `4` for watchOS
- `6` for Mac Catalyst
- `7` for iOS Simulator
- `8` for tvOS Simulator
- `9` for watchOS Simulator

##### Os Version

A report includes OS version information in an object that can contain the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `build` | String | The build number of the operating system. Appears in a translated report inside the parentheses under OS Version. |
| `isEmbedded` | Boolean | A Boolean with a `true` value if the operating system is for an embedded platform. |
| `releaseType` | String | The type of release: `User` for a release version and `Beta` for a prerelease versions. Appears in a translated report under Release Type. |
| `train` | String | A string containing the platform and OS version number. Appears in a translated report under OS Version. |

##### Bundle Info

A report includes bundle information in an object with the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `CFBundleIdentifier` | String | The bundle identifier for the process that crashed. Appears in a translated report under Identifier. |
| `CFBundleShortVersionString` | String | The bundle version string (short) for the process that crashed; see [`CFBundleShortVersionString`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString). Appears in a translated report under Version. |
| `CFBundleVersion` | String | The bundle version for the process that crashed; see [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion). Appears in a translated report under Version. |

##### Store Info

A report includes store information in an object with the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `applicationVariant` | String | The specific variant of your app produced by app thinning. Appears in a translated report under App Variant. |
| `deviceIdentifierForVendor` | String | A unique identifier for the combination of the device and vendor of the crashed app. Two reports for apps from the same vendor and from the same device contain identical values. This field is only present for TestFlight builds of an app, and replaces the CrashReporter Key field. Appears in a translated report under Beta Identifier. |
| `itemID` | String | The Apple identifier, a unique record for titles in the store. |

##### Exception

A report includes exception information in an object with the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `codes` | String | Processor-specific information about the exception encoded into one or more 64-bit hexadecimal numbers. This appears in a translated report under Exception Codes. |
| `message` | String | Additional human-readable information extracted from the exception codes. This appears in a translated report under Exception Message. |
| `signal` | String | The BSD termination signal; see [`Understanding the exception types in a crash report`](understanding-the-exception-types-in-a-crash-report.md). This appears in a translated report under Exception Type as the text inside the parentheses. |
| `subtype` | String | The human-readable description of the exception codes. This appears in a translated report under Exception Subtype. |
| `type` | String | The name of the Mach exception that terminated the process; see [`Understanding the exception types in a crash report`](understanding-the-exception-types-in-a-crash-report.md). This appears in a translated report under Exception Type as the text before the parenthesis. |

For more information, see [`Exception information`](examining-the-fields-in-a-crash-report#Exception-information.md).

> **Note**: This exception information doesn’t refer to language exceptions thrown by an API or language features in Objective-C or C++. Crash reports record language exception information separately.

##### Termination

A report includes termination information in an object that can contain the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `byPid` | Number | The identifier of the terminating process.  This appears in a translated report under Terminating Process as the number in brackets after the terminating process name. |
| `byProc` | String | The name of the terminating process.  This appears in a translated report under Terminating Process before the PID in brackets. |
| `code` | Number | A code the system uses to identify the reason for termination or a BSD termination signal the system used. For a list of possible reason codes, see [`Understanding the exception types in a crash report`](understanding-the-exception-types-in-a-crash-report.md). This appears in a translated report under Termination Reason. |
| `flags` | Number | Options set by the terminating process for how the process should terminate; see [`reason_flags`](https://developer.apple.comhttps://opensource.apple.com/source/xnu/xnu-3789.21.4/bsd/sys/reason.h.auto.html). |
| `indicator` | String | Human-readable description of the termination code, if available. This appears in a translated report under Termination Reason. |
| `namespace` | String | A namespace the system uses to categorize the reason for termination; see [`reason_flags`](https://developer.apple.comhttps://opensource.apple.com/source/xnu/xnu-3789.21.4/bsd/sys/reason.h.auto.html). This appears in a translated report under Termination Reason. |

For details on how to use this information, see [`Exception information`](examining-the-fields-in-a-crash-report#Exception-information.md).

JSON stores numeric values as decimal numbers. The value the system stores in the `code` property is intended to be viewed in its hexadecimal form; see [`Convert numeric values to hexadecimal numbers`](interpreting-the-json-format-of-a-crash-report#Convert-numeric-values-to-hexadecimal-numbers.md).

##### Threads

A report includes thread information in objects that can contain the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `frames` | Array | An array of dictionaries describing each frame of the thread’s backtrace. Stack frames are in calling order, where frame 0 is the function that was executing at the time execution halted. Frame 1 is the function that called the function in frame 0, and so on. For a description of this object‘s properties, see [`Frames`](interpreting-the-json-format-of-a-crash-report#Frames.md). |
| `id` | Number | The thread’s index number. |
| `queue` | String | A string that identifies the dispatch queue of the crashing thread, if applicable. This appears in a translated report in the label above the backtrace of each thread under Dispatch Queue. |
| `threadState` | Dictionary | A JSON representation of the CPU registers and their values for the thread as well as other useful runtime data from when the process terminated. The structure and properties of this object depend on the `flavor`. This appears in its own section of the formatted report after the backtraces for all the threads. |
| `triggered` | Boolean | A Boolean with a `true` value if this thread is responsible for the crash. This appears in a translated report as Triggered by Thread. |

For details on how to use this information, see [`Backtraces`](examining-the-fields-in-a-crash-report#Backtraces.md) and [`Thread state`](examining-the-fields-in-a-crash-report#Thread-state.md).

JSON contains numbers for memory addresses in frame and thread state objects as decimal digits. To view the numbers contained in these fields in their more common hexadecimal form, see [`Convert numeric values to hexadecimal numbers`](interpreting-the-json-format-of-a-crash-report#Convert-numeric-values-to-hexadecimal-numbers.md).

##### Frames

A report includes information about frames in objects with the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `imageIndex` | Number | The index of the binary image containing the code this frame in the backtrace is executing. The object at this index in the `usedImages` array contains information about this image. For a description of this object‘s properties, see [`Binary images`](interpreting-the-json-format-of-a-crash-report#Binary-images.md). |
| `imageOffset` | Number | The byte offset from the start of the binary image to the current instruction. If you add this value to the `base` value from the binary images list, you’ll get the runtime memory address of the instruction that’s executing. For frame 0 in each backtrace, this is the address of the machine instruction executing on a thread when the process terminated. For other stack frames, this is the address of the first machine instruction that executes after control returns to that stack frame. This runtime memory address is the value that appears next to each frame in the backtraces of the formatted report. |
| `symbol` | String | In a fully symbolicated crash report, the name of the function that is executing. |
| `symbolLocation` | Number | The number of bytes from the executing instruction’s entry point. This is the value that appears after the ‘+’ next to each frame in the backtraces of the formatted report. |

For details on how to use this information, see [`Backtraces`](examining-the-fields-in-a-crash-report#Backtraces.md).

JSON contains numbers for the memory locations and offsets as decimal digits. To convert the numbers contained in these fields to their more common hexadecimal form, see [`Convert numeric values to hexadecimal numbers`](interpreting-the-json-format-of-a-crash-report#Convert-numeric-values-to-hexadecimal-numbers.md).

##### Binary Images

A report includes information about binary images loaded in the process at the time of termination in objects with the following properties:

| Key | Type | Description |
| --- | --- | --- |
| `arch` | String | The CPU architecture from the binary image that the operating system loaded into the process. |
| `base` | Number | The binary image’s load address. This is the start of the memory address range for the loaded image that appears in a translated report. |
| `name` | String | The binary name. |
| `path` | String | The path to the binary on disk. macOS replaces user-identifable path components with placeholder values to protect privacy. |
| `size` | Number | The size of the image. If you add this value to the `base` value, you’ll get the end of the memory address range for the loaded image that appears in a translated report. |
| `source` | String | A character that indicates the binary image’s region type: `P` (process), `S` (shared cache), `C` (shared cache library), `K` (kernel), `U` (kernel cache),  `T` (kernel text exec), `A` (absolute). |
| `uuid` | String | A build UUID that uniquely identifies the binary image you can use to locate the corresponding `dSYM` file when symbolicating the crash report. For more information, see [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md). |

For details on how to use this information, see [`Binary images`](examining-the-fields-in-a-crash-report#Binary-images.md).

##### Convert Numeric Values to Hexadecimal Numbers

JSON stores numeric values as decimal numbers. Many of these numeric values, such as error codes and memory addresses, appear in a translated report as hexadecimal numbers to make them easier to interpret.

You can use the following to print a hexadecimal representation of the numbers from the decimal representation found in the JSON.

```swift
import Foundation

let decimal = 2343432205

print(String(format: "0x%lx", decimal))
// Prints "0x8badf00d".
```

## See Also

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md)
  Replace hexadecimal addresses in a crash report with function names and line numbers that correspond to your app’s code.
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)
  Find patterns in crash reports that identify common problems, and investigate the issue based on the pattern.
- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md)
  Understand the structure of a crash report and the information each field contains.
- [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)
  Learn what the exception type tells you about why your app crashed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/interpreting-the-json-format-of-a-crash-report)*