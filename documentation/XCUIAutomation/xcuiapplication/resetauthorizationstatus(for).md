# resetAuthorizationStatus(for:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Resets the authorization status for a protected resource.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+
- watchOS 6.2+
- Xcode 16.3+

## Declaration

```swift
func resetAuthorizationStatus(for resource: XCUIProtectedResource)
```

```objc
- (void) resetAuthorizationStatusForResource:(XCUIProtectedResource) resource;
```

## Parameters

- `resource`: A system resource that requires user authorization to access.

## See Also

### Resetting authorization status
- [enum XCUIProtectedResource](../xcuiprotectedresource.md)
  A system resource that requires user authorization to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/resetauthorizationstatus(for:))*