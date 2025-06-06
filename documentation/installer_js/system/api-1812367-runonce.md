# runOnce

**Framework**: Installer JS  
**Kind**: uid

Launches a given program in the `Resources` directory of the installation package, if it has not been run already.

## Declaration

```swift
run(programName, args...)
```

#### Return_value

After the program is executed, its exit code. If the program is not executed (see discussion), `undefined`.

#### Overview

On subsequent invocations with the same arguments, the program is not launched and the exit code of the first execution is returned.

The `allow-external-scripts` attribute of the `options` element in the distribution definition must be `'yes'` for the program to be launched. And, the Installer application asks the user’s permission before launching the program. See [`Distribution Definition XML Schema Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Introduction.html#//apple_ref/doc/uid/TP40005370) for more information.

Use this method instead of [`run`](system/1812364-run.md) when a program’s exit code using the same arguments is not expected to change.

## Parameters

- `programName`: Name of the program to execute.
- `args...`: Arguments passed to the program.

## See Also

- [run](system/1812364-run.md)
  Launches a given program in the `Resources` directory of the installation package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/system/1812367-runonce)*