# WKUserInterfaceDirectionPolicy.system

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

The directionality follows the view’s user interface layout direction.

**Availability**:
- macOS 10.12+

## Declaration

```swift
case system
```

```c
WKUserInterfaceDirectionPolicySystem
```

#### Discussion

The web view adheres to the direction in its [`userInterfaceLayoutDirection`](../../AppKit/nsview/userinterfacelayoutdirection.md) property.

## See Also

### Direction Policies
- [WKUserInterfaceDirectionPolicy.content](./content.md)
  The directionality follows the CSS/HTML/XHTML specifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserinterfacedirectionpolicy/system)*