# gestaltSystemVersion

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
gestaltSystemVersion = 'sysv'
```

#### Discussion

Indicates the version number of the operating system, with limitations on the values returned.

> ❗ **Important**: Never infer the availability of hardware or software features from the value that the `Gestalt` function returns when you pass it the [`gestaltSystemVersion`](./gestaltsystemversion.md) selector.
>
> In macOS 10.4 and later, the recommended way to get operating system version information is to use the `gestaltSystemVersionMajor`, `gestaltSystemVersionMinor`, and `gestaltSystemVersionBugFix` selectors, listed below, in concert. These selectors do not have arbitrary limits on the values returned.

If the values of the minor or bug fix revision are larger than 9, then `gestaltSystemVersion` will substitute the value 9 for them.  For example, when running OS X v10.3.15, this selector returns `0x1039`. When running OS X v10.10.5, this selector returns `0x1095`.

 For macOS, the version representations are as shown in [Table 1](./gestaltsystemversion.md#1966941).

| macOS version | Representation |
| --- | --- |
| 10.0 | 0x1000 |
| 10.1 | 0x1010 |
| 10.2 | 0x1020 |
| 10.3 | 0x1030 |
| 10.4 | 0x1040 |

For systems prior to macOS, the version is represented as four hexadecimal digits in the low-order word of the return value. For example, if your application is running in version 7.0.1, then `Gestalt` returns the value 0x0701. Ignore the high-order word of the returned value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1470788-system_version_selectors/gestaltsystemversion)*