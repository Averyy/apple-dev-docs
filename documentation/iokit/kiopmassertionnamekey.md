# kIOPMAssertionNameKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

The CFDictionary key for assertion name. Setting this key is required when you're creating an assertion.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPMAssertionNameKey
```

## Discussion

`kIOPMAssertionNameKey` describes the the activity the assertion is protecting. The creator should specify a CFString value for this key in the dictionary passed to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md)

The assertion name is separate from the assertion type's behavior - specify a CFString like "Checking mail" or "Compiling" that describes the task that this assertion protects.

The CFString you associate with this key does not have to be localizable (macOS will not attempt to localize it.)

Describe your assertion as thoroughly as possible. See these other keys that can you can also set to add explanation to an assertion: OPTIONAL [`kIOPMAssertionDetailsKey`](./kiopmassertiondetailskey.md) OPTIONAL [`kIOPMAssertionHumanReadableReasonKey`](./kiopmassertionhumanreadablereasonkey.md) OPTIONAL [`kIOPMAssertionLocalizationBundlePathKey`](./kiopmassertionlocalizationbundlepathkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertionnamekey)*