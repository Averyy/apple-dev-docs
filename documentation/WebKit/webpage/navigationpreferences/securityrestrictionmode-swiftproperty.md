# securityRestrictionMode

**Framework**: WebKit  
**Kind**: property

Security restriction mode for this navigation.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
var securityRestrictionMode: WebPage.NavigationPreferences.SecurityRestrictionMode { get set }
```

#### Discussion

Security restriction modes provide different levels of security hardening for high-risk browsing contexts. `SecurityRestrictionMode.maximizeCompatibility` provides additional hardening while maintaining full web compatibility:

- JavaScript JIT compilation disabled (interpreter-only execution)
- Increased Memory Tagging Extension (MTE) coverage across allocations in the WebContent process Setting a security restriction mode creates separate, isolated WebContent processes for the specified protection level. This preference only applies to main frame navigations and will be ignored for subframe navigations. When set for a main frame, all subframe content and opened windows inherit the same security restrictions. When the system has chosen `SecurityRestrictionMode.lockdown` (e.g., in Lockdown Mode), attempts to set a less restrictive mode will fail silently. The default value is `SecurityRestrictionMode.none`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/securityrestrictionmode-swift.property)*