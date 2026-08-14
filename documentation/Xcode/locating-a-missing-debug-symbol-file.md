# Locating a missing debug symbol file

**Framework**: Xcode

Find the debug symbol file (`.dSYM`) required to decode the hexadecimal address from a crash report.

#### Overview

When your crash report includes a hexadecimal address from a binary you created or a third-party binary, you need to find its companion `.dSYM` file to *symbolicate* that address. *Symbolication* is the process of replacing memory addresses in a crash log with human-readable function names and line numbers. A `.dSYM` file is a macOS bundle that contains debug symbols for a binary. The build UUID links the two files. A binary and its `.dSYM` file are compatible only when their build UUIDs match. For more information, see [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md) and [`Adding identifiable symbol names to a crash report`](adding-identifiable-symbol-names-to-a-crash-report.md).

##### Locate the Build Uuid of the Binary

The following backtrace highlights a hexadecimal address at line frame 3 from a binary named `TouchCanvas`:

![A screenshot that highlights a hexadecimal address at line frame 3 in a crash report.](/images/com.apple.Xcode/locating-a-missing-debug-symbol-01@2x.png)

To find the build UUID of the binary, look for a binary with that name in the list of binary images at the bottom of the crash report. This list contains the build UUID of each binary represented in the crash report. Record the binary’s build UUID from the fourth column. For more information, see [`Binary images`](examining-the-fields-in-a-crash-report#Binary-images.md).

After you record the build UUID from the binary images section, convert it to a 36-character uppercase hexadecimal string in the format `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`. The following binary images section shows a build UUID of `e3ea8743c9e63c68bf048d51363b689d` for `TouchCanvas`, which becomes `E3EA8743-C9E6-3C68-BF04-8D51363B689D` after conversion:

![A screenshot that highlights the name and UUID of a binary in a crash report.](/images/com.apple.Xcode/locating-a-missing-debug-symbol-02@2x.png)

Alternatively, you can use Xcode to find the build UUID of the binary. When you open a crash report in Xcode, the Debug navigator appears. Control-click the process or any thread in the navigator, then choose Show Library Info from the contextual menu. Xcode lists the name, UUID, load address, and path of every binary represented in the crash report. The following Debug navigator shows a build UUID of `E3EA8743-C9E6-3C68-BF04-8D51363B689D` for `TouchCanvas`:

![A screenshot that shows the Debug navigator on the left containing a crash report and a contextual menu opened on the right displaying a list of binary images.](/images/com.apple.Xcode/locating-a-missing-debug-symbol-03@2x.png)

##### Locate the Corresponding Dsym File

After you find the binary’s build UUID, use it to locate the corresponding `.dSYM` file. In Terminal, run the following `mdfind` command, including the quotation marks around the query:

```shell
% mdfind "com_apple_xcode_dsym_uuids == <UUID>"
```

If Spotlight finds a matching `.dSYM`, `mdfind` prints the path to the file. For example, the following command returns the path to a `.dSYM` named `TouchCanvas.app.dSYM`:

```shell
% mdfind "com_apple_xcode_dsym_uuids == E3EA8743-C9E6-3C68-BF04-8D51363B689D"
/Users/.../TouchCanvas.app.dSYM
```

If Spotlight fails to find a matching `.dSYM`, `mdfind` prints nothing. Check the following:

- In System Settings, confirm that Spotlight indexing is enabled for the directory containing the `.dSYM` files.
- Confirm that the path to that directory doesn’t include `.noindex`.
- Confirm that your build produces debugging information. For more information, see [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md).

After you complete these checks, retry the `mdfind` command. If the command still fails and the binary is from a third-party framework or package, contact its developers for the `.dSYM` file.

If you use Xcode to archive your app, take the following additional steps:

- Verify that you still have the Xcode archive for the version of your app that crashed. If you no longer have the archive, you can’t symbolicate the hexadecimal address for that version. To avoid this in the future, release a new version of your app and retain its Xcode archive, so you can symbolicate crash reports for the new version.
- Add the Xcode archive to a location where Spotlight can find it, such as your home directory.

##### Determine the Build Uuid of the Dsym File

After you locate the `.dSYM` file, use `dwarfdump` to retrieve its build UUID. In Terminal, run `dwarfdump` with the `--uuid` option and the path to the `.dSYM` file:

```shell
% dwarfdump --uuid <path-to-dSYM>
```

The following command returns `E3EA8743-C9E6-3C68-BF04-8D51363B689D` as the build UUID of `TouchCanvas.app.dSYM`:

```shell
% dwarfdump --uuid /Users/.../TouchCanvas.app.dSYM
UUID: E3EA8743-C9E6-3C68-BF04-8D51363B689D (arm64) /Users/.../TouchCanvas.app.dSYM/Contents/Resources/DWARF/TouchCanvas
```

##### Confirm the Build Uuids Match

Verify that the `.dSYM` file’s build UUID matches the binary’s build UUID. If the build UUIDs match, you can symbolicate the hexadecimal address in Xcode or from the command line. For more information, see [`Adding identifiable symbol names to a crash report`](adding-identifiable-symbol-names-to-a-crash-report.md).

## See Also

- [Resetting access to protected resources in macOS](resetting-access-to-protected-resources-in-macos.md)
  Use Terminal to remove your app’s authorization access to protected resources during testing.
- [Acquiring operating system symbol information](acquiring-operating-system-symbol-information.md)
  Download symbols for Apple system frameworks using Xcode or Terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/locating-a-missing-debug-symbol-file)*