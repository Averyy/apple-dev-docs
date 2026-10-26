# requestWithSession:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a scene session activation request object with a scene session that you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) requestWithSession:(UISceneSession *) session;
```

#### Return Value

A scene session activation request object.

#### Discussion

Create an activation request with this method when you want the system to activate an existing scene session that you provide.

## Parameters

- `session`: The specific scene session to activate.

## See Also

### Creating a request
- [+ request](./request.md)
  Creates a scene session activation request object.
- [+ requestWithRole:](./requestwithrole_.md)
  Creates a scene session activation request object with a role that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithsession:)*