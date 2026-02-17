# WebPage.NavigationPreferences.SecurityRestrictionMode

**Framework**: WebKit  
**Kind**: enum

Security restriction modes for WebView content.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst ?+
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
enum SecurityRestrictionMode
```

## Topics

### Enumeration Cases
- [WebPage.NavigationPreferences.SecurityRestrictionMode.lockdown](webpage/navigationpreferences/securityrestrictionmode-swift.enum/lockdown.md)
  Maximum security restrictions including feature disablement. Applied automatically by the system in Lockdown Mode.
- [WebPage.NavigationPreferences.SecurityRestrictionMode.maximizeCompatibility](webpage/navigationpreferences/securityrestrictionmode-swift.enum/maximizecompatibility.md)
  Enhanced security protections optimized for maintaining web compatibility. Disables JIT compilation and enables increased MTE adoption.
- [WebPage.NavigationPreferences.SecurityRestrictionMode.none](webpage/navigationpreferences/securityrestrictionmode-swift.enum/none.md)
  No additional security restrictions beyond WebKit defaults.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/securityrestrictionmode-swift.enum)*