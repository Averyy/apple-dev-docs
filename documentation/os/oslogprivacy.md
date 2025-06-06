# OSLogPrivacy

**Framework**: os  
**Kind**: struct

The privacy options that determine when to redact or display values in log messages.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct OSLogPrivacy
```

#### Overview

The [`OSLogPrivacy`](oslogprivacy.md) structure determines the visibility of interpolated values in log messages. Because people have access to log messages that your app generates, use the privacy options to hide potentially sensitive information. For example, you might use it to hide account information or personal data.

Use the available properties and methods to fetch an appropriately configured version of this structure, and pass it with your interpolated value in the log message. The following example shows how to mark a variable that contains the user’s bank account information as private:

```swift
Logger().info("User bank account number: \(accountNumber, privacy: .private)")
```

When you want to replace the generic redaction string with a hashed version of the original value, specify privacy options using the [`auto(mask:)`](oslogprivacy/auto(mask:).md), [`private(mask:)`](oslogprivacy/private(mask:).md), and [`sensitive(mask:)`](oslogprivacy/sensitive(mask:).md) methods. Using a hash string makes it possible to correlate log messages that contain the same original value, which helps you protect the user’s privacy and still diagnose issues surrounding a specific value.

## Topics

### Getting the Privacy Options
- [static var auto: OSLogPrivacy](oslogprivacy/auto.md)
  The standard option to let the system determine whether to redact or display a value.
- [static var `private`: OSLogPrivacy](oslogprivacy/private.md)
  The standard option to always redact the interpolated value.
- [static var `public`: OSLogPrivacy](oslogprivacy/public.md)
  The standard option to always show the interpolated value.
- [static var sensitive: OSLogPrivacy](oslogprivacy/sensitive.md)
  The option to always redact interpolated values that contain sensitive information.
### Creating a Custom Privacy Mask
- [static func auto(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/auto(mask:).md)
  Returns a privacy structure that determines whether to redact or show values according to their type, and customizes the display of redacted values.
- [static func `private`(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/private(mask:).md)
  Returns a privacy structure that marks an interpolated value as private, and customizes the display of redacted values.
- [static func sensitive(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/sensitive(mask:).md)
  Returns a privacy structure that marks an interpolated value as sensitive, and customizes the display of redacted values.
- [OSLogPrivacy.Mask](oslogprivacy/mask.md)
  A mask that establishes how the system displays a redacted value in a log message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy)*