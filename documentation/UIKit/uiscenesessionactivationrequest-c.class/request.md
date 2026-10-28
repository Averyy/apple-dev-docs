# request

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a scene session activation request object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) request;
```

## Return Value

A scene session activation request object.

## Discussion

When you create a scene session activation request object with this method, [`role`](./role.md) defaults to [`windowApplication`](../uiscenesession/role-swift.struct/windowapplication.md).

## See Also

### Creating a request
- [+ requestWithRole:](./requestwithrole_.md)
  Creates a scene session activation request object with a role that you provide.
- [+ requestWithSession:](./requestwithsession_.md)
  Creates a scene session activation request object with a scene session that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/request)*